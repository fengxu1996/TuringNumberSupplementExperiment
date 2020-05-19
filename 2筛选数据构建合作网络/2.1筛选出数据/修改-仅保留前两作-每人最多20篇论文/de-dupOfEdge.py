# -*- coding: utf-8 -*-
# !/usr/bin/env python
edge_save = set()
with open(r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\networkEdge.txt", 'r', encoding='utf-8') as f:
    for e in f:
        e = e.strip('\n')
        edge_save.add(e)

with open(r"E:\XF\图灵数补充实验\处理数据集\修改-仅保留前2作-每人最多查5篇论文\networkEdge.txt", 'w', encoding='utf-8') as f:
    for e in edge_save:
        f.write(e+'\n')

