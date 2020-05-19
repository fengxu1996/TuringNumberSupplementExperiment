# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
检查我们的数据集中（name，org）会不会重复，重复多少
"""
import csv
path = r"C:\桌面文件\珍贵的数据\图灵数据集\图灵数据集\原始数据\处理前数据\2.学者列表.csv"
authors_list = []
with open(path, 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == 'id':
            continue
        id = int(row[1])
        name = row[2]
        org = row[3]
        authors_list.append((name, org))
        pass
    pass

print(len(authors_list))

set_authors = set()
for x in authors_list:
    set_authors.add(x)
print(len(set_authors))
