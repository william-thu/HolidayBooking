# -*- coding: utf-8 -*-


def obtainDetails(car_hires):
    more_car = "yes"

    while more_car == "yes":
        car_type = input("The type of car (SUV or Bus, ...):")
        car_seats = input("The number of seats (2, 4, 5, 7, ...):")
        car_brand_name = input("The brand name of car(Cherry,Geely,Volvo,)")
        car_price = input("The price of car (200, 300, ...):")
        car_start_date = input("The start date to hire car (05-11-2023):")
        car_end_date = input("The end date to hire car (09-11-2023):")

        hire = {}
        hire["car_type"] = car_type
        hire["car_seats"] = car_seats
        hire["car_brand_name"] = car_brand_name
        hire["car_price"] = car_price
        hire["car_start_date"] = car_start_date
        hire["car_end_date"] = car_end_date

        car_hires.append(hire)
        more_car = input("Do you want to hire another car? yes or no: ")


def printDetails(car_hires):
    for hire in car_hires:
        print(hire["car_type"])
        print(hire["car_seats"])
        print(hire["car_brand_name"])
        print(hire["car_price"])
        print(hire["car_start_date"])
        print(hire["car_end_date"])


def getTotalCost(car_hires):
    total_cost = 0
    for hire in car_hires:
        total_cost = total_cost + float(hire["car_price"])
    return total_cost