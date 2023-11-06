def obtainDetails(flights):
    # Define valid ranges of values
    month = ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    day = list(range(0,32))
    hour = list(range(0,25))
    minute = list(range(0,61))
    correct_input = True
    more_flights = "yes"
    while correct_input == True and more_flights == "yes":
        destination = input("Destination of the flight: ")
        month_of_departure = input("Month of departure: ")
        if month_of_departure.upper() in month:
            correct_input = True
        else:
            print('Please input a valid month!')
            break
        day_of_departure = input("Day of departure: ")
        if int(day_of_departure) in day:
            correct_input = True
        else:
            print('Please input a valid day!')
            break
        hour_of_departure = input('Time(hour) of daparture:')
        if int(hour_of_departure) in hour:
            correct_input = True
        else:
            print('Please input a valid hour!')
            break
        minute_of_departure = input('Time(minute) of daparture:')
        if int(minute_of_departure) in minute:
            correct_input = True
        else:
            print('Please input a valid minute!')
            break
        month_of_arrival = input("Month of arrival: ")
        if month_of_arrival.upper() in month:
            correct_input = True
        else:
            print('Please input a valid month!')
            break
        day_of_arrival = input("Day of arrival: ")
        if int(day_of_arrival) in day:
            correct_input = True
        else:
            print('Please input a valid day!')
            break
        hour_of_arrival = input('Time(hour) of arrival:')
        if int(hour_of_arrival) in hour:
            correct_input = True
        else:
            print('Please input a valid hour!')
            break
        minute_of_arrival = input('Time(minute) of arrival:')
        if int(minute_of_arrival) in minute:
            correct_input = True
        else:
            print('Please input a valid minute!')
            break
        cost = float(input("Cost of the flight: "))
        flight = {}
        flight["Destination"] = destination
        flight["Departure month"] = month_of_departure
        flight["Departure day"] = day_of_departure
        flight["Departure hour"] = hour_of_departure
        flight["Departure minute"] = minute_of_departure
        flight["Arrival month"] = month_of_arrival
        flight["Arrival day"] = day_of_arrival
        flight["Arrival hour"] = hour_of_arrival
        flight["Arrival minute"] = minute_of_arrival
        flight["Cost"] = cost
        flights.append(flight)
        more_flights = input("Do you want to add another flight? yes or no: ")


def printDetails(flights):
    for flight in flights:
        print('Destination of this flight : ' + flight["Destination"])
        print('Departure date of this flight : ' +  flight["Departure day"] +' '+ flight["Departure month"].upper())
        print('Departure time of this flight : ' +  flight["Departure hour"] + ' : ' + flight["Departure minute"])
        print('Arrival date of this flight : ' +  flight["Arrival day"] +' '+ flight["Arrival month"].upper())
        print('Arrival time of this flight : ' +  flight["Arrival hour"] + ' : ' + flight["Arrival minute"])
        print('Cost of this flight : ' +  str(flight["Cost"]))


def getTotalCost(flights):
    total_cost = 0
    for flight in flights:
        total_cost = total_cost + float(flight["Cost"])
    return total_cost
