import requests

API_MAIN = 'https://www.metaweather.com/'
API_LOCATION = '/api/location/search/?query='
API_WEATHER = '/api/location/'
API_LOCATION_DAY = '/api/location/(woeid)/'

def fetch_location(place_name):
    return requests.get(API_MAIN + API_LOCATION + place_name).json()

def fetch_weather(woeid):
    return requests.get(API_MAIN + API_WEATHER + str(woeid)).json()

place_name = input('Where are you on Earth')
location = fetch_location(place_name)
woeid = location[0]['woeid']
print(woeid)
weather = fetch_weather(woeid)
# print(weather['consolidated_weather'][0]['created'])

for date in weather['consolidated_weather']:
    wind_direction = date['wind_direction_compass']
    wind_speed = int(date['wind_speed'])*1.60
    current_date = date['applicable_date']
    print(current_date)
    
    
