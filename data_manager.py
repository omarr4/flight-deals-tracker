import requests


class DataManager:

    def __init__(self):
        self.SHEETY_ENDPOINT = "//example endpoint"
        self.AUTH_HEADER = {
            "Authorization": "example auth code"
        }

    def get_data(self, sheet_name):
        """"Returns a list of dictionaries with the sheet values."""
        response = requests.get(url=f"{self.SHEETY_ENDPOINT}/{sheet_name}", headers=self.AUTH_HEADER)
        sheet_data = response.json()[sheet_name]
        return sheet_data

    def update_prices_sheet(self, row_id, code=None, price=None):
        """"Updates the IATA Code of the passed id argument, if the city was found."""
        body = {
            "price": {
            }
        }

        if code is not None:
            body["price"]["iataCode"] = code
        if price is not None:
            body["price"]["lowestPrice"] = price

        requests.put(url=f"{self.SHEETY_ENDPOINT}/prices/{row_id}", json=body, headers=self.AUTH_HEADER)

    def add_data(self, sheet_name, data: dict):
        """Adds a city and its lowest price to the data sheet."""
        json = {
            sheet_name[:-1]: data
        }
        response = requests.post(url=f"{self.SHEETY_ENDPOINT}/{sheet_name}",
                                 json=json,
                                 headers=self.AUTH_HEADER)
        print(response.json())
