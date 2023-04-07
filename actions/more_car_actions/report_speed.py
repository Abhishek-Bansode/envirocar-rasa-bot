from typing import Dict, Text, Any, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionReportSpeed(Action):
    def name(self) -> Text:
        return "action_report_speed"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:

        speed = tracker.get_slot("speed")

        # call external API to report speed
        response = requests.post(
            "https://example.com/report_speed",
            data={"speed": speed}
        )

        dispatcher.utter_message(f"Speed reported as {speed} km/h.")

        return [SlotSet("speed", speed)]