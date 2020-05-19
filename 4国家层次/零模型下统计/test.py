# -*- coding: utf-8 -*-
# !/usr/bin/env python
# C:\桌面文件\代码_数据\TuringNumberSupplementExperiment\data\zeroModel\ID_hIndex_paperNum_citationSum_zeroModelTN_country.txt
path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\zeroModel\ID_hIndex_paperNum_" \
       r"citationSum_zeroModelTN_country.txt"
path_format = r"C:\桌面文件\代码_数据\图灵数补充实验\data\countrys" \
              r"Scholar\NullModelCountryScholar\{}.txt".format
country_scholars = dict()
with open(path, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.strip('\n').split('\t')
        if row[5] != '':
            if row[5] not in country_scholars.keys():
                country_scholars[row[5]] = []
            country_scholars[row[5]].append(row)
            pass
    pass

for country in country_scholars.keys():
    path_i = path_format(country)
    authorsList = country_scholars[country]
    with open(path_i, 'w', encoding='utf-8') as f:
        for author in authorsList:
            f.write('\t'.join(author)+'\n')
