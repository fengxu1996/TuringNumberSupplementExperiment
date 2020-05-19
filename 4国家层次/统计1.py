# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_hIndex_paperNum_citationSum_TN_country.txt"
# data = pd.read_csv(path, sep='\t', header=0,
#                    dtype={'ID': str, 'hIndex': int, 'paperNum': int,
#                           'citationSum': int, 'TN': int, 'country': str})
country_scholars_dict = dict()
with open(path, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.rstrip('\n').split('\t')
        if len(row) == 6:
            if row[5] not in country_scholars_dict.keys():
                country_scholars_dict[row[5]] = []
            country_scholars_dict[row[5]].append(row)


country_peopleNum_list = list()
for key in country_scholars_dict.keys():
    path_i = r"C:\桌面文件\代码_数据\图灵数补充实验\data\countrysScholar" + "\\{}.txt".format(key)
    # print(key, len(country_scholars_dict[key]))
    country_peopleNum_list.append((key, len(country_scholars_dict[key])))
    with open(path_i, 'w', encoding='utf-8') as f:
        for e in country_scholars_dict[key]:
            f.write('\t'.join(e) + '\n')
        pass

country_peopleNum_list = sorted(country_peopleNum_list, key=lambda x: x[1], reverse=True)
print(country_peopleNum_list)
"""各个国家的人数"""
with open(r"C:\桌面文件\代码_数据\图灵数补充实验\data\country_peopleNum.txt", 'w', encoding='utf-8') as f:
    for x in country_peopleNum_list:
        f.write(x[0] + '\t' + str(x[1]) + '\n')

"""每个国家的TN的分布情况"""
country_TN_peopleNum_dict = dict()  # key: country, value: {key: TN, value: peopleNum}
for key in country_scholars_dict.keys():
    authorList = country_scholars_dict[key]
    country_TN_peopleNum_dict[key] = \
        {'TN0': 0, 'TN1': 0, 'TN2': 0, 'TN3': 0, 'TN4': 0, 'TN5': 0, 'TN6': 0, 'TN7': 0}
    for author in authorList:
        if author[4] == '0':
            country_TN_peopleNum_dict[key]['TN0'] += 1
        elif author[4] == '1':
            country_TN_peopleNum_dict[key]['TN1'] += 1
        elif author[4] == '2':
            country_TN_peopleNum_dict[key]['TN2'] += 1
        elif author[4] == '3':
            country_TN_peopleNum_dict[key]['TN3'] += 1
        elif author[4] == '4':
            country_TN_peopleNum_dict[key]['TN4'] += 1
        elif author[4] == '5':
            country_TN_peopleNum_dict[key]['TN5'] += 1
        elif author[4] == '6':
            country_TN_peopleNum_dict[key]['TN6'] += 1
        elif author[4] == '7':
            country_TN_peopleNum_dict[key]['TN7'] += 1
    pass
with open(r"C:\桌面文件\代码_数据\图灵数补充实验\data\country_TN_distribution.txt", 'w', encoding='utf-8') as f:
    f.write("country\tTN0\tTN1\tTN2\tTN3\tTN4\tTN5\tTN6\tTN7\n")
    countries = [e[0] for e in country_peopleNum_list]
    for c in countries:
        x = [
            country_TN_peopleNum_dict[c]['TN0'],
            country_TN_peopleNum_dict[c]['TN1'],
            country_TN_peopleNum_dict[c]['TN2'],
            country_TN_peopleNum_dict[c]['TN3'],
            country_TN_peopleNum_dict[c]['TN4'],
            country_TN_peopleNum_dict[c]['TN5'],
            country_TN_peopleNum_dict[c]['TN6'],
            country_TN_peopleNum_dict[c]['TN7']
        ]
        x = list(map(str, x))
        f.write(c+'\t'+'\t'.join(x)+'\n')
    pass
"""productivity 各国家的 论文总数、人均论文数"""
"""impact 各国家的 引用总数、人均引用数、hIndex总和、人均hIndex"""
country_paperNumTotal_citationTotal_hIndexTotal_dict = dict()
country_paperNumAve_citationAve_hIndexAve_dict = dict()
for key in country_scholars_dict.keys():
    authorList = country_scholars_dict[key]
    authorNum = len(authorList)
    hIndexSum = 0
    paperNumSum = 0
    citationSum = 0
    for author in authorList:
        hIndexSum += int(author[1])
        paperNumSum += int(author[2])
        citationSum += int(author[3])
    country_paperNumTotal_citationTotal_hIndexTotal_dict[key] = {}
    country_paperNumTotal_citationTotal_hIndexTotal_dict[key]['hIndexTotal'] = hIndexSum
    country_paperNumTotal_citationTotal_hIndexTotal_dict[key]['paperNumTotal'] = paperNumSum
    country_paperNumTotal_citationTotal_hIndexTotal_dict[key]['citationTotal'] = citationSum
    country_paperNumAve_citationAve_hIndexAve_dict[key] = {}
    country_paperNumAve_citationAve_hIndexAve_dict[key]['hIndexAve'] = hIndexSum / authorNum
    country_paperNumAve_citationAve_hIndexAve_dict[key]['paperNumAve'] = paperNumSum / authorNum
    country_paperNumAve_citationAve_hIndexAve_dict[key]['citationAve'] = citationSum / authorNum
with open(r"C:\桌面文件\代码_数据\图灵数补充实验\data\country_hIndex_paperNum_citation_Total.txt", 'w',
          encoding='utf-8') as f:
    countries = [e[0] for e in country_peopleNum_list]
    f.write("country\thIndexTotal\tpaperNumTotal\tcitationTotal\n")
    for c in countries:
        x = [
            country_paperNumTotal_citationTotal_hIndexTotal_dict[c]['hIndexTotal'],
            country_paperNumTotal_citationTotal_hIndexTotal_dict[c]['paperNumTotal'],
            country_paperNumTotal_citationTotal_hIndexTotal_dict[c]['citationTotal']
        ]
        x = list(map(str, x))
        f.write(c+'\t'+'\t'.join(x)+'\n')
        pass
    pass
with open(r"C:\桌面文件\代码_数据\图灵数补充实验\data\country_hIndex_paperNum_citation_Ave.txt", 'w',
          encoding='utf-8') as f:
    countries = [e[0] for e in country_peopleNum_list]
    f.write("country\thIndexAve\tpaperNumAve\tcitationAve\n")
    for c in countries:
        x = [
            country_paperNumAve_citationAve_hIndexAve_dict[c]['hIndexAve'],
            country_paperNumAve_citationAve_hIndexAve_dict[c]['paperNumAve'],
            country_paperNumAve_citationAve_hIndexAve_dict[c]['citationAve']
        ]
        x = list(map(str, x))
        f.write(c+'\t'+'\t'.join(x)+'\n')
        pass
    pass

print([e[0] for e in country_peopleNum_list])

