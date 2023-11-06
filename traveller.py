"""
---------------------------------------------------
Responsible team member: Phyo Nyein Thu (William)
---------------------------------------------------
"""

# Function to check if input has any special characters
def has_special_characters(input_string):
    special_characters = "!`¬£$%^&*()-_=+[]{}#~'@;:/?><.,|"
    for char in input_string:
        if char in special_characters:
            return True
        else:
            return False

# Function to check if input has any numbers
def has_numerical_characters(input_string):
    numerical_characters = "1234567890"
    for char in input_string:
        if char in numerical_characters:
            return True
        else:
            return False

# Function to validate Date of Birth format
def validate_dob(dob):
    valid_months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    # Split the provided dob by '/'
    date_parts = dob.split('/')

    # Check the three parts of the format, and assign them to dd/mm/yyyy respectively
    if len(date_parts) != 3:
        print("Invalid DoB provided.")
        return False
    else:
        day = date_parts[0]
        month = date_parts[1]
        year = date_parts[2]
        if not (day.isdigit() and year.isdigit()):
            print("Day and year must be numeric values.")
            return False
        elif len(day) >= 3 or int(day) >= 32:
            print("Invalid date. (1-31 only)")
            return False
        elif len(year) >= 5:
            print("Invalid year.")
            return False
        if month.lower() not in valid_months:
            print("Use three-letter abbreviations (jan, feb, etc...)")
            return False
    return True

# Get traveller details
def obtainDetails(travellers):
    print("-------------- You are now booking for a Holiday! --------------")
    more_travellers = True
    while more_travellers == True:
        valid_name = False
        valid_dob = False
        valid_phone = False
        valid_passport = False

        # Obtain traveller's name
        while valid_name == False:
            name = input("Enter traveller's name: ")
            if has_numerical_characters(name):
                print("Name cannot contain numeric characters.")
            elif has_special_characters(name):
                print("Name cannot contain special characters.")
            else:
                valid_name = True

        # Obtain traveller's DoB
        while valid_dob == False:
            dob = input("Enter Date of Birth (dd/mm/yyyy) - Month must be 3-letters abbreviated : ")
            if not validate_dob(dob):
                print("Use the provided format.")
            else:
                valid_dob = True

        # Obtain Traveller's Phone Number
        while valid_phone == False:
            phoneNo = input("Enter Phone Number: ")
            if has_special_characters(phoneNo):
                print("Phone no. cannot contain special characters.")
            elif not has_numerical_characters(phoneNo):
                print("Phone no. cannot contain non-numeric characters.")
            elif int(phoneNo) <= 9:
                print("Phone no. must be at least 10 digits long.")
            else:
                valid_phone = True

        # Obtain Traveller's Passport
        while valid_passport == False:
            passportNo = input("Enter passport number: ")
            if has_special_characters(passportNo):
                print("Passport cannot contain special characters.")
            else:
                valid_passport = True

        traveller = {
            "Name": name,
            "Date of Birth": dob,
            "Passport Number": passportNo,
            "Phone Number": phoneNo
        }

        travellers.append(traveller)
        while True:
            response = input("Do you want to enter another traveller information? (yes / no): ").lower()
            if response == "yes":
                break
            elif response == "no":
                more_travellers = False
                break
            else:
                print("Invalid response. Please enter 'yes' or 'no'.")


def printDetails(travellers):
    print("--------------- Traveller Details ---------------")
    for traveller in travellers:
        print("Name: ", traveller["Name"])
        print("Date of Birth: ", traveller["Date of Birth"])
        print("Passport Number: ", traveller["Passport Number"])
        print("Phone Number: ", traveller["Phone Number"])
        print("------------------------------------------")



