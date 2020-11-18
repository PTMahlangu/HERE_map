import requests
from flask import Flask,render_template

URL = "https://geocode.search.hereapi.com/v1/geocode"
location = input("Enter the location here: ") #taking user input
api_key = 'XXXXXXXXXXXXXXXXXXXXXXXX' # Acquire from developer.here.com
PARAMS = {'apikey':api_key,'q':location} 

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
data = r.json()
print(data)

#Acquiring the latitude and longitude from JSON 
# latitude = data['items'][0]['position']['lat']
# print(latitude)
# longitude = data['items'][0]['position']['lng']
# print(longitude)
# city = data['items'][0]['address']['city']
# print(city)
# street = data['items'][0]['address']['street']
# print(street)
# state = data['items'][0]['address']['state']
# print(state)
# county = data['items'][0]['address']['county']
# print(county)

#Flask code 
# app = Flask(__name__)
# @app.route('/')

# def map_func():
# 	return render_template('geocoding_complete.html',apikey=api_key,latitude=latitude,longitude=longitude)#map.html is my HTML file name

# if __name__ == '__main__':
#     app.run(debug = False)
