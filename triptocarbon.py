from request_and_distance import *
import requests

# response = requests.get('https://api.triptocarbon.xyz/v1/footprint?activity=10&activityType=miles&country=usa&mode=taxi')
# print(response.text)


# driving
# walking
# bicycling
# transit
# 
# 
# economyFlight
# businessFlight
# firstclassFlight
# anyFlight
# motorbike

def translateMode(googleMode):
    carTypes = set(["dieselCar", "petrolCar", "anyCar", "taxi"])
    transitTypes = set(["bus", "transitRail"])
    if googleMode == "driving":
        car = input("What type of car do you drive?:")
        while car not in carTypes:
            print("Try again")
            car = input("What type of car do you drive?:")
        return car
    elif googleMode == "walking":
        return None 
    elif googleMode == "bicycling":
        return None
    elif googleMode == "transit":
        transit = input("What type of transit?:")
        while transit not in transitTypes:
            print("Try again")
            transit = input("What type of transit?:")
        return transit
    else: input("Try again")
    
def destToKm(googleDirections):
    return googleDirections

def kmToMiles(km):
    return 0.62137119*km 

def translateAll(googleDistance, googleMode):
    googleDistance = kmToMiles(googleDistance)
    mode = googleMode
    googleMode = translateMode(mode)
    carbonAPI = f'https://api.triptocarbon.xyz/v1/footprint?activity={googleDistance}&activityType=miles&country=usa&mode={googleMode}'
    response = requests.get(carbonAPI)
    return response.text 
    
# print(translateAll(16.0934, "driving"))