# -*- coding: utf-8 -*-
# !/usr/bin/env python
import json
import csv
from collections import defaultdict
# dblp_path = r"D:\Dataset\dblp_v12\dblp.v12.json"
# paper_path = r"E:\XF\TuringNumberSupplementExperiment\图灵数据集\原始数据\处理前数据\1.论文列表.csv"
paper_path = r"C:\桌面文件\珍贵的数据\图灵数据集\图灵数据集\原始数据\处理前数据\1.论文列表.csv"
# author_path = r"E:\XF\TuringNumberSupplementExperiment\图灵数据集\原始数据\处理前数据\2.学者列表.csv"
author_path = r"C:\桌面文件\珍贵的数据\图灵数据集\图灵数据集\原始数据\处理前数据\2.学者列表.csv"
# # r"E:\XF\TuringNumberSupplementExperiment\图灵数据集\原始数据\处理前数据\3.学者到图灵奖获得者的路径列表.csv"

with open(paper_path, 'r', encoding='utf-8', newline='') as f:
    pass

with open(author_path, 'r', encoding='utf-8', newline='') as f:
    pass




# # 读出学者列表
# # set_id = set()
# # set_id_name_affiliation = set()
# set_name_affiliation = set()
# # map_id_name_affiliation = dict()  # key: id, value: [name, org] 为了跟数据集中的相同id的作者做对照，检查是不是一样的
# map_name_org__id = defaultdict(lambda: set())  # key: (name, org), value: id   保存同一个(name，org)下的所有id，最后输出文件保存
# with open(author_path, 'r', encoding='utf-8', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         if row[1] == 'id':
#             continue
#         id = int(row[1])
#         name = row[2].lstrip('\'').rstrip('\'')
#         affiliation = row[3]
#         # print(type(name), name, type(affiliation), affiliation)
#         set_name_affiliation.add((name, affiliation))
#         # map_id_name_affiliation[id] = (name, affiliation)
#         print(affiliation)
#
# # with open(dblp_path, 'r', encoding='utf-8') as f:
# #     for row in f:
# #         row = row.lstrip(',').rstrip('\n')
# #         if row == '[' or row == ']':  # 第一行或最后一行跳过
# #             continue
# #         paper_i= eval(row)
# #         id = paper_i['id']
# #         if 'authors' not in paper_i.keys():
# #             continue
# #         authors = paper_i['authors']
# #         for author in authors:
# #             if 'org' in author.keys():
# #                 if (author['name'], author['org']) in set_name_affiliation:
# #                     # print(author)
# #                     map_name_org__id[(author['name'], author['org'])].add(author['id'])
# #             else:
# #                 if (author['name'], '') in set_name_affiliation:
# #                     # print(author)
# #                     map_name_org__id[(author['name'], '')].add(author['id'])
# #         pass
# #     pass
# # print(len(map_name_org__id))
# # tolCnt = 0
# # multiCnt = 0
# # path_out = r"E:\XF\TuringNumberSupplementExperiment\处理数据集\Matched_AuthorName_Org_IDs.txt"
# # with open(path_out, 'w', encoding='utf-8', newline='') as f:
# #     writer = csv.writer(f, delimiter='\t')
# #     writer.writerow(['name', 'org', 'id'])
# #     for e in map_name_org__id.keys():
# #         writer.writerow([e[0], e[1], ','.join(list(map(str, list(map_name_org__id[e]))))])
# #         tolCnt += 1
# #         if len(map_name_org__id[e]) > 1:
# #             multiCnt += 1
# #         pass
# #     pass
# # print('tolCnt:', tolCnt, 'multiCnt:', multiCnt)
