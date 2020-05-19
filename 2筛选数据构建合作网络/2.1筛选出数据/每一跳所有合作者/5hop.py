# -*- coding: utf-8 -*-
# !/usr/bin/env python
import xlrd
path = r"E:\XF\图灵数补充实验\图灵奖获得者.xlsx"
path_dblp = r"D:\Dataset\dblp_v12\dblp.v12.json"
excel = xlrd.open_workbook(path, encoding_override="utf-8")
sheet = excel.sheet_by_index(0)
set_turing_id = set()  # turing id
one_hop_collaborator_ids = set()  # 1 hop id
two_hop_collaborator_ids = set()  # 2 hop id
three_hop_collaborator_ids = set()  # 3 hop id
four_hop_collaborator_ids = set()  # 4 hop id
five_hop_collaborator_ids = set()  # 5 hop id


path_oneHop_collaborator = r"E:\XF\图灵数补充实验\处理数据集\1hop_collabor_IDs.txt"
path_twoHop_collaborator = r"E:\XF\图灵数补充实验\处理数据集\2hop_collabor_IDs.txt"
path_threeHop_collaborator = r"E:\XF\图灵数补充实验\处理数据集\3hop_collabor_IDs.txt"
path_fourHop_collaborator = r"E:\XF\图灵数补充实验\处理数据集\4hop_collabor_IDs.txt"
path_fiveHop_collaborator = r"E:\XF\图灵数补充实验\处理数据集\5hop_collabor_IDs.txt"


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
# read two hop id
with open(path_twoHop_collaborator, 'r', encoding='utf-8') as f:
    flag = False
    for row in f:
        if flag is False:
            flag = True
            continue
        row = row.rstrip('\n')
        two_hop_collaborator_ids.add(int(row))
    pass
# read three hop id
with open(path_threeHop_collaborator, 'r', encoding='utf-8') as f:
    flag = False
    for row in f:
        if flag is False:
            flag = True
            continue
        row = row.rstrip('\n')
        three_hop_collaborator_ids.add(int(row))
    pass
# read four hop id
with open(path_fourHop_collaborator, 'r', encoding='utf-8') as f:
    flag = False
    for row in f:
        if flag is False:
            flag = True
            continue
        row = row.rstrip('\n')
        four_hop_collaborator_ids.add(int(row))
    pass

# 4 hop ids ---> 5 hop ids
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
            if id_i in four_hop_collaborator_ids:
                flag = True
                pass
            pass
        if flag is True:
            for id in paper_i_ids:
                five_hop_collaborator_ids.add(id)
            pass
        pass
    pass

with open(path_fiveHop_collaborator, 'w', encoding='utf-8') as f:
    f.write("fiveHopID\n")
    for id in five_hop_collaborator_ids:
        if id not in four_hop_collaborator_ids and\
                id not in three_hop_collaborator_ids and\
                id not in two_hop_collaborator_ids and \
                id not in one_hop_collaborator_ids and \
                id not in set_turing_id:
            f.write(str(id)+'\n')
