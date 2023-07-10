import sys
import requests
import json

if len(sys.argv) != 2:
    print('Missing command-line argument! ')
    sys.exit()

try:
    n = float(sys.argv[1])
except ValueError:
    print('Command-line argument is not a number! ')
    sys.exit()

try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.RequestException:
    sys.exit()

try:
    data = json.loads(response.text)
    price = float(data['bpi']['USD']['rate'].replace(',', ''))
except (ValueError, KeyError):
    sys.exit()

total_cost = n*price
print("{:.2f}".format(total_cost))