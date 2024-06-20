from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import os.path
import urllib.request

filepath = "../data/iss-location.txt"

class ActionCurrentIssLocation(Action):

    def name(self) -> Text:
        return "action_current_iss_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # download (and replace) file
        if os.path.isfile(filepath):
            os.remove(filepath)
        urllib.request.urlretrieve("https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.txt", filepath)

        print(os.path.abspath(__file__))
        file = open(filepath, "r")
        end_reached = False
        location = ""
        for line in file:
            if end_reached:
                location = line
                break
            if "COMMENT End sequence of events" in line:
                end_reached = True

        dispatcher.utter_message(text="location: " + location)

        return []

class ActionFutureIssLocation(Action):

    def name(self) -> Text:
        return "action_future_iss_location"
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # download (and replace) file
        if os.path.isfile("../../api-data/iss-location.txt"):
            os.remove("../../api-data/iss-location.txt")
        urllib.request.urlretrieve("https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.txt", "text.txt")

        if(len(tracker.latest_message['entities']) == 0):
            dispatcher.utter_message(text="I'm sorry, but I didn't understand your formatting. Please try again.")
        else:
            dispatcher.utter_message(text="[Placeholder for the ISS location at: " + tracker.latest_message['entities'][0]['value'] + " ]")

        return []

