from typing import Dict, Text, Any, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionReportAcceleration(Action):
    def name(self) -> Text:
        return "action_report_acceleration"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:

        acceleration = tracker.get_slot("acceleration")

        # call external API to report acceleration
        response = requests.post(
            "https://example.com/report_acceleration",
            data={"acceleration": acceleration}
        )

        dispatcher.utter_message(f"Acceleration reported as {acceleration} m/s².")

        return [SlotSet("acceleration", acceleration)]