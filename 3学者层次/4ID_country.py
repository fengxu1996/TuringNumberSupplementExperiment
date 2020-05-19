# -*- coding: utf-8 -*-
# !/usr/bin/env python
import googlemaps
KEY = "AIzaSyCu6kBPjCOnfr2ZpEuPAMp8FPJW4jq6Z_E"
gmaps = googlemaps.Client(key=KEY)

path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_geojson.txt"
pathOut = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_country.txt"

ID_latlng_dict = dict()  # 没有直接的国家信息，保存经纬度，用来反向查询国家
with open(pathOut, 'w', encoding='utf-8') as fOut:
    with open(path, 'r', encoding='utf-8') as f:
        for row in f:
            row = row.rstrip('\n').split('\t')
            ID = row[0]
            if len(row) == 1:
                fOut.write(row[0] + '\n')
            else:
                geo = eval(row[1])
                address_components = geo[0]['address_components']
                country_longName = ''
                country_shortName = ''
                flag = 0
                for ele in address_components:
                    if 'country' in ele['types']:
                        flag = 1
                        country_longName = ele['long_name']
                        country_shortName = ele['short_name']
                        break
                    pass
                if flag == 1:
                    fOut.write(row[0] + '\t' + str(country_longName) + '\t' + str(country_shortName) + '\n')
                else:
                    # fOut.write(row[0] + '\n')
                    # ID_latlng_dict[row[0]] = \
                    lat = geo[0]['geometry']['location']['lat']
                    lng = geo[0]['geometry']['location']['lng']
                    latlng = (lat, lng)
                    flag = 0
                    longName = ''
                    shortName = ''
                    reverse_geocode_result = gmaps.reverse_geocode(latlng)
                    for e in reverse_geocode_result[0]['address_components']:
                        if 'country' in e['types']:
                            flag = 1
                            # print(e['long_name'], e['short_name'])
                            longName = e['long_name']
                            shortName = e['short_name']
                    if flag == 0:
                        fOut.write(row[0] + '\n')
                        print(row[0] + '\t' + 'not countryName')
                    else:
                        fOut.write(row[0]+'\t'+longName+'\t'+shortName+'\n')
                pass
            pass
        pass

