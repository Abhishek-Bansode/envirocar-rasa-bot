from typing import Dict, Text, Any, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionReportBrake(Action):
    def name(self) -> Text:
        return "action_report_brake"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        brake_value = tracker.get_slot("brake_value")

        # You can perform any required action or API call here using the
        # brake_value and dispatcher object

        # For example, to send a response back to the user:
        if brake_value is not None:
            response = f"The current brake value is {brake_value}"
        else:
            response = "Sorry, I could not find the brake value."

        dispatcher.utter_message(text=response)

        return []