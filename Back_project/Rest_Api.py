from flask import Flask
from flask_restful import Api, Resource
import Prototype_Wop
import json

app = Flask(__name__)
api = Api(app)
# Getting data from the json file
availablePlacesFile = open('availablePlaces.json', 'r')
dataFromAvailablePlacesFile = json.load(availablePlacesFile)
responseFile = open('../Project_123/response.json')


class WopApi(Resource):

    def post(self, UserChoise_State, UserChoise_City, UserChoise_Floor, UserChoise_Storage, UserChoise_Size,
             UserChoise_Price):

        filteredPlaces = {"filteredPlaces": []}
        response = {"Very Good places": [], "Good places": []}

        filteredPlaces = self.MakeFileUserFilter(UserChoise_State, UserChoise_City, UserChoise_Size, UserChoise_Price,
                                                 UserChoise_Storage,
                                                 UserChoise_Floor, filteredPlaces)

        response = self.MakeFileResponse(filteredPlaces, response)

        return response

    # filter according the user choice
    def MakeFileUserFilter(self, UserChoise_State, UserChoise_City, UserChoise_Size, UserChoise_Price,
                           UserChoise_Storage,
                           UserChoise_Floor, filteredPlaces):

        for place in dataFromAvailablePlacesFile["available_places"]:
            # should be more parameter, according to the front filter
            if place["State"] == UserChoise_State and place["City"] == UserChoise_City and place[
                "area"] <= UserChoise_Size and place["storage"] == UserChoise_Storage and place[
                "floor"] == UserChoise_Floor:
                if place["price"] <= UserChoise_Price:
                    # print(place["price"])
                    filteredPlaces["filteredPlaces"].append(place)
        return filteredPlaces

    # checking if the places matching to the user, will return
    def MakeFileResponse(self, filteredPlaces, response):
        for place in filteredPlaces["filteredPlaces"]:
            areaCategory = 0
            Storage = 0
            publicTransport = 0
            publicParking = 0

            if 50 <= place["area category"] <= 100:
                areaCategory = 1
            else:
                areaCategory = 2
            if place["storage"] == "yes":
                Storage = 1
            if place["Public Transport"] == "yes":
                Storage = 1
            if place["Public parking"] == "yes":
                Storage = 1
                # sent the places to the tree --> return 0 for bad place,1 for good place,2 for very good place
            clasification = Prototype_Wop.DecisionTree(areaCategory, place["floor"], Storage, publicTransport,
                                                       publicParking)
            if clasification[0] == 1:
                response["Good places"].append(place)
            if clasification[0] == 2:
                response["Very Good places"].append(place)

        return response


# the API
api.add_resource(WopApi,
                 "/WopApi/<string:UserChoise_State>/<string:UserChoise_City>/<int:UserChoise_Floor>/<string"
                 ":UserChoise_Storage>/<int:UserChoise_Size>/<int:UserChoise_Price>")
# api example:
# http://127.0.0.1:5000/WopApi/Israel/Beer Sheva/0/yes/80/8000

if __name__ == "__main__":
    app.run(debug=True)

availablePlacesFile.close()
