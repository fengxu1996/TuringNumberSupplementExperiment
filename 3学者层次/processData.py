# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
过滤，只保存有国家信息的学者id和该学者的国家
"""
# path_ID_country = r"C:\桌面文件\代码_数据\TuringNumberSupplementExperiment\data\ID_country.txt"
# path_out = r"C:\桌面文件\代码_数据\TuringNumberSupplementExperiment\data\ID_country_final.txt"
# with open(path_out, 'w', encoding='utf-8') as fOut:
#     with open(path_ID_country, 'r', encoding='utf-8') as f:
#         for row in f:
#             row = row.rstrip('\n').split('\t')
#             if len(row) != 1:
#                 fOut.write(row[0] + '\t' + row[1] + '\t' + row[2] + '\n')
#         pass
#     pass

# path_out = r"C:\桌面文件\代码_数据\TuringNumberSupplementExperiment\data\ID_country_final.txt"
# with open(path_out, 'a+', encoding='utf-8') as f:
#     f.write('2681190977'+'\t'+'The Kingdom of Denmark'+'\t'+'DNK'+'\n')
#     f.write('2780033398'+'\t'+'United States'+'\t'+'US'+'\n')
#     f.write('2697903471' + '\t' + 'United States' + '\t' + 'US' + '\n')
#     f.write('2988412133' + '\t' + 'United States' + '\t' + 'US' + '\n')
#     f.write('2809216397' + '\t' + 'United Kingdom' + '\t' + 'GB' + '\n')
#     pass
import pandas as pd

path1 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\data1\ID_hIndex.txt"
path2 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\data1\ID_paperNum_citationSum.txt"
path3 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_country_final.txt"
path_turing = r"C:\桌面文件\代码_数据\图灵数补充实验\data\data1\turingID.txt"

path_root = r"C:\桌面文件\代码_数据\图灵数补充实验\data\data1\{}hop_collabor_IDs.txt".format
ID_hIndexPaperNumCitationNumTN = dict()

for i in range(1, 8):
    path_i = path_root(i)
    with open(path_i, 'r', encoding='utf-8') as f:
        flag = 0
        for row in f:
            if flag == 0:
                flag = 1
                continue
            row = row.rstrip('\n')
            ID_hIndexPaperNumCitationNumTN[row] = dict()
            ID_hIndexPaperNumCitationNumTN[row]['TN'] = str(i)
with open(path_turing, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.rstrip('\n').split(',')[0]
        ID_hIndexPaperNumCitationNumTN[row] = dict()
        ID_hIndexPaperNumCitationNumTN[row]['TN'] = '0'

with open(path1, 'r', encoding='utf-8') as f:
    for row in f:
        row = row.rstrip('\n').split('\t')
        ID_hIndexPaperNumCitationNumTN[row[0]]['hIndex'] = row[1]

with open(path2, 'r', encoding='utf-8') as f:
    for row in f:
        row = row.rstrip('\n').split('\t')
        ID_hIndexPaperNumCitationNumTN[row[0]]['paperNum'] = row[1]
        ID_hIndexPaperNumCitationNumTN[row[0]]['citationSum'] = row[2]

with open(path3, 'r', encoding='utf-8') as f:
    for row in f:
        row = row.rstrip('\n').split('\t')
        ID_hIndexPaperNumCitationNumTN[row[0]]['country'] = row[2]


pathOut = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_hIndex_paperNum_citationSum_TN_country.txt"
with open(pathOut, 'w', encoding='utf-8') as f:
    f.write("ID\thIndex\tpaperNum\tcitationSum\tTN\tcountry\n")
    for e in ID_hIndexPaperNumCitationNumTN.keys():
        ID = e
        hIndex = ID_hIndexPaperNumCitationNumTN[ID]['hIndex']
        paperNum = ID_hIndexPaperNumCitationNumTN[ID]['paperNum']
        citationSum = ID_hIndexPaperNumCitationNumTN[ID]['citationSum']
        TN = ID_hIndexPaperNumCitationNumTN[ID]['TN']
        if 'country' in ID_hIndexPaperNumCitationNumTN[ID].keys():
            country = ID_hIndexPaperNumCitationNumTN[ID]['country']
            f.write(ID+'\t'+hIndex+'\t'+paperNum+'\t'+citationSum+'\t'+TN+'\t'+country+'\n')
        else:
            f.write(ID+'\t'+hIndex+'\t'+paperNum+'\t'+citationSum+'\t'+TN+'\n')
