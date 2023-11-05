#zero or more hotels
# name of hotel, address, star rating, board

#input the hotels details - name of hotel, address, star rating, board
# address = City, street, number

def checkErrors(input):
    if len(input) == 0 or input.isdigit() or len(input) < 4:
        print("Error! Enter correct details")
        print("Your input was either empty, a number was provided or it was less than 4 letters")
        return False
    else:
        return True



def obtainDetails(hotels):
    isHotel = True
    star_rating = [1, 2, 3, 4, 5]
    board_options = ["full", "half", "bed and breakfast"]
    print("The next step is to book your hotels")

    while isHotel == True:
        name_input = input("Enter the name of the hotel: ")

        while checkErrors(name_input) == False:
            name_input = input("Enter the name of the hotel: ")


        print("Enter the full address of hotel")
        city_input = input("City: ")

        while checkErrors(city_input) == False:
            city_input = input("City: ")

        street_input = input("Street: ")
        while checkErrors(street_input) == False:
            street_input = input("Street: ")


        building_valid = False
        while building_valid == False:
            building_number_input = input("Building number: ")
            if len(building_number_input) == 0 or building_number_input.isdigit() == False or len(building_number_input) > 4:
                print("Error! Enter correct building number")
                print("Must be a number.")
            else:
                building_valid = True
                full_address = building_number_input + " " + street_input + " " + city_input


                star_valid = False
                while star_valid == False:
                    star_input = input("Please select a star rating (1 to 5): ")
                    if int(star_input) not in star_rating:
                        print("Error! Select from 1 to 5")
                    else:
                        star_valid = True
                        board_valid = False
                        while board_valid == False:
                            board_input = input("Please type one of the board options -> full, half, bed and breakfast: ")
                            if board_input not in board_options:
                                print("Error! Enter correct option")
                            else:
                                board_valid = True

                        cost_input = input("Enter the cost (in pounds): ")

                        hotel_details = {"Name": name_input,"Address": full_address,"Rating" : star_input,
                                         "Board" : board_input, "Cost": cost_input }

                        hotels.append(hotel_details)
                        other_hotel_input = input("Do you want to add another hotel? ")
                        if other_hotel_input.capitalize() == "Yes":
                            continue
                        else:
                            isHotel = False



def printDetails(hotels):
    carry_on = False
    while carry_on == False:
        question_input = input("Type 'all' to get all hotels details or type the number of hotel:  ")
        if question_input.capitalize() == "All":
            carry_on = True
            for hotel in hotels:
                print("Name: " + hotel["Name"])
                print("Address: " + hotel["Address"])
                print("Rating: " + hotel["Rating"])
                print("Board: " + hotel["Board"])
                print("Cost: " + hotel["Cost"])
                print()
        elif  "1" <= question_input <= "5":
            carry_on = True
            i = int(question_input)
            if 0<=i<=5:
                print("Name: " + hotels[i]["Name"])
                print("Address: " + hotels[i]["Address"])
                print("Rating: " + hotels[i]["Rating"])
                print("Board: " + hotels[i]["Board"])
                print("Cost: " + hotels[i]["Cost"])
        else:
            carry_on = False
            print("Incorrect input")



def getTotalCost(hotels):
    total_cost = 0
    for hotel in hotels:
        total_cost = total_cost + float(hotel["Cost"])
    return total_cost
