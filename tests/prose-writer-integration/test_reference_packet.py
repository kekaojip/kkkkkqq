"""Behavioral checks for retrieval transport, not a test of literary quality.

Fixtures below are synthetic and must never be used as production donor text.
"""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / 'skills/prose-preparation/runtime/source_shadow_packet.py'
FIDELITY = ROOT / 'skills/prose-preparation/runtime/source_shadow_fidelity.py'
spec = importlib.util.spec_from_file_location('reference_packet', PACKET)
runtime = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runtime)


class ReferencePacketTests(unittest.TestCase):
    def setUp(self):
        self.source = '  甲问：“还走吗？”\n\n\n乙答：“等人。”  \n \n甲留在门边。\n'
        self.story = {
            'plot': '林迟等钱到账后才买米；本段结束时尚未到账。',
            'character_block': {'林迟': '先问到账时间；不抱怨，也不离开。'},
            'emotional_thread': '担心今天没饭吃，但没有改变等待的决定。',
            'safe_continuity': {'balance': 0, 'location': '米铺门口'},
            'forbidden_reveals': ['后台作者真相不得传入正文'],
            'segments': [{
                'id': 'wait', 'target_facts': ['等到账', '没有买米'],
                'pov': '林迟', 'dwell': 'BRIDGE_FAST',
                'character_state': {'purpose': '问还要等多久'},
                'emotional_residue': '担心', 'local_stop': '仍在等',
                'new_caller_field': {'must_survive': ['完整的细节，不是标签']},
                'source_fact_blacklist': ['甲', '乙'], 'tags': ['DIALOGUE']
            }]
        }

    def test_complete_input_survives_without_mutation(self):
        original = copy.deepcopy(self.story)
        packet = runtime.build_packet(self.source, self.story)
        self.assertEqual(packet['approved_story_input'], original)
        for key, value in original['segments'][0].items():
            self.assertEqual(packet['segments'][0][key], value)
        self.assertEqual(self.story, original)
        packet['approved_story_input']['character_block'].clear()
        self.assertEqual(self.story, original)

    def test_reference_windows_preserve_exact_source_bytes(self):
        packet = runtime.build_packet(self.source, self.story, radius=1)
        for segment in packet['segments']:
            for window in [segment['primary_window'], *segment['alternate_windows']]:
                expected = self.source[window['source_start_char']:window['source_end_char']]
                self.assertEqual(window['text'].encode(), expected.encode())
        self.assertIn('\n\n\n', packet['segments'][0]['primary_window']['text'])

    def test_keyword_hit_never_certifies_semantic_fit(self):
        # Matching dialogue markers cannot prove equivalent plot/POV/dwell.
        packet = runtime.build_packet(self.source, self.story)
        self.assertEqual(packet['segments'][0]['reference_selection_status'],
                         'CANDIDATES_REQUIRE_SEMANTIC_REVIEW')
        self.assertEqual(packet['source_verification_authority'],
                         'S3_SOURCE_ACQUISITION_NOT_THIS_RETRIEVER')
        self.assertNotIn('recurring_phrase_inventory', packet)
        self.assertNotIn('writer_rules', packet)
        self.assertEqual(packet['prose_realization_skill'],
                         'skills/novel-prose-writer-zh/SKILL.md')

    def test_unusable_input_stops_instead_of_emitting_success(self):
        for story in ({}, {'segments': []}, {'segments': [None]}):
            with self.assertRaises(ValueError):
                runtime.build_packet(self.source, story)
        with self.assertRaises(RuntimeError):
            runtime.build_packet(' \n\n', self.story)
        with self.assertRaises(ValueError):
            runtime.build_packet(self.source, self.story, radius=-1)

    def test_original_window_helper_remains_usable(self):
        self.assertEqual(runtime.windows(['甲。', '乙。'], 0)[0]['text'], '甲。')

    def test_both_cli_paths_execute(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            (td/'source.txt').write_text(self.source, encoding='utf-8')
            (td/'story.json').write_text(json.dumps(self.story, ensure_ascii=False), encoding='utf-8')
            subprocess.run([sys.executable, str(PACKET), '--source-body', str(td/'source.txt'),
                            '--story', str(td/'story.json'), '--out', str(td/'packet.json')],
                           check=True, capture_output=True)
            packet = json.loads((td/'packet.json').read_text())
            self.assertEqual(packet['approved_story_input'], self.story)
            (td/'candidate.txt').write_text('林迟还在米铺门口等着。', encoding='utf-8')
            subprocess.run([sys.executable, str(FIDELITY), '--candidate', str(td/'candidate.txt'),
                            '--source-body', str(td/'source.txt'), '--out', str(td/'diagnosis.json')],
                           check=True, capture_output=True)
            diagnostic = json.loads((td/'diagnosis.json').read_text())
            self.assertTrue(diagnostic['diagnostic_only'])
            self.assertNotIn('pass', diagnostic)
            self.assertNotIn('rewrite_required', diagnostic)


if __name__ == '__main__':
    unittest.main()
