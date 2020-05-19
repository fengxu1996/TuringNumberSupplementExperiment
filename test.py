# -*- coding: utf-8 -*-
# !/usr/bin/env python
# import csv
# path = r"C:\Users\Xu_F\Desktop\Matched_AuthorName_Org_IDs.txt"
# path_out = r"C:\Users\Xu_F\Desktop\ans\Matched_AuthorName_Org_IDs.txt"
# with open(path_out, 'w', encoding='utf-8') as fOut:
#     with open(path, 'r', encoding='utf-8') as f:
#         for line in f:
#             line = line.strip()
#             if line != '':
#                 fOut.write(line+'\n')
#                 pass
#         pass
# def formatTitle(title):
# #     ans = ''
# #     for ch in title:
# #         if '0' <= ch <= '9' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
# #             ans += ch
# #         else:
# #             ans += ' '
# #     ans = ' '.join(ans.split())
# #     return ans
# #
# #
# # # s = ' as .... ....   sf. '
# # # print(formatTitle(s))
# # # s = ' a as   a  '
# # # print(s.split())
# # title = "AS asdfasf .."
# # print(title.lower())
# # for ch in title.lower():
# #     print(ch)

# set_0 = set()
# set_0.add(1)
# set_0.add(2)
# set_0.add(3)
# set_0.add(4)
#
# set_0.add([5,6,7])
# print(list(set_0))
from collections import defaultdict
TN_peopleNum = defaultdict(lambda: 0)
path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_hIndex_paperNum_citationSum_TN_country.txt"
with open(path, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.strip('\n').split('\t')
        TN_peopleNum[row[4]] += 1
        pass
with open(r"C:\桌面文件\代码_数据\图灵数补充实验\data\TN_peopleNum.txt", 'w', encoding='utf-8') as f:
    print(list(TN_peopleNum.keys()))
    f.write("TN\tpeopleNum\n")
    for i in range(0, 8):
        f.write(str(i)+'\t'+str(TN_peopleNum[str(i)])+'\n')
    pass
