#!/usr/bin/env node
'use strict';
const fs=require('fs'),path=require('path'),zlib=require('zlib'),crypto=require('crypto'),Module=require('module');
const payload=Array.from({length:7},(_,i)=>fs.readFileSync(path.join(__dirname,'.payloads',`check-ai-patterns.js.${String(i+1).padStart(2,'0')}.b64`),'utf8').trim()).join('');
const src=zlib.gunzipSync(Buffer.from(payload,'base64'));
if(crypto.createHash('sha256').update(src).digest('hex')!=='d297fce88a4089989fe124f7f256bbf6ede6a614c0e6238ece1ae4a749eded71') throw new Error('embedded source checksum mismatch');
const m=new Module(__filename,module.parent);m.filename=__filename;m.paths=module.paths;m._compile(src.toString('utf8'),__filename);
