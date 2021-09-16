import json
import argparse

def parseJson(channelID,date,file):
    objectsFound = 0
    print("BEGIN \n")
    with open(file, 'r') as dataFile:
        for data in dataFile:
            obj = json.loads(data) 
            try:
                if obj['timestamp'][1:11] == date and obj['channel'] == channelID:
                    objectsFound += 1
                    print("MESSAGE")
                    print("Event Type: " + obj["event_type"])
                    print("Message ID: " + obj["message_id"])
                    print("Time Sent: " + obj["timestamp"])
                    print("Word Count: " + obj["word_count"])
                    print()
            except:
                0==0
    print("\nEND")
    return objectsFound


if __name__ == "__main__":
    channelID = ""
    file = ""
    date = ""
    parser = argparse.ArgumentParser()
    parser.add_argument("-c","--channel", help = "channel ID",required = True)
    parser.add_argument("-d","--date", help = "Date in YEAR-MONTH-DAY format", required = True)
    parser.add_argument("-f","--file", help = "filename", required = True)
    args = parser.parse_args()

    results = parseJson(args.channel, args.date, args.file)
    print("Results: " + str(results))
