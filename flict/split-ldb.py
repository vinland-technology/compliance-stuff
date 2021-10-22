#!/usr/bin/python3

import json
import sys

TRANS_FILE = "translation.json"

def read_trans_file(cf):
    with open(cf) as fp:
        return json.load(fp)

def main():

    translations = read_trans_file(TRANS_FILE)

    trans_map = {}
    
    for translation in translations ['translations']:
        #print (" * " + str(translation))
        spdx = translation['spdx_id']
        le = translation['license_expression']
        if le in trans_map:
            if trans_map[le] == spdx:
                trans_map[le] = None
                pass
            else:
                #                print(le + " --> " + spdx + " already defined as: " + str(trans_map[le]) + "  | " + str(len(list(trans_map))))
                trans_map[le] = None
        else:
            trans_map[le] = spdx

    clean = []
    dirty = []
    for t in translations ['translations']:
        spdx = t['spdx_id']
        le = t['license_expression']
        if trans_map[le] == None:
            clean.append({
                "spdx_id": spdx,
                "comment": None,
                "license_expression": le
                })
        else:
            dirty.append({
                "spdx_id": spdx,
                "comment": None,
                "license_expression": le
                })

    print("Original: " + str(len(translations ['translations'])), file=sys.stderr)
    print("Clean: " + str(len(clean)), file=sys.stderr)
    print("Dirty: " + str(len(dirty)), file=sys.stderr)
    translations ['translations'] = clean
    translations ['failed_translations'] = dirty
    print(json.dumps(translations))
        
            
if __name__ == '__main__':
    main()

