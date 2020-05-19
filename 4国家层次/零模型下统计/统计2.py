# -*- coding: utf-8 -*-
# !/usr/bin/env python
path1 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\zeroModel\ID_hIndex_paperNum_" \
          r"citationSum_zeroModelTN_country.txt"
"""Null Model下各个TN 所占人数"""
map_NullTN_peopleNum = dict()
with open(path1, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.strip('\n').split('\t')
        if row[4] not in map_NullTN_peopleNum.keys():
            map_NullTN_peopleNum[row[4]] = 0
        map_NullTN_peopleNum[row[4]] += 1
        pass
    pass
# NullTN_peopleNum_list = [(k, v) for k, v in map_NullTN_peopleNum.items()]
with open(r"C:\桌面文件\代码_数据\图灵数补充实验\data\zeroModel\NullModelTN_peopleNum.txt", 'w', encoding='utf-8') as f:
    f.write("NullModelTN\tpeopleNum\n")
    for k, v in map_NullTN_peopleNum.items():
        f.write(k+'\t'+str(v)+'\n')
"""Null Model下不同国家的TN分布情况"""
NullModel_country_TN_num_dict = dict()  # 国家，TN，人数
with open(path1, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.strip('\n').split('\t')
        if row[5] != '':  # 国家
            if row[5] not in NullModel_country_TN_num_dict.keys():
                NullModel_country_TN_num_dict[row[5]] = {}
                x = ['TN_0', 'TN_1', 'TN_2', 'TN_3', 'TN_4', 'TN_5', 'TN_6', 'TN_7', 'TN_8',
                     'TN_9', 'TN_10', 'TN_11', 'TN_12', 'TN_INF']
                for i in x:
                    NullModel_country_TN_num_dict[row[5]][i] = 0
            # if "TN_"+row[4] not in NullModel_country_TN_num_dict[row[5]].keys():
            #     NullModel_country_TN_num_dict[row[5]]["TN_"+row[4]] = 0
            NullModel_country_TN_num_dict[row[5]]["TN_"+row[4]] += 1
    pass
print(list(NullModel_country_TN_num_dict['CN'].keys()))
with open(r"C:\桌面文件\代码_数据\图灵数补充实验\data\zeroModel\NullModel_country_TN_distribution.txt",
          'w', encoding='utf-8') as f:
    x = ['TN_0', 'TN_1', 'TN_2', 'TN_3', 'TN_4', 'TN_5', 'TN_6', 'TN_7', 'TN_8',
         'TN_9', 'TN_10', 'TN_11', 'TN_12', 'TN_INF']
    f.write("country\t"+'\t'.join(x)+'\n')
    for country in NullModel_country_TN_num_dict.keys():
        xx = []
        for i in x:
            xx.append(NullModel_country_TN_num_dict[country][i])
        xx = list(map(str, xx))
        f.write(country+'\t'+'\t'.join(xx)+'\n')
    pass
