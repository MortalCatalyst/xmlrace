'''
Created on 2 Jul 2014

@author: sayth
'''
import csv
import re
from sys import argv
SCRIPT, FILENAME = argv


def out_file_name(file_name):
    """take an input file and keep the name with appended _clean"""
    file_parts = file_name.split(".",)
    output_file = file_parts[0] + '_clean.' + file_parts[1]
    return output_file


def race_table(text_file):
    """utility to reorganise poorly made csv entry"""
    output_table = []
    for record in text_file:
        if record[0] == 'Meeting':
            meeting = record[3]
            rail = record[6]
            weather = record[7]
            track = record[8]
        elif record[0] == 'Race':
            date = record[13]
            race = record[1]
            benchmark = record[4]
            distance = record[5]
        elif record[0] == 'Horse':
            number = record[1]
            name = record[2]
            jockey = record[6]
            barrier = record[7]
            weight = record[8]
            results = record[9]
            res_split = re.split('[- ]', results)
            starts = res_split[0]
            wins = res_split[1]
            seconds = res_split[2]
            thirds = res_split[3]
            try:
                prizemoney = res_split[4]
            except IndexError:
                prizemoney = 0
            trainer = record[4]
            location = record[5]
            b_rating = record[15]
            sex = record[16]
            print(name, wins, seconds)
            output_table.append(
                (meeting, date, rail, weather, track, distance,
                 benchmark, race, number, name, sex, b_rating,
                 weight, barrier, starts, wins, seconds,
                 thirds, prizemoney, trainer, location, jockey))
    return output_table

MY_FILE = out_file_name(FILENAME)

# with open(FILENAME, 'r') as f_in, open(MY_FILE, 'w') as f_out:
#     for line in race_table(f_in.readline()):
#         new_row = line
with open(FILENAME, 'r') as f_in, open(MY_FILE, 'w') as f_out:
    lines = filter(None, (line.rstrip() for line in f_in))
    CONTENT = csv.reader(row for row in lines if not row.startswith('<!--'))
    # print(content)
    FILE_CONTENTS = race_table(CONTENT)
    # print new_name
    # f_out.write(str(FILE_CONTENTS))
    headers = ['MEETING', 'DATE', 'RAIL', 'WEATHER', 'TRACK', 'DISTANCE',
               'BENCHMARK', 'RACE', 'NUMBER', 'NAME', 'SEX', 'B_RATING',
               'WEIGHT', 'BARRIER', 'STARTS', 'WINS', 'SECONDS', 'THIRDS',
               'PRIZEMONEY', 'TRAINER', 'LOCATION', 'JOCKEY']

    f_csv = csv.writer(f_out)
    f_csv.writerow(headers)
    f_csv.writerows(FILE_CONTENTS)


# Old implementation for reference
#     input_table = [[item.strip(' "') for item in record.split(',')]
#                    for record in text_file.splitlines()]
# At this point look at input_table to find the record indices
#     identity = string.maketrans("", "")
#     print(input_table)
#     input_table = [s.translate(identity, ",'") for s
#                    in input_table]

if __name__ == '__main__':
    pass
