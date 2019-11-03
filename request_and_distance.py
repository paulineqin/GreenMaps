import requests, json

r = requests.get("https://maps.googleapis.com/maps/api/directions/json?"
+ "origin=Toronto&destination=Montreal"
+ "&key=AIzaSyACBj7THYkOMiWaUcwjfBadeNsEOOuSecg")

headers = r.headers

origin = input("What is your origin?")
mode = input("What is your mode of transportation?")
possibleModes = ["driving", "transit", "walking", "bicycling"]

#print(repr((origin,destination)))
origin2 = ("+".join(origin))

url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin2}&destination=Piada+Italian+Street+Food+3600+Forbes+Avenue&mode={mode}&key=AIzaSyACBj7THYkOMiWaUcwjfBadeNsEOOuSecg"


response = requests.request("GET", url, headers=headers)
#print(response.text)
#print(response.text)

#distance of legs 
def getNumRoutes(directions):
    return len(directions["routes"])

def getNumLegs(directions,routeNum):
    routeNum -=1 #-1 because user will usually input starting from 1
    routes = directions["routes"]
    return len(routes[routeNum]["legs"])

def getLegDistance(directions, routeNum, legNum):
    routeNum -= 1
    legNum -= 1 # -1 because user will usually input starting from 1
    routes = directions["routes"][routeNum]
    legs = routes["legs"][legNum]
    return legs["distance"]["text"]

def getSteps(directions, routeNum, legNum):
    routeNum -=1 
    legNum -=1 
    routes = directions["routes"][routeNum]
    leg = routes["legs"][legNum]
    steps = leg["steps"]
    return steps

def checkTotalStepsDistance(steps, mode):
    total = 0
    mode_to_check = mode.upper()
    for stepIndex in range(len(steps)):
        if (steps[stepIndex]["travel_mode"] == mode_to_check):
            total += steps[stepIndex]["distance"]["value"]
    return total 



def getDistance(routes, routeNum, legNum, stepNum):
    return routes[routeNum]["legs"][legNum]["steps"][stepNum]["distance"]

def calculateDistances(steps): 
    totalDistances = dict()
    for mode in possibleModes: 
        dist = checkTotalStepsDistance(steps,mode)
        totalDistances[mode] = dist
    return totalDistances
    

#legs = routes[0]["legs"]

#firstLeg = legs[0]
#print(getDistance(routes, 0, 0, 10))
#print((routes[0]["legs"][0]["steps"][0]["distance"]))
#print(type(directions["routes"]))
#print(firstLeg.keys())
directions = json.loads(response.text)
steps = getSteps(directions,0,0)
totals = calculateDistances(steps)
print(totals)
#print(json.dumps(directions, indent=4, sort_keys=True))

#print(r.headers)
