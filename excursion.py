"""
---------------------------------------------------
Responsible team member(s):
-
-
---------------------------------------------------
"""

import traveller

def obtainDetails(excursions):
    print("-------------- You are now entering details for your excursion! --------------")
    more_excursions = "yes"
    while more_excursions == "yes":
        valid_venue = False
        while valid_venue == False:
          venue = input("Name of the venue: ")
          if traveller.has_special_characters(venue):
            print("Venue name cannot contain special characters.")
          else:
            valid_venue = True
        date = input("Date of the excursion: ")
        time = input("Time of the excursion: ")
        cost = float("Cost of the excursion: ")

        excursion = {
          "Venue": venue,
          "Date": date,
          "Time": time,
          "Cost": cost
        }

        excursions.append(excursion)
        while True:
            response = input("Do you want to enter another excursion? (yes / no): ").lower()
            if response == "yes":
                break
            elif response == "no":
                more_excursions = False
                break
            else:
                print("Invalid response. Please enter 'yes' or 'no'.")


def printDetails(excursions):
    print("--------------- Excursion Details ---------------")
    for excursion in excursions:
        print("Name of Venue: ", excursion["Venue"])
        print("Arrival Date: ", excursion["Date"])
        print("Arrival Time: ", excursion["Time"])
        print("Venue Cost: ", excursion["Cost"])
        print("------------------------------------------")


def getTotalCost(excursions):
    total_cost = 0
    for excursion in excursions:
        total_cost = total_cost + float(excursion["Cost"])
    return total_cost