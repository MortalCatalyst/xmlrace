# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xmltodict


with open('20160409RAND0.xml') as f:
    my = xmltodict.parse(f.read())
    for event in my['meeting']:
        eventID = event["@id"]
        location = event["@venue"]
        eventDate = event["@date"]
        print( eventID + '\t' + location + '\t' + eventDate)
        for race in my['meeting']['race']:
            print(race["@id"] + '\t' + race["@number"])
            for noms in race['nomination']:
                saddle = noms["@number"]
                horse = noms["@horse"]
                horseId = noms["@id"]
                print(saddle + '\t' + horse + '\t' + horseId)
