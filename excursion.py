"""
---------------------------------------------------
Team Member(s) contribution:

- William: validateMonth(), traveller.has_numerical_characters(),
error handling for venue name and date
- Aigerim : excursions limit
-
---------------------------------------------------
"""

import traveller

def validateMonth(month):
  valid_months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
  if month.upper() in valid_months:
    return True
  else:
    return False

def obtainDetails(excursions):
    print("-------------- You are now entering details for your excursion! --------------")
    more_excursions = "yes"
    while more_excursions == "yes":
        valid_venue = False
        valid_time_hour = False
        valid_time_setting = False
        valid_date_day = False
        valid_date_month = False

        # Get Venue Name
        while valid_venue == False:
          venue = input("Name of the venue: ")
          if traveller.has_special_characters(venue):
            print("Venue name cannot contain special characters.")
          else:
            valid_venue = True

        # Get Venue Date
        while valid_date_day == False:
          date_day = input("Excursion date (1-31): ")
          if traveller.has_numerical_characters(date_day) == False:
            print("Day of the date must be a numerical value.")
          elif int(date_day) < 1 or int(date_day) > 31:
            print("Not a valid date.")
          else:
            valid_date_day = True

        while valid_date_month == False:
          date_month = input("Month of the excursion (abbreviated): ")
          if validateMonth(date_month):
            valid_date_month = True
            date = date_day + ' ' + date_month.upper()
          else:
            print("Not a valid month.")

        # Get Venue Time
        while valid_time_hour == False:
          time_hour = input("Arrival Time (in hours): ")
          if traveller.has_numerical_characters(time_hour) == False:
            print("Time of the venue must be a number.")
          elif len(time_hour) >= 3 or int(time_hour) >= 25:
            print("Not a valid hour.")
          else:
            valid_time_hour = True

        while valid_time_setting == False:
          available_time_settings = ['am', 'pm']
          time_setting = input("AM or PM: ")
          if time_setting.lower() == available_time_settings[0]:
            valid_time_setting = True
            time = time_hour + str(time_setting)
          elif time_setting.lower() == available_time_settings[1]:
            valid_time_setting = True
            time = time_hour + ' ' + str(time_setting)
          else:
            print("Not a valid time setting.")

        cost = input("Cost of the excursion: ")

        excursion = {
          "Venue": venue,
          "Date": date,
          "Time": time,
          "Cost": cost
        }

        excursions.append(excursion)
        excursions_limit = 10
        while True:
            response = input("Do you want to enter another excursion? (yes / no): ").lower()
            if response == "yes" and len(excursions) < excursions_limit:
                break
            elif response == "yes" and len(excursions) >= excursions_limit:
                print("Oops! You've reached the limit")
                more_excursions = False
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
        print("Venue Cost: £", excursion["Cost"])
        print("------------------------------------------")


def getTotalCost(excursions):
    total_cost = 0
    for excursion in excursions:
        total_cost = total_cost + float(excursion["Cost"])
    return total_cost