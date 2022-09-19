# import main Flask class and request object
from cgitb import reset
import requests
import json
import os
from datetime import date
import functools
from flask import (
    Blueprint
)
# variables from the env
# app = create_app()
rainUrl = os.getenv('rainUrl', default='https://api.data.gov.sg/v1/environment/rainfall')
locationName = os.getenv('locationName', default='Marina Gardens Drive')


# init blueprint
bp = Blueprint('default', __name__, url_prefix='/')

# default route
@bp.route('/')
def detectRaining():
    data = getData()
    stationID = getStation(data)
    finalResult = getRaindata(stationID, data)
    print(f"{date.today()} App able access API {rainUrl}")
    return finalResult
    # return 'Query String Example'


def getData():
  # Read data from the api
  response = requests.get(rainUrl)
  if response:
    data = json.loads(response.content)
    return data

def getStation(data):
  # Find the station id based on the name
    stations = data['metadata']['stations']
    for station in stations:
      if station['name'] == locationName:
        stationID = station['id']
        return stationID

def getRaindata(stationID, data):
  # Find raindata for specific station ID
    readings = data['items'][0]['readings']
    timeStamp = data['items'][0]['timestamp'].split('T')[1].split('+')[0]

    # print(readings)
    for reading in readings:
      if reading['station_id'] == stationID:
        if reading['value'] == 0:
          result = f"{locationName}, {timeStamp}, {reading['value']}mm, Not Raining"
        else:
          result = f"{locationName}, {timeStamp}, {reading['value']}mm, Raining"
        return result
# Location, Time, Rainfall Amount, Raining/Not Raining
