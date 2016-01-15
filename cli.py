#!/usr/bin/env python

import sys
import json

from bonamigator import bon_amic

# Given a json file as first parameter calculate the "bon amic"

if __name__=="__main__":

    with open(sys.argv[1]) as json_file:    
        data = json.load(json_file)

    participants = data["participants"].keys()
    excludes = data["excludes"].keys()

    bons_amics = bon_amic(participants)

    for give, recieve in bons_amics.items():
        print give + " give to " + recieve
