# -*- coding: utf-8 -*-
# !/usr/bin/env python
import xlrd
path = r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\papers.txt"
path_turingID = r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\turingID.txt"
path_i_hop = r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\{}hop_collabor_IDs.txt".format

ID_paperNum_dict = dict()
ID_citationSum_dict = dict()
set_authorID = set()
with open(path_turingID, 'r', encoding='utf-8') as f:
    flag = False
    for row in f:
        if flag is False:
            flag = True
            continue
        row = row.strip('\n').split(',')[0]
        set_authorID.add(int(row))
        ID_citationSum_dict[int(row)] = 0
        ID_paperNum_dict[int(row)] = 0
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
            ID_citationSum_dict[int(row)] = 0
            ID_paperNum_dict[int(row)] = 0
        pass
    pass

with open(path, 'r', encoding='utf-8') as f:
    for row in f:
        row = row.strip('\n')
        paper = eval(row)
        authors = paper['authors']
        citation = paper['n_citation']
        for author in authors:
            if author['id'] in set_authorID:
                ID_paperNum_dict[author['id']] += 1
                ID_citationSum_dict[author['id']] += citation
            pass
        pass
    pass
path_out = r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\ID_paperNum_citationSum.txt"
with open(path_out, 'w', encoding='utf-8') as fOut:
    for id in set_authorID:
        fOut.write(str(id)+'\t'+str(ID_paperNum_dict[id])+'\t'+str(ID_citationSum_dict[id])+'\n')
