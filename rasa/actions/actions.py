from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCurrentIssLocation(Action):

    def name(self) -> Text:
        return "action_current_iss_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="[Placeholder for the current ISS location]")

        return []

class ActionFutureIssLocation(Action):

    def name(self) -> Text:
        return "action_future_iss_location"
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if(len(tracker.latest_message['entities']) == 0):
            dispatcher.utter_message(text="I'm sorry, but I didn't understand your formatting. Please try again.")
        else:
            dispatcher.utter_message(text="[Placeholder for the ISS location at: " + tracker.latest_message['entities'][0]['value'] + " ]")

        return []

