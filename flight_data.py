class FlightData:
    def __init__(self, price, dest_city, dest_airport, out_date, num_nights, link):
        self.price = price
        self.dest_city = dest_city
        self.dest_airport = dest_airport
        self.out_date = out_date
        self.num_nights = num_nights
        self.link = link

    def get_all_data(self):
        """"Returns all flight data in a readable format as a string."""
        return (
            f"Destination: {self.dest_city}\n"
            f"Airport: \"{self.dest_airport}\" Airport\n"
            f"Departure Date: {self.out_date}\n"
            f"Number of Nights: {self.num_nights} Nights\n"
            f"Price: {self.price} JOD\n\n"
            f"Link: {self.link}\n"
            f"------------------------------------------------------------------------------------------------------\n")
