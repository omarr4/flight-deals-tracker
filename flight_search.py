import requests
import os
from datetime import datetime, timedelta
from flight_data import FlightData

HEADERS = {
    "apikey": "example key"
}


class FlightSearch:

    def __init__(self):
        self.LOCATIONS_ENDPOINT = " https://tequila-api.kiwi.com/locations/query"
        self.SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
        self.AMMAN_CODE = "AMM"

    def get_code(self, city):
        """"Returns the code of the city argument passed."""
        response = requests.get(url=self.LOCATIONS_ENDPOINT,
                                params={
                                    "term": city.lower()
                                },
                                headers=HEADERS
                                ).json()['locations'][0]['code']
        return response

    def get_flight_data(self, city_code):
        """"
        Returns the flight data as a FlightData object.
        Data retrieved:
            Destination city and airport, departure date, number of nights and flight price.
        """
        tomorrow = datetime.now().date() + timedelta(days=1)
        date_to = tomorrow + timedelta(days=30) #days=180
        params = {
            "fly_from": self.AMMAN_CODE,
            "fly_to": city_code,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": date_to,
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 14,
            "max_stopovers": 100,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "JOD",
        }
        response = requests.get(url=self.SEARCH_ENDPOINT, params=params, headers=HEADERS)
        try:
            data = response.json()['data'][0]
            fl_data = FlightData(price=data['price'],
                                 dest_city=data['cityTo'],
                                 dest_airport=data['flyTo'],
                                 out_date=data['route'][0]['local_departure'][:10],
                                 num_nights=data['nightsInDest'],
                                 link=data['deep_link']
                                 )
            return fl_data
        except IndexError:
            return "No flights found for"


