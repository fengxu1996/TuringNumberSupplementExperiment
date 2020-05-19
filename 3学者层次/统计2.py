# -*- coding: utf-8 -*-
# !/usr/bin/env python
iHopSet = []
pathFormat = r"C:\桌面文件\代码_数据\图灵数补充实验\data\data1\{}hop_collabor_IDs.txt".format
for i in range(1, 8):
    path_i = pathFormat(i)
    hopi = set()
    with open(path_i, 'r', encoding='utf-8') as f:
        flag = 0
        for row in f:
            if flag == 0:
                flag = 1
                continue
            row = row.rstrip('\n')
            hopi.add(row)
            pass
    iHopSet.append(hopi)

turingSet = set()
turingPath = r"C:\桌面文件\代码_数据\图灵数补充实验\data\data1\turingID.txt"
with open(turingPath, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.rstrip('\n').split(',')[0]
        turingSet.add(row)
        pass
    pass
ID_findCountry = set()
ID_country_path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_country.txt"
with open(ID_country_path, 'r', encoding='utf-8') as f:
    for row in f:
        row = row.rstrip('\n').split('\t')
        if len(row) != 1:
            ID_findCountry.add(row[0])
    pass
print(len(ID_findCountry))
fullID = turingSet | iHopSet[0] | iHopSet[1] | iHopSet[2] | iHopSet[3] | iHopSet[4] \
         | iHopSet[5] | iHopSet[6]
print(len(fullID))

notFindCountryID = fullID - ID_findCountry
print('turing org miss num:', len(turingSet & notFindCountryID))

for i in range(0, len(iHopSet)):
    print(i+1, 'hop org miss num:', len(iHopSet[i] & notFindCountryID))

# print('1 hop org miss num:', len(turingSet & notFindCountryID))
# print('2 hop org miss num:', len(turingSet & notFindCountryID))
# print('3 hop org miss num:', len(turingSet & notFindCountryID))
# print('4 hop org miss num:', len(turingSet & notFindCountryID))
# print('5 hop org miss num:', len(turingSet & notFindCountryID))
# print('6 hop org miss num:', len(turingSet & notFindCountryID))
# print('7 hop org miss num:', len(turingSet & notFindCountryID))
print(list(turingSet & notFindCountryID))
# ['2681190977', '2780033398', '2697903471', '2988412133', '2809216397']
# 丹麦    The Kingdom of Denmark  DNK
# 美国    United States   US
# 美国    United States   US
# 美国    United States   US
# 英国    United Kingdom	GB
