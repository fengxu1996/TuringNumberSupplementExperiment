# -*- coding: utf-8 -*-
# !/usr/bin/env python

import xlrd
from collections import defaultdict
path = r"E:\XF\图灵数补充实验\图灵奖获得者.xlsx"
path_dblp = r"D:\Dataset\dblp_v12\dblp.v12.json"
excel = xlrd.open_workbook(path, encoding_override="utf-8")
sheet = excel.sheet_by_index(0)
set_turing_id = set()  # turing id
one_hop_collaborator_ids = set()  # 1 hop id
one_hop_collaborator_ids_FULL = set()  # 1 hop id FULL
two_hop_collaborator_ids = set()  # 2 hop id

path_oneHop_collaborator = r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\1hop_collabor_IDs.txt"
path_oneHop_collaborator_FULL = r"E:\XF\图灵数补充实验\处理数据集\1hop_collabor_IDs.txt"

path_twoHop_collaborator = r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\2hop_collabor_IDs.txt"

# E:\XF\TuringNumberSupplementExperiment\处理数据集\修改-仅保留前几作\2hop_collabor_IDs.txt
oneHopID_Num_dict = defaultdict(lambda: 0)  # 记录每个id已经查了多少篇论文，用来做约束


# read turing id
for i in range(1, sheet.nrows):
    row = sheet.row_values(i)
    id = str(row[4]).split(',')[0]
    set_turing_id.add(int(id))
    pass
# read one hop id
with open(path_oneHop_collaborator, 'r', encoding='utf-8') as f:
    flag = False
    for row in f:
        if flag is False:
            flag = True
            continue
        row = row.rstrip('\n')
        one_hop_collaborator_ids.add(int(row))
    pass
# read one hop id FULL
with open(path_oneHop_collaborator_FULL, 'r', encoding='utf-8') as f:
    flag = False
    for row in f:
        if flag is False:
            flag = True
            continue
        row = row.rstrip('\n')
        one_hop_collaborator_ids_FULL.add(int(row))
    pass
edge_save = set()  # 保存图的边信息
# 1 hop ids ---> 2 hop ids
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
        matchedID = None
        for author in authors:
            id_i = author['id']
            paper_i_ids.append(id_i)
            if id_i in one_hop_collaborator_ids:
                flag = True
                matchedID = id_i
                if oneHopID_Num_dict[id_i] > 20:
                    paperNumLimit = True
                    break
                pass
            pass
        if paperNumLimit is True:
            continue
        oneHopID_Num_dict[matchedID] += 1
        if flag is True:
            cnt = 0
            xxx = []  # 用于构建边
            for id in paper_i_ids:
                if cnt >= 2:
                    break
                two_hop_collaborator_ids.add(id)
                cnt += 1
                xxx.append(id)
                if id != matchedID:  # 上一跳的学者与筛选出的学者间的边
                    xx = sorted([id, matchedID])
                    edge_save.add(str(xx[0]) + '\t' + str(xx[1]))
            for i in range(0, len(xxx) - 1):  # 论文内的作者间的边
                for j in range(i + 1, len(xxx)):
                    xx = sorted([xxx[i], xxx[j]])
                    edge_save.add(str(xx[0]) + '\t' + str(xx[1]))
            pass
        pass
    pass

with open(path_twoHop_collaborator, 'w', encoding='utf-8') as f:
    f.write("twoHopID\n")
    for id in two_hop_collaborator_ids:
        if id not in one_hop_collaborator_ids_FULL and \
                id not in set_turing_id:
            f.write(str(id)+'\n')

with open(r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\networkEdge.txt", 'a+', encoding='utf-8') as f:
    for e in edge_save:
        f.write(e+'\n')
    pass