# ---------------------------- main.py - ---------------------------
import traveller
import hotel
import flight
import excursion  # this has been done for you
import car_hire  # only include if 4 students in a team

travellers = []
hotels = []
flights = []
excursions = []
car_hires = []  # only include if 4 students in a team

traveller.obtainDetails(travellers)
hotel.obtainDetails(hotels)
flight.obtainDetails(flights)
excursion.obtainDetails(excursions)  # this has been done for you
car_hire.obtainDetails(car_hires)  # only include if 4 students in a team

traveller.printDetails(travellers)
hotel.printDetails(hotels)
flight.printDetails(flights)
excursion.printDetails(excursions)  # this has been done for you
car_hire.printDetails(car_hires)  # only include if 4 students in a team

total_cost = 0
total_cost = hotel.getTotalCost(hotels)
total_cost = total_cost + flight.getTotalCost(flights)
total_cost = total_cost + excursion.getTotalCost(excursions)  # this has been done for you
total_cost = total_cost + car_hire.getTotalCost(car_hires)  # only include if 4 students in a team
print("Total cost of holiday: " + str(total_cost))



