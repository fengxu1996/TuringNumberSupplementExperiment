# -*- coding: utf-8 -*-
# !/usr/bin/env python
path1 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\zeroModel\zeroMode_IDTN.txt"
path2 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_hIndex_paperNum_citationSum_TN_country.txt"

map_ID_hIndex_paperNum_citationSum_zeroModelTN_country = {}
with open(path1, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.strip('\n').split('\t')
        map_ID_hIndex_paperNum_citationSum_zeroModelTN_country[row[0]] = {}
        map_ID_hIndex_paperNum_citationSum_zeroModelTN_country[row[0]]['zeroModelTN'] = row[1]

with open(path2, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.strip('\n').split('\t')
        map_ID_hIndex_paperNum_citationSum_zeroModelTN_country[row[0]]['hIndex'] = row[1]
        map_ID_hIndex_paperNum_citationSum_zeroModelTN_country[row[0]]['paperNum'] = row[2]
        map_ID_hIndex_paperNum_citationSum_zeroModelTN_country[row[0]]['citationSum'] = row[3]
        if len(row) == 6:
            map_ID_hIndex_paperNum_citationSum_zeroModelTN_country[row[0]]['country'] = row[5]
        else:
            map_ID_hIndex_paperNum_citationSum_zeroModelTN_country[row[0]]['country'] = ''
    pass

pathOut = r"C:\桌面文件\代码_数据\图灵数补充实验\data\zeroModel\ID_hIndex_paperNum_" \
          r"citationSum_zeroModelTN_country.txt"
with open(pathOut, 'w', encoding='utf-8') as f:
    f.write("ID\thIndex\tpaperNum\tcitationSum\tzeroModelTN\tcountry\n")
    for key in map_ID_hIndex_paperNum_citationSum_zeroModelTN_country.keys():
        hIndex = map_ID_hIndex_paperNum_citationSum_zeroModelTN_country[key]['hIndex']
        paperNum = map_ID_hIndex_paperNum_citationSum_zeroModelTN_country[key]['paperNum']
        citationSum = map_ID_hIndex_paperNum_citationSum_zeroModelTN_country[key]['citationSum']
        zeroModelTN = map_ID_hIndex_paperNum_citationSum_zeroModelTN_country[key]['zeroModelTN']
        country = map_ID_hIndex_paperNum_citationSum_zeroModelTN_country[key]['country']
        x = [key, hIndex, paperNum, citationSum, zeroModelTN, country]
        f.write('\t'.join(x)+'\n')
