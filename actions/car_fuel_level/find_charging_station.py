# actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class FindChargingStations(Action):
    def name(self) -> Text:
        return "action_find_charging_stations"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get user location from tracker
        user_location = tracker.get_slot('location')

        # TODO: Call an external API to find nearby charging stations based on user location
        # For example, using the Open Charge Map API
        response = requests.get('https://api.openchargemap.io/v3/poi/?output=json&latitude=' + str(user_location['lat']) + '&longitude=' + str(user_location['lon']) + '&distance=10&distanceunit=KM&maxresults=5&key=<your_api_key>')
        charging_stations = response.json()

        # Format response
        message = "Here are some nearby charging stations:\n"
        for station in charging_stations:
            message += f"{station['AddressInfo']['Title']}\n{station['AddressInfo']['AddressLine1']}, {station['AddressInfo']['Town']}\n\n"

        # Send response to user
        dispatcher.utter_message(text=message)

        return []
