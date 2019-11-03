from request_and_distance import *
import requests

# response = requests.get('https://api.triptocarbon.xyz/v1/footprint?activity=10&activityType=miles&country=usa&mode=taxi')
# print(response.text)


# driving
# walking
# bicycling
# transit
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
        # car = input("What type of car do you drive?:")
        # while car not in carTypes:
        #     print("Try again")
        #     car = input("What type of car do you drive?:")
        car = "anyCar"
        return car
    elif googleMode == "walking":
        return None 
    elif googleMode == "bicycling":
        return None
    elif googleMode == "transit":
        # transit = input("What type of transit?:")
        # while transit not in transitTypes:
        #     print("Try again")
        #     transit = input("What type of transit?:")
        transit = "bus"
        return transit
    else: input("Try again")
    
def MetersToMiles(m):
    return 0.00062137*m

def translateAll(googleMode, googleDistance):
    googleDistance = MetersToMiles(googleDistance)
    mode = googleMode
    googleMode = translateMode(mode)
    carbonAPI = f'https://api.triptocarbon.xyz/v1/footprint?activity={googleDistance}&activityType=miles&country=usa&mode={googleMode}'
    response = requests.get(carbonAPI)
    return response.text

def getCarbon(trip=google.runFunction()):
    carbonPerMode = dict()
    print(trip)
    for key in trip:
        mode = key
        dist = trip[key]
        if dist != 0:
            carbon = translateAll(mode, dist)
            carbonPerMode[mode] = carbon
    return carbonPerMode
 
print(getCarbon())
#{'driving': 1251, 'transit': 0, 'walking': 0, 'bicycling': 0}

#trips = {(origin, destination, googleMode);{(mode1,distance), (mode2, distance)}}

#Carnegie Mellon University
#Piada Italian Street Food 3600 Forbes Avenue
# print(translateAll(16.0934, "driving"))