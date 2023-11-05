def obtainDetails(excursions):
    more_excursions = "yes"
    while more_excursions == "yes":
        venue = input("Name of the venue: ")
        date = input("Date of the excursion: ")
        time = input("Time of the excursion: ")
        cost = input("Cost of the excursion: ")
        excursion = {}
        excursion["Venue"] = venue
        excursion["Date"] = date
        excursion["Time"] = time
        excursion["Cost"] = cost
        excursions.append(excursion)
        more_excursions = input("Do you want to add another excursion? yes or no: ")


def printDetails(excursions):
    for excursion in excursions:
        print(excursion["Venue"])
        print(excursion["Date"])
        print(excursion["Time"])
        print(excursion["Cost"])


def getTotalCost(excursions):
    total_cost = 0
    for excursion in excursions:
        total_cost = total_cost + float(excursion["Cost"])
    return total_cost