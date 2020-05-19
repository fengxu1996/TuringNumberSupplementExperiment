# -*- coding: utf-8 -*-
# !/usr/bin/env python
from collections import defaultdict
import xlrd
def formatTitle(title):
    ans = ''
    for ch in title:
        if '0' <= ch <= '9' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            ans += ch
        else:
            ans += ' '
    ans = ' '.join(ans.split())
    return ans
# path = r"C:\桌面文件\代码_数据\TuringNumberSupplementExperiment\data\图灵奖获得者.xlsx"
path = r"E:\XF\图灵数补充实验\图灵奖获得者.xlsx"
excel = xlrd.open_workbook(path, encoding_override="utf-8")
# all_sheet = excel.sheets()
# print(all_sheet)
sheet = excel.sheet_by_index(0)
print(sheet.name, sheet.nrows)
# print(sheet.row_values(0))

set_turingPapers = set()
dict_title_turingWinnerName = defaultdict()
for i in range(1, sheet.nrows):
    # print(row)
    row = sheet.row_values(i)
    titles = row[5:]
    for title in titles:
        if title == '':
            continue
        title_format = formatTitle(title.lower())
        set_turingPapers.add(title_format)
        dict_title_turingWinnerName[title_format] = row[2]
        pass

path_dblp = r"D:\Dataset\dblp_v12\dblp.v12.json"
path_out = r"E:\XF\图灵数补充实验\处理数据集\findTuringAwardWinnersSomePapers.txt"
f_writer = open(path_out, 'w', encoding='utf-8')
with open(path_dblp, 'r', encoding='utf-8') as f:
    for row in f:
        row = row.rstrip('\n').lstrip(',')
        if row == '[' or row == ']':
            continue
        row = eval(row)
        if 'title' not in row.keys():
            continue
        title = row['title']
        if 'authors' not in row.keys():
            continue
        authors = row['authors']
        id = row['id']
        title_format = formatTitle(title.lower())
        if title_format in set_turingPapers:
            f_writer.write(str(id)+'\t'+dict_title_turingWinnerName[title_format]+'\t'+title+'\t'+str(authors)+'\n')
            pass
f_writer.close()
