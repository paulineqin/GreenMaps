import requests, json

r = requests.get("https://maps.googleapis.com/maps/api/directions/json?"
+ "origin=Toronto&destination=Montreal"
+ "&key=AIzaSyACBj7THYkOMiWaUcwjfBadeNsEOOuSecg")

headers = r.headers
class GoogleDirections(object):
    def askOriginTransportation(self):
        origin = input("What is your origin?")
        destination0 = input("What is your destination?")
        destination = ("+".join(destination0))
        mode = input("What is your mode of transportation?")
        
        #print(repr((origin,destination)))
        origin2 = ("+".join(origin))
        
        url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin2}&destination={destination}&mode={mode}&key=AIzaSyACBj7THYkOMiWaUcwjfBadeNsEOOuSecg"
        return url 
        
    def getPossibleModes(self):
        possibleModes = ["driving", "transit", "walking", "bicycling"]
        return possibleModes
        
    def getResponse(self, url):
        response = requests.request("GET", url, headers=headers)
        return response 
    
    def getDirections(self, response):
        directions = json.loads(response.text)
        return directions 
        
    #print(response.text)
    #print(response.text)
    
    #distance of legs 
    def getNumRoutes(self, directions):
        return len(directions["routes"])
    
    def getNumLegs(self, directions, routeNum):
        routeNum -=1 #-1 because user will usually input starting from 1
        routes = directions["routes"]
        return len(routes[routeNum]["legs"])
    
    def getLegDistance(self, directions, routeNum, legNum):
        routeNum -= 1
        legNum -= 1 # -1 because user will usually input starting from 1
        routes = directions["routes"][routeNum]
        legs = routes["legs"][legNum]
        return legs["distance"]["text"]
    
    def getSteps(self, directions, routeNum, legNum):
        routeNum -=1 
        legNum -=1 
        routes = directions["routes"][routeNum]
        leg = routes["legs"][legNum]
        steps = leg["steps"]
        return steps
    
    def checkTotalStepsDistance(self, steps, mode):
        total = 0
        mode_to_check = mode.upper()
        for stepIndex in range(len(steps)):
            if (steps[stepIndex]["travel_mode"] == mode_to_check):
                total += steps[stepIndex]["distance"]["value"]
        return total 
    
    def getDistance(self, routes, routeNum, legNum, stepNum):
        return routes[routeNum]["legs"][legNum]["steps"][stepNum]["distance"]
    
    def calculateDistances(self, steps,possibleModes): 
        totalDistances = dict()
        for mode in possibleModes: 
            dist = self.checkTotalStepsDistance(steps,mode)
            totalDistances[mode] = dist
        return totalDistances
    
    def runFunction(self):
        actual_url = self.askOriginTransportation()
        possibleModes = self.getPossibleModes()
        response = self.getResponse(actual_url)
        directions = self.getDirections(response)
        steps = self.getSteps(directions,0,0)
        totals = self.calculateDistances(steps, possibleModes)
        return totals 

google = GoogleDirections()

