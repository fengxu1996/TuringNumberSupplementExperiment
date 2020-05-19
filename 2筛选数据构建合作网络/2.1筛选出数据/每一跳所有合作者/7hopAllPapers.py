# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
筛选条件为 只要论文的authors id里面包含有turing id和 1 hop id 到 6 hop id 中的一个，就保存该论文。
"""
import xlrd
from collections import defaultdict
path = r"E:\XF\图灵数补充实验\图灵奖获得者.xlsx"
path_dblp = r"D:\Dataset\dblp_v12\dblp.v12.json"
excel = xlrd.open_workbook(path, encoding_override="utf-8")
sheet = excel.sheet_by_index(0)
path_oneHop_collaborator = r"E:\XF\图灵数补充实验\处理数据集\1hop_collabor_IDs.txt"
path_twoHop_collaborator = r"E:\XF\图灵数补充实验\处理数据集\2hop_collabor_IDs.txt"
path_threeHop_collaborator = r"E:\XF\图灵数补充实验\处理数据集\3hop_collabor_IDs.txt"
path_fourHop_collaborator = r"E:\XF\图灵数补充实验\处理数据集\4hop_collabor_IDs.txt"
path_fiveHop_collaborator = r"E:\XF\图灵数补充实验\处理数据集\5hop_collabor_IDs.txt"
path_sixHop_collaborator = r"E:\XF\图灵数补充实验\处理数据集\6hop_collabor_IDs.txt"
path_sevenHop_collaborator = r"E:\XF\图灵数补充实验\处理数据集\7hop_collabor_IDs.txt"

path_7hopAllPapers = r"E:\XF\图灵数补充实验\处理数据集\7hopAllPapers.txt"

collaborEdge_cnt = defaultdict(lambda: 0)
set_turing_1to7HopIDs = set()
# read turing id
for i in range(1, sheet.nrows):
    row = sheet.row_values(i)
    id = str(row[4]).split(',')[0]
    set_turing_1to7HopIDs.add(int(id))
    pass
# read one hop id
with open(path_oneHop_collaborator, 'r', encoding='utf-8') as f:
    flag = False
    for row in f:
        if flag is False:
            flag = True
            continue
        row = row.rstrip('\n')
        set_turing_1to7HopIDs.add(int(row))
    pass
# read two hop id
with open(path_twoHop_collaborator, 'r', encoding='utf-8') as f:
    flag = False
    for row in f:
        if flag is False:
            flag = True
            continue
        row = row.rstrip('\n')
        set_turing_1to7HopIDs.add(int(row))
    pass
# read three hop id
with open(path_threeHop_collaborator, 'r', encoding='utf-8') as f:
    flag = False
    for row in f:
        if flag is False:
            flag = True
            continue
        row = row.rstrip('\n')
        set_turing_1to7HopIDs.add(int(row))
    pass
# read four hop id
with open(path_fourHop_collaborator, 'r', encoding='utf-8') as f:
    flag = False
    for row in f:
        if flag is False:
            flag = True
            continue
        row = row.rstrip('\n')
        set_turing_1to7HopIDs.add(int(row))
    pass
# read five hop id
with open(path_fiveHop_collaborator, 'r', encoding='utf-8') as f:
    flag = False
    for row in f:
        if flag is False:
            flag = True
            continue
        row = row.rstrip('\n')
        set_turing_1to7HopIDs.add(int(row))
    pass
# read six hop id
with open(path_sixHop_collaborator, 'r', encoding='utf-8') as f:
    flag = False
    for row in f:
        if flag is False:
            flag = True
            continue
        row = row.rstrip('\n')
        set_turing_1to7HopIDs.add(int(row))
    pass
# read seven hop id
with open(path_sevenHop_collaborator, 'r', encoding='utf-8') as f:
    flag = False
    for row in f:
        if flag is False:
            flag = True
            continue
        row = row.rstrip('\n')
        set_turing_1to7HopIDs.add(int(row))
    pass
with open(path_7hopAllPapers, 'w', encoding='utf-8') as fOut:
    with open(path_dblp, 'r', encoding='utf-8') as f:
        for row in f:
            row = row.rstrip('\n').lstrip(',')
            if row == '[' or row == ']':
                continue
            paper_i = eval(row)
            if 'authors' not in paper_i.keys():
                continue
            authors = paper_i['authors']
            for author in authors:
                id_i = author['id']
                if id_i in set_turing_1to7HopIDs:
                    fOut.write(row+'\n')
