# -*- coding: utf-8 -*-
# !/usr/bin/env python
import xlrd

path = r"E:\XF\图灵数补充实验\图灵奖获得者.xlsx"
excel = xlrd.open_workbook(path, encoding_override="utf-8")
sheet = excel.sheet_by_index(0)
set_id = set()

path_i_hop = r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-" \
             r"每人最多查5篇论文\{}hop_collabor_IDs.txt".format

dblp_path = r"D:\Dataset\dblp_v12\dblp.v12.json"
for i in range(1, sheet.nrows):
    row = sheet.row_values(i)
    id = str(row[4]).split(',')[0]
    set_id.add(int(id))
    pass

for i in range(1, 8):
    path_i = path_i_hop(i)
    flag = False
    with open(path_i, 'r', encoding='utf-8') as f:
        for row in f:
            if flag is False:
                flag = True
                continue
            row = row.strip('\n')
            set_id.add(int(row))
        pass
    pass

papers_path = r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\papers.txt"
with open(papers_path, 'w', encoding='utf-8') as fOut:
    with open(dblp_path, 'r', encoding='utf-8') as f:
        for row in f:
            row = row.rstrip('\n').lstrip(',')
            if row == '[' or row == ']':
                continue
            paper_i = eval(row)
            if 'authors' not in paper_i.keys():
                continue
            authors = paper_i['authors']
            for author in authors:
                if author['id'] in set_id:
                    fOut.write(row+'\n')
                    break
                pass
        pass
    pass

