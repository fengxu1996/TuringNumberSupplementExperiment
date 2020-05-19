# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
第一跳不做筛选，保留所有人，因为人数比较少，共5千多人
"""

import xlrd
import csv
from collections import defaultdict
path = r"E:\XF\图灵数补充实验\图灵奖获得者.xlsx"
# path = r"C:\桌面文件\代码_数据\TuringNumberSupplementExperiment\data\图灵奖获得者.xlsx"
excel = xlrd.open_workbook(path, encoding_override="utf-8")
sheet = excel.sheet_by_index(0)
# print(sheet)
# 得到这些图灵奖获得者的id
set_turing_id = set()
one_hop_collaborator_ids = set()  # 要去除第一跳中包含的turing id

turingID_Num_dict = defaultdict(lambda: 0)  # 记录每个id已经查了多少篇论文，用来做约束


for i in range(1, sheet.nrows):
    row = sheet.row_values(i)
    # id = str(row[4])#.split(',')[0]
    # print(id)
    id = str(row[4]).split(',')[0]
    # print(id)
    set_turing_id.add(int(id))
    pass
edge_save = set()  # 保存图的边信息
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
        paperNumLimit = False  # 标记是否超过论文数限制
        paper_i_ids = []
        matchedID = None  # 用于记录连接到的上层的节点
        for author in authors:
            id_i = author['id']
            paper_i_ids.append(id_i)
            if id_i in set_turing_id:
                flag = True
                matchedID = id_i
                if turingID_Num_dict[id_i] > 20:  # 查到的该图灵获得者的论文数有没有超过20篇
                    paperNumLimit = True
                    break
                pass
            pass
        if paperNumLimit is True:  # 因为该学者已经查了超过20篇了，跳过这个学者
            continue
        turingID_Num_dict[matchedID] += 1
        if flag is True:
            cnt = 0
            xxx = []  # 用于构建边
            for id in paper_i_ids:
                if cnt >= 2:  # 只保留下这个论文的前两作
                    break
                one_hop_collaborator_ids.add(id)
                cnt += 1
                xxx.append(id)
                if id != matchedID:  # 上一跳的学者与筛选出的学者间的边
                    xx = sorted([id, matchedID])
                    edge_save.add(str(xx[0])+'\t'+str(xx[1]))
            for i in range(0, len(xxx)-1):  # 论文内的作者间的边
                for j in range(i+1, len(xxx)):
                    xx = sorted([xxx[i], xxx[j]])
                    edge_save.add(str(xx[0]) + '\t' + str(xx[1]))
                    pass
                pass
            pass
        pass
    pass

path_oneHop_collaborator = r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\1hop_collabor_IDs.txt"
with open(path_oneHop_collaborator, 'w', encoding='utf-8') as f:
    f.write("oneHopID\n")
    for id in one_hop_collaborator_ids:
        if id not in set_turing_id:
            f.write(str(id) + '\n')
    pass

with open(r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\networkEdge.txt", 'a+', encoding='utf-8') as f:
    for e in edge_save:
        f.write(e+'\n')
    pass
