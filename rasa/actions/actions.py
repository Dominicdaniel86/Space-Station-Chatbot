from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import os.path
import urllib.request
from datetime import datetime

filepath = "../data/iss-location.txt"
url = "https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.txt"


def download_file():
    # download (and replace) file
    if os.path.isfile(filepath):
        os.remove(filepath)
    urllib.request.urlretrieve(url, filepath)


def find_location(timestamp):
    file = open(filepath, "r")

    smaller_entry = ""
    bigger_entry = ""

    values = [
        int(timestamp[:4]), # year
        int(timestamp[5:7]), # month
        int(timestamp[8:10]), # day
        int(timestamp[11:13]), # hour
        int(timestamp[14:16]) # minute
    ]

    starting_line_found = False
    index = 1

    for line in file:
        if not starting_line_found:
            if "COMMENT End sequence of events" in line:
                starting_line_found = True
        else:
            values_line = [int(line[:4]), int(line[5:7]), int(line[8:10]), int(line[11:13]), int(line[14:16])]
            i = 0
            while i <= 4:
                if values[i] > values_line[i]:
                    smaller_entry = line
                    break
                elif values[i] < values_line[i]:
                    bigger_entry = line
                    break
                i += 1
        if bigger_entry != "":
            break
        index += 1
    
    if smaller_entry == "":
        return bigger_entry
    return smaller_entry


class ActionCurrentIssLocation(Action):

    def name(self) -> Text:
        return "action_current_iss_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        download_file()
        location = find_location(str(datetime.now()))

        dispatcher.utter_message(text=f"location: {location}")

        return []


class ActionFutureIssLocation(Action):

    def name(self) -> Text:
        return "action_future_iss_location"
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        download_file()
        
        if(len(tracker.latest_message['entities']) == 0):
            dispatcher.utter_message(text="I'm sorry, but I didn't understand your formatting. Please try again.")
        else:
            entity = tracker.latest_message['entities'][0]['value']
            location = find_location(entity)
            dispatcher.utter_message(text=f"location: {location}")

        return []

