#!/usr/bin/env python3

import json
import os


def strip_headers(filename):
	s = open(filename).read()
	data = json.loads(s)
	if 'ExportedDateTime' in data['Header']:
		del data['Header']['ExportedDateTime']
	if 'ArchiveFileName' in data['Header']:
		del data['Header']['ArchiveFileName']
	s = json.dumps(data, indent=2, ensure_ascii=False)
	open(filename, 'w', encoding='utf-8').write(s)


for root, dirs, files in os.walk('.', topdown=False):
    for name in files:
    	if name.endswith('.json'):
        	strip_headers(os.path.join(root, name))
