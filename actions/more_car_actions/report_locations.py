import requests
from typing import Dict, Text, Any, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionReportLocation(Action):
    def name(self) -> Text:
        return "action_report_location"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:

        lat = tracker.get_slot("latitude")
        lon = tracker.get_slot("longitude")

        # call external API to report location
        response = requests.post(
            "https://example.com/report_location",
            data={"latitude": lat, "longitude": lon}
        )

        dispatcher.utter_message("Location reported.")

        return [SlotSet("latitude", lat), SlotSet("longitude", lon)]