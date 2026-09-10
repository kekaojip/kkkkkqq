#!/usr/bin/env node
'use strict';
const fs = require('fs');
const path = require('path');
const zlib = require('zlib');
const crypto = require('crypto');
const Module = require('module');
const parts = ['01','02'];
const payload = parts.map(function (n) {
  return fs.readFileSync(path.join(__dirname, '.payloads', 'normalize-punctuation.js.' + n + '.b64'), 'utf8').trim();
}).join('');
const src = zlib.gunzipSync(Buffer.from(payload, 'base64'));
const actual = crypto.createHash('sha256').update(src).digest('hex');
const expected = 'a346f975de2d7a0d0fa935ab25cc58f853f7c7cbe29ea58e79835945e83803ad';
if (actual !== expected) throw new Error('embedded source checksum mismatch');
const m = new Module(__filename, module.parent);
m.filename = __filename;
m.paths = module.paths;
m._compile(src.toString('utf8'), __filename);
