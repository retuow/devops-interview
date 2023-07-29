#!/usr/bin/python3

from datetime import datetime
from urllib import request
import json

if __name__ == '__main__':
    lat = 50.930581
    lon = 5.780691
    response = request.urlopen(f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}')
    if response.status != 200:
        raise Exception('Unable to retrieve sunrise/sunset data')
    data = json.loads(response.read().decode('utf-8'))
    if data['status'] != 'OK':
        raise Exception('Bad request sent to API')
    sunrise = datetime.strptime(data['results']['sunrise'], '%I:%M:%S %p').time()
    sunset = datetime.strptime(data['results']['sunset'], '%I:%M:%S %p').time()
    now = datetime.utcnow().time()
    print('OFF') if sunrise < now < sunset else print('ON')
