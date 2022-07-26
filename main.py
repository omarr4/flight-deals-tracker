# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from add_user import AddUser
from notification_manager import NotificationManager

data_manager = DataManager()
prices_sheet_data = data_manager.get_data("prices")
flight_finder = FlightSearch()


def configure_iata(row, row_id, city_name):
    """"Returns the corresponding IATA Code.
    It checks if the city has an IATA Code value yet. If not; we update the value in the sheet.
    Otherwise, we just return it as is."""
    try:
        if row['iataCode'] == "":
            # find the city's iata code from the locations API endpoint
            iata = flight_finder.get_code(city_name)
            # update the iata code we got from the locations API into our sheet
            data_manager.update_prices_sheet(row_id=row_id, code=iata)
        else:
            iata = row['iataCode']

    except KeyError:
        iata = flight_finder.get_code(city_name)
        data_manager.update_prices_sheet(row_id=row_id, code=iata)

    return iata


def update_message(flight_data, row_id, row, message, city_name):
    try:
        if flight_data.price < row['lowestPrice']:
            message += f"{flight_data.price} JOD - NEW LOW PRICE!!\n"
            data_manager.update_prices_sheet(row_id=row_id, price=flight_data.price)

        message += flight_data.get_all_data()

    except AttributeError:
        message += (f"{flight_data} {city_name}.\n"
                    f"------------------------------------------------------------------------------------------------"
                    f"------\n")

    except KeyError:
        data_manager.update_prices_sheet(row_id=row_id, price=flight_data.price)
        message += flight_data.get_all_data()

    return message


def run():
    cust_list = DataManager().get_data("users")
    message = ""

    for row in prices_sheet_data:
        # Get the city name from the row
        city_name = row['city']

        # Get the row id as it is needed for when we make the API call to Sheety
        row_id = row['id']

        # Get IATA Code
        iata_code = configure_iata(row, row_id, city_name)

        # the big method that gets all the flight data and returns it as a FlightData object
        # OR a string if there were no flights found
        data = flight_finder.get_flight_data(iata_code)

        message = update_message(data, row_id, row, message, city_name)

    print(message)

    for customer in cust_list:
        notif = NotificationManager(customer['email'])
        notif.send_email(message)


# AddUser().add_user()
run()
