# -*- coding: utf-8 -*-
# !/usr/bin/env python
import csv
from collections import defaultdict
def formatTitle(title):
    ans = ''
    for ch in title:
        if '0' <= ch <= '9' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            ans += ch
        else:
            ans += ' '
    ans = ' '.join(ans.split())
    return ans
# title_ = input('title:')
# title_ = formatTitle(title_.lower())
titles = "Who gets acknowledged: Measuring scientific contributions through automatic acknowledgment indexing	Using Information Technology to Transform the Way We Learn	Transforming Health Care Through Information Technology	Transforming Access to Government Information	The revolution yet to happen	A history and evaluation of System R	A Critique of Forrester's Model of an Urban Area	On the Covering and Reduction Problems for Context-Free Grammars	Single pass precedence analysis	During the past year, the President's Information Technology Advisory Committee (PITAC) has focused much of its attention on providing a vision for information technology's role in helping to drive progress in the 21	USING PHOTO-COMPOSER EQUIPNENT FROM SAN JOSE RESEARCH nl SYSTEM (S JRLVM1)"
titles = titles.lower().split('\t')
titles = set(list(map(formatTitle, titles)))
# print(titles)
path_out = r"E:\XF\图灵数补充实验\处理数据集\jamesGray.txt"
outer = open(path_out, 'w', encoding='utf-8')
dblp_path = r"D:\Dataset\dblp_v12\dblp.v12.json"
with open(dblp_path, 'r', encoding='utf-8') as f:
    for row in f:
        row = row.lstrip(',').rstrip('\n')
        if row == '[' or row == ']':  # 第一行或最后一行跳过
            continue
        paper_i = eval(row)
        title = formatTitle(paper_i['title'].lower())
        if title in titles:
            print(str(paper_i['authors']))
            outer.write(str(paper_i['authors'])+'\n')
        pass
    pass
outer.close()
