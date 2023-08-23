class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

    def __str__(self):
        return f"Flight ID: {self.flight_id}, From: {self.source}, To: {self.destination}, Price: {self.price}"

class FlightDetails:
    def __init__(self):
        self.flights = []
        self.flights.append(Flight("AI161E90", "BLR", "BOM", 5600))
        self.flights.append(Flight("BR161F91", "BOM", "BBI", 6750))
        self.flights.append(Flight("AI161F99", "BBI", "BLR", 8210))
        self.flights.append(Flight("VS171E20", "JLR", "BBI", 5500))
        self.flights.append(Flight("AS171G30", "HYD", "JLR", 4400))
        self.flights.append(Flight("AI131F49", "HYD", "BOM", 3499))

    def search_flight(self, user_input):
        for flight in self.flights:
            if flight.flight_id == user_input or flight.source == user_input or flight.destination == user_input:
                print(flight)

flight_details = FlightDetails()
user_input = input("Enter Flight ID or Source City or Destination City: ")
flight_details.search_flight(user_input)
 