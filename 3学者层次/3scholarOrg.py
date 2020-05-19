# -*- coding: utf-8 -*-
# !/usr/bin/env python
path = r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\papers.txt"
path_turingID = r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\turingID.txt"
path_i_hop = r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\{}hop_collabor_IDs.txt".format

ID_orgList_dict = dict()
set_authorID = set()
with open(path_turingID, 'r', encoding='utf-8') as f:
    flag = False
    for row in f:
        if flag is False:
            flag = True
            continue
        row = row.strip('\n').split(',')[0]
        set_authorID.add(int(row))
        ID_orgList_dict[int(row)] = []
    pass
for i in range(1, 8):
    path_i = path_i_hop(i)
    with open(path_i, 'r', encoding='utf-8') as f:
        flag = False
        for row in f:
            if flag is False:
                flag = True
                continue
            row = row.strip('\n')
            set_authorID.add(int(row))
            ID_orgList_dict[int(row)] = []
        pass
    pass

with open(path, 'r', encoding='utf-8') as f:
    for row in f:
        row = row.strip('\n')
        paper = eval(row)
        authors = paper['authors']
        for author in authors:
            if author['id'] in set_authorID:
                if 'org' in author.keys():
                    ID_orgList_dict[author['id']].append(author['org'])
            pass
        pass
    pass


path_out = r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\ID_orgs.txt"
with open(path_out, 'w', encoding='utf-8') as fOut:
    for id in set_authorID:
        if len(ID_orgList_dict[id]) != 0:
            fOut.write(str(id) + '\t' + '\t'.join(ID_orgList_dict[id]) + '\n')
        else:
            fOut.write(str(id) + '\n')
