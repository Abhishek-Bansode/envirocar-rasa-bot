from typing import Dict, Text, Any, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionReportTemperature(Action):
    def name(self) -> Text:
        return "action_report_temperature"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:

        temperature = tracker.get_slot("temperature")

        # call external API to report temperature
        response = requests.post(
            "https://example.com/report_temperature",
            data={"temperature": temperature}
        )

        dispatcher.utter_message(f"Temperature reported as {temperature} °C.")

        return [SlotSet("temperature", temperature)]