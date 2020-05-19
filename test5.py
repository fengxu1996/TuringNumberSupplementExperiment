# -*- coding: utf-8 -*-
# !/usr/bin/env python
path1 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\zeroModel\NullModel_country_aveTN.txt"
path2 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_country_final.txt"
sx_fullName = dict()
with open(path2, 'r', encoding='utf-8') as f:
    for row in f:
        row = row.strip('\n').split('\t')
        if row[2] not in sx_fullName.keys():
            sx_fullName[row[2]] = row[1]
            pass
    pass
pathOut = r"C:\桌面文件\代码_数据\图灵数补充实验\data\zeroModel\GEOInput_" \
          r"NullModel_countryFullName_aveTN.txt"
# NullModel_countrySX_aveTN = dict()
with open(pathOut, 'w', encoding='utf-8') as fOut:
    with open(path1, 'r', encoding='utf-8') as f:
        flag = 1
        for row in f:
            if flag == 1:
                flag = 0
                continue
            row = row.strip('\n').split('\t')
            fOut.write("{name: "+"\'"+sx_fullName[row[0]]+"\', value: "+row[1]+"},\n")
        pass
    pass
