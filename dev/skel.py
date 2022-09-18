import configparser
from urllib import response
import requests
import json

# Read from config.ini and bind the variables
config = configparser.ConfigParser()
config.read('config.ini')
rainUrl = config['dev']['url']
locationName = config['dev']['locationName']
stationID = ''

# Read data from the api
response = requests.get(rainUrl)
if response:
  data = json.loads(response.content)
# Find the station name first
  stations = data['metadata']['stations']
  for station in stations:
    if station['name'] == locationName:
      stationID = station['id']
    # else:
    #   print('Station Name Not Found')
  # print(stationID)

# Find raindata for specific station ID
  readings = data['items'][0]['readings']
  # print(readings)
  for reading in readings:
    if reading['station_id'] == stationID:
      if reading['value'] == 0:
        print('Not Raining')
      else:
        print('Raining')
else:
  print('An error occurr')
