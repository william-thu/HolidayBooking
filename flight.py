def obtainDetails(flights):
  more_flights = "yes"
  while more_flights == "yes":
      destination = input("Destination of the flight: ")
      date_of_departure = input("Date of departure: ")
      time_of_departure = input('Time of daparture:')
      date_of_arrival = input('Date of arrival:')
      time_of_arrival = input("Time of arrival: ")
      cost = float(input("Cost of the flight: "))
      flight = {}
      flight["Destination"] = destination
      flight["Departure date"] = date_of_departure
      flight["Departure time"] = time_of_departure
      flight["Arrival date"] = date_of_arrival
      flight["Arrival time"] = time_of_arrival
      flight["Cost"] = cost
      flights.append(flight)
      more_flights = input("Do you want to add another flight? yes or no: ")


def printDetails(flights):
  for flight in flights:
      print('The destination of this flight : ' + flights[0]["Destination"])
      print('The departure date of this flight : ' +  flights[0]["Departure date"])
      print('The departure time of this flight : ' +  flights[0]["Departure time"])
      print('The arrival date of this flight : ' +  flights[0]["Arrival date"])
      print('The arrival time of this flight : ' +  flights[0]["Arrival time"])
      print('The cost of this flight : ' +  str(flights[0]["Cost"]))


def getTotalCost(flights):
  total_cost = 0
  for flight in flights:
      total_cost = total_cost + float(flight["Cost"])
  return total_cost