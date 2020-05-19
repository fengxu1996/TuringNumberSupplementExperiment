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
# print(len(iHopSet))

ID_orgs_path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\data1\ID_orgs.txt"
ID_notHaveOrg = set()
with open(ID_orgs_path, 'r', encoding='utf-8') as f:
    for row in f:
        row = row.rstrip('\n').split('\t')
        if len(row) == 1:
            ID_notHaveOrg.add(row[0])
        pass
turingSet = set()
turingPath = r"C:\桌面文件\代码_数据\图灵数补充实验\data\data1\turingID.txt"
with open(turingPath, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.strip('\n').split(',')[0]
        turingSet.add(row)
        pass
    pass

print('turing org miss num:', len(turingSet & ID_notHaveOrg))
for i in range(0, len(iHopSet)):
    print(i+1, 'hop org miss num:', len(iHopSet[i] & ID_notHaveOrg))
