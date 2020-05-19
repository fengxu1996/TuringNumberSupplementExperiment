# -*- coding: utf-8 -*-
# !/usr/bin/env python
import googlemaps
from datetime import datetime
import time

KEY = "AIzaSyCu6kBPjCOnfr2ZpEuPAMp8FPJW4jq6Z_E"
gmaps = googlemaps.Client(key=KEY)

# Geocoding an address
address = "Carnegie - Mellon University#TAB#"
# geocode_result = gmaps.geocode(address)
# print(geocode_result)
# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((37.8736514,-122.2577944))
print(reverse_geocode_result)
print(reverse_geocode_result[0]['address_components'])
for e in reverse_geocode_result[0]['address_components']:
    if 'country' in e['types']:
        print(e['long_name'], e['short_name'])

# Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
