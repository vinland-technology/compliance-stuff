#!/usr/bin/python3

import json
import sys

FLICT_TRANSL_FILE = "flict-translations.json"


def add_to_map(map, key, item):
    if key not in map:
        map[key] = set()
    map[key].add(item)
    

def main():

    with open(FLICT_TRANSL_FILE) as fp:
        translations = json.load(fp)
        translation_map = {}
        for translation in translations['translations']:
            add_to_map(translation_map, translation['spdx_id'], translation['license_expression'])

        print("# SPDX identifiers\n")
        for key, value in translation_map.items():
            print("## " + key + "\n")
            alias_set = set()
            #print("### Aliases\n")
            for alias in value:
                if alias in alias_set:
                    print("ERROR::::")
                    sys.exit(1)
                alias_set.add(alias)
                print(" * " + alias.replace("'", "") + "\n\n")
            

if __name__ == '__main__':
    main()

