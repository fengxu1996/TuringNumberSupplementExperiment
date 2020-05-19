# -*- coding: utf-8 -*-
# !/usr/bin/env python
path1 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\country_TNAverage.txt"
path2 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\country_TN_distribution.txt"
path3 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_country_final.txt"
pathOut = r"C:\桌面文件\代码_数据\图灵数补充实验\data\countryFullName_TNAverage.txt"
pathOut1 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\GEOIn_countryFullName_TNAverage.txt"
countrySX_FullName_dict = dict()
with open(path3, 'r', encoding='utf-8') as f:
    for row in f:
        row = row.strip('\n').split('\t')
        if row[2]  not in countrySX_FullName_dict.keys():
            countrySX_FullName_dict[row[2]] = row[1]
    pass

with open(pathOut, 'w', encoding='utf-8') as fOut:
    with open(path1, 'r', encoding='utf-8') as f:
        flag = 0
        for row in f:
            if flag == 0:
                flag = 1
                continue
            row = row.strip('\n').split('\t')
            fOut.write(row[0]+'\t'+countrySX_FullName_dict[row[0]]+'\t'+row[1]+'\n')
            pass
        pass
    pass
with open(pathOut1, 'w', encoding='utf-8') as fOut:
    with open(path1, 'r', encoding='utf-8') as f:
        flag = 0
        for row in f:
            if flag == 0:
                flag = 1
                continue
            row = row.strip('\n').split('\t')
            fOut.write('{name: \''+countrySX_FullName_dict[row[0]]+'\', value: '+row[1]+'},\n')
            pass
        pass
    pass
