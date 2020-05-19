# -*- coding: utf-8 -*-
# !/usr/bin/env python
# https://maps.googleapis.com/maps/api/geocode/json?latlng=32.104637,35.17451399999999&key=AIzaSyCu6kBPjCOnfr2ZpEuPAMp8FPJW4jq6Z_E

# https://maps.googleapis.com/maps/api/geocode/outputFormat?parameters
# https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
# https://maps.googleapis.com/maps/api/geocode/json?latlng=40.1148898,-73.961452&key=YOUR_API_KEY

import googlemaps
from datetime import datetime
import time

KEY = "AIzaSyCu6kBPjCOnfr2ZpEuPAMp8FPJW4jq6Z_E"
# gmaps = googlemaps.Client(key=KEY)
#
# # Geocoding an address
# address = "Carnegie - Mellon University#TAB#"
# geocode_result = gmaps.geocode(address)
# print(geocode_result)
# Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
# print(reverse_geocode_result)
# Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)


def main():
    ID_orgs_path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_orgs.txt"
    outPath = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_geojson.txt"
    gmaps = googlemaps.Client(key=KEY)
    with open(outPath, 'a+', encoding='utf-8') as fOut:
        with open(ID_orgs_path, 'r', encoding='utf-8') as f:
            for row in f:
                row = row.rstrip('\n').split('\t')
                if len(row) == 1:
                    fOut.write(row[0]+'\n')
                else:
                    for i in range(1, len(row)):
                        address = row[i]
                        try:
                            geocode_result = gmaps.geocode(address)
                        except Exception as e:
                            print(e)
                        if geocode_result is None or len(geocode_result) == 0:
                            continue
                        else:
                            fOut.write(row[0] + '\t' + str(geocode_result) + '\n')
                            break
                        pass
                # time.sleep(0.1)
                pass
            pass
        pass
    pass


if __name__ == "__main__":
    main()
    pass



# fOut.write(row[0]+'\t'+
#            str(geocode_result[0]['geometry']['location']['lat']) + ',' +
#            str(geocode_result[0]['geometry']['location']['lng']) + '\t' +
#            str(geocode_result) + '\n'
#            )
