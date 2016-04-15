import xmltodict
'''import csv
import re
from sys import argv
SCRIPT, FILENAME = argv


def out_file_name(file_name):
    """take an input file and keep the name with appended _clean"""
    file_parts = file_name.split(".",)
    output_file = file_parts[0] + '_clean.' + file_parts[1]
    return output_file'''

with open('20160319RHIL0.xml') as f:
    my = xmltodict.parse(f.read())
    # print(my['meeting']["@id"])
#    for event in my['meeting']:
    eventID = my['meeting']["@id"]
    location = my['meeting']["@venue"]
    eventDate = my['meeting']["@date"]
    meeting = [eventID, location, eventDate]
    # print(['meeting']['race']["@number"])
    fields = []
    for race in my['meeting']['race']:
        raceArr = []
        # race.append(race["@id"],race["@number"])
        raceNum = race["@number"]
        raceID = race["@id"]
        # print(race["@id"] + '\t' + race["@number"])
        for noms in race['nomination']:
            saddle = noms["@number"]
            horse = noms["@horse"]
            horseId = noms["@id"]
            barrier = noms["@barrier"]
            career = noms["@career"]
            rating = noms["@rating"]
            #sexA = noms["@sex"]
            #trackRec = noms["@thistrack"]
            age = noms["@age"]
            description = noms["@description"]
            #price = noms["@pricestarting"]
            weights = noms["@weight"]
            # print(saddle + '\t' + horse + '\t' + horseId)

            myArr = [eventID, location, eventDate, raceNum, raceID, saddle,
                     horse, horseId, barrier, career, age, description, weights]
            fields.append(myArr)


print(fields)

'''MY_FILE = out_file_name(FILENAME)

with open(FILENAME, 'r') as f_in, open(MY_FILE, 'w') as f_out:
    lines = filter(None, (line.rstrip() for line in f_in))
    CONTENT = csv.reader(row for row in lines if not row.startswith('<!--'))
    # print(content)
    FILE_CONTENTS = race_table(CONTENT)

    headers = ['MEETING', 'DATE', 'RAIL', 'WEATHER', 'TRACK', 'DISTANCE',
               'BENCHMARK', 'RACE', 'NUMBER', 'NAME', 'SEX', 'B_RATING',
               'WEIGHT', 'BARRIER', 'STARTS', 'WINS', 'SECONDS', 'THIRDS',
               'PRIZEMONEY', 'TRAINER', 'LOCATION', 'JOCKEY']

    f_csv = csv.writer(f_out)
    f_csv.writerow(headers)
    f_csv.writerows(FILE_CONTENTS)
'''
