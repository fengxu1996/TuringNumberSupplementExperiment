# -*- coding: utf-8 -*-
# !/usr/bin/env python
path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_geojson.txt"
pathOut = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_latlng.txt"
with open(pathOut, 'w', encoding='utf-8') as fOut:
    with open(path, 'r', encoding='utf-8') as f:
        for row in f:
            row = row.rstrip('\n').split('\t')
            ID = row[0]
            if len(row) == 1:
                fOut.write(row[0] + '\n')
            else:
                geo = eval(row[1])
                lat = geo[0]['geometry']['location']['lat']
                lng = geo[0]['geometry']['location']['lng']
                fOut.write(row[0] + '\t' + str(lat) + ',' + str(lng) + '\n')
                pass
            pass
        pass
