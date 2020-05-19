# -*- coding: utf-8 -*-
# !/usr/bin/env python
import xlrd
import csv
path = r"E:\XF\图灵数补充实验\图灵奖获得者.xlsx"
# path = r"C:\桌面文件\代码_数据\TuringNumberSupplementExperiment\data\图灵奖获得者.xlsx"
excel = xlrd.open_workbook(path, encoding_override="utf-8")
sheet = excel.sheet_by_index(0)
# print(sheet)
# 得到这些图灵奖获得者的id
set_turing_id = set()
one_hop_collaborator_ids = set()  # 要去除第一跳中包含的turing id

for i in range(1, sheet.nrows):
    row = sheet.row_values(i)
    # id = str(row[4])#.split(',')[0]
    # print(id)
    id = str(row[4]).split(',')[0]
    print(id)
    set_turing_id.add(int(id))
    pass

path_dblp = r"D:\Dataset\dblp_v12\dblp.v12.json"

# turing award id ---> 1 hop collaborator
with open(path_dblp, 'r', encoding='utf-8') as f:
    for row in f:
        row = row.rstrip('\n').lstrip(',')
        if row == '[' or row == ']':
            continue
        paper_i = eval(row)
        if 'authors' not in paper_i.keys():
            continue
        authors = paper_i['authors']
        flag = False
        paper_i_ids = []
        for author in authors:
            id_i = author['id']
            paper_i_ids.append(id_i)
            if id_i in set_turing_id:
                flag = True
                pass
            pass
        if flag is True:
            for id in paper_i_ids:
                one_hop_collaborator_ids.add(id)
            pass
        pass
    pass

path_oneHop_collaborator = r"E:\XF\图灵数补充实验\处理数据集\1hop_collabor_IDs.txt"
with open(path_oneHop_collaborator, 'w', encoding='utf-8') as f:
    f.write("oneHopID\n")
    for id in one_hop_collaborator_ids:
        if id not in set_turing_id:
            f.write(str(id) + '\n')
    pass
