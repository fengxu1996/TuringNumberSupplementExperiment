# -*- coding: utf-8 -*-
# !/usr/bin/env python
# path = r"E:\XF\TuringNumberSupplementExperiment\处理数据集\修改-仅保留前2作-每人最多查5篇论文\ID_orgs.txt"
# cnt1 = 0
# cnt2 = 0
# with open(path, 'r', encoding='utf-8') as f:
#     for row in f:
#         row = row.strip('\n').split('\t')
#         if len(row) == 1:
#             cnt1 += 1
#         cnt2 += 1
#         pass
#     pass
# print('all:',cnt2, 'missOrg:', cnt1)
# # all: 53531 missOrg: 5221
path1 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_orgs.txt"
path2 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_geojson.txt"

ID_all = set()
ID_mapORG = dict()
with open(path1, 'r', encoding='utf-8') as f:
    for row in f:
        row = row.rstrip('\n').split('\t')
        ID_all.add(row[0])
        ID_mapORG[row[0]] = []
        for i in range(1, len(row)):
            ID_mapORG[row[0]].append(row[i])
ID_geo = set()
ID_mapGEO = dict()
with open(path2, 'r', encoding='utf-8') as f:
    for row in f:
        row = row.rstrip('\n').split('\t')
        ID_geo.add(row[0])
        if len(row)!=1:
            ID_mapGEO[row[0]] = row[1]

ID_missed = ID_all - ID_geo
path_checkMissedID = r"C:\桌面文件\代码_数据\图灵数补充实验\data\checkMissedID_ORG.txt"
with open(path_checkMissedID, 'w', encoding='utf-8') as f:
    for idMiss in ID_missed:
        # print(idMiss, ID_mapORG[idMiss])
        f.write(idMiss+'\t'+str(ID_mapORG[idMiss])+'\n')
    pass

