# -*- coding: utf-8 -*-
# !/usr/bin/env python

def h_index(citations):
    citations.sort(reverse=True)
    citations.append(0)
    ans = 0
    for i in range(0, len(citations)):
        if citations[i] < i + 1:
            ans = i
            break
    return ans
path = r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\papers.txt"
path_turingID = r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\turingID.txt"
path_i_hop = r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\{}hop_collabor_IDs.txt".format

ID_citationList_dict = dict()
set_authorID = set()
with open(path_turingID, 'r', encoding='utf-8') as f:
    flag = False
    for row in f:
        if flag is False:
            flag = True
            continue
        row = row.strip('\n').split(',')[0]
        set_authorID.add(int(row))
        ID_citationList_dict[int(row)] = []
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
            ID_citationList_dict[int(row)] = []
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
                ID_citationList_dict[author['id']].append(citation)
            pass
        pass
    pass

path_out = r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\ID_hIndex.txt"
with open(path_out, 'w', encoding='utf-8') as fOut:
    for id in set_authorID:
        hindex = h_index(ID_citationList_dict[id])
        fOut.write(str(id)+'\t'+str(hindex)+'\n')
