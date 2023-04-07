# actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ReportFuelLevel(Action):
    def name(self) -> Text:
        return "action_report_fuel_level"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get fuel level from tracker
        fuel_level = tracker.latest_message['text']

        # TODO: Perform some action based on fuel level
        # For example, send a notification to the user to refuel their car

        # Send response to user
        dispatcher.utter_message(text="Thanks for letting me know your fuel level.")

        return []
