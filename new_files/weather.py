# api key fromhttps://home.openweathermap.org
# KEY: ed5029ac800b77cfa99178fc07b4bc86

# username and password: kqxtgiftpqlydpryhq@kjkpc kqxtgiftpqlydpryhq@kjkpc.net
import requests
import json
city_name = 'Talking Rock'
state_code = 'GA'
country_code = 'US'
# get api key
API_KEY = ''

with open('api_key.txt', 'r', encoding='utf') as file:
    API_KEY = file.readline()
    print(API_KEY)


response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_KEY}')

# get the lat and long
response_data = json.loads(response.text)
lat = response_data[0]['lat']
lon = response_data[0]['lon']

# get the temp
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}')
response_data = json.loads(response.text)

temp = round(response_data['main']['temp'] * (9/5) - 459.67, 1)
print(temp)
# round(285.44 * (9 / 5) - 459.67, 1)  # Convert Kelvin to Fahrenheit.
#  import requests
# >>> city_name = 'San Francisco'
# >>> state_code = 'CA'
# >>> country_code = 'US'
# >>> API_key = '30ee784a80d81480dab1749d33980112'  # Not a real API key
# >>> response = requests.get(f'https://api.openweathermap.org/geo/1.0/
# direct?q={city_name},{state_code},{country_code}&appid={API_key}')
# >>> response.text  # This is a Python string.
# '[{"name":"San Francisco","local_names":{"id":"San Francisco",
# --snip--
# ,"lat":37.7790262,"lon":-122.419906,"country":"US","state":"California"}]'
# >>> import json
# >>> response_data = json.loads(response.text)
# >>> response_data  # This is a Python data structure.
# [{"name":"San Francisco","local_names":{"id":"San Francisco",
# --snip--
# ,"lat":37.7790262,"lon":-122.419906,"country":"US","state":"California"}]