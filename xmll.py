import xmltodict


with open('20160409RAND0.xml') as f:
    my = xmltodict.parse(f.read())

    print(my['meeting']["@id"])
#    for event in my['meeting']:
    eventID = my['meeting']["@id"]
    location = my['meeting']["@venue"]
    eventDate = my['meeting']["@date"]
#        print( eventID + '\t' + location + '\t' + eventDate)
    meeting = [eventID, location, eventDate]
    print(meeting)
    for race in my['meeting']['race']:
        print(race["@id"] + '\t' + race["@number"])
        for noms in race['nomination']:
            saddle = noms["@number"]
            horse = noms["@horse"]
            horseId = noms["@id"]
            print(saddle + '\t' + horse + '\t' + horseId)
