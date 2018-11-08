import requests
import argparse
import datetime
import time

parser = argparse.ArgumentParser(description='Change theme based on sunset and sunrise times.')

parser.add_argument('-lat', '--latitude', help='Latitude', required=True)
parser.add_argument('-lng', '--longitute', help='Longitude', required=True)
args = parser.parse_args()

url = "https://api.sunrise-sunset.org/json?lat=" + args.latitude + "&lng=" + args.longitute

r  = requests.get(url)

data = r.json()

now = datetime.datetime.now().time()

sunset = datetime.datetime.strptime(data['results']['sunset'], "%I:%M:%S %p").time()

if now < sunset:
    print 'Its not sunset'
else:
    print 'Its sunset'
