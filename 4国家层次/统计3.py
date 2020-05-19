# -*- coding: utf-8 -*-
# !/usr/bin/env python
path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\country_TN_distribution.txt"
pathOut = r"C:\桌面文件\代码_数据\图灵数补充实验\data\country_TNAverage.txt"
country_TNAverage_dict = dict()

with open(pathOut, 'w', encoding='utf-8') as fOut:
    fOut.write("country\taveTN\n")
    with open(path, 'r', encoding='utf-8') as f:
        flag = 0
        for row in f:
            if flag == 0:
                flag = 1
                continue
            row = row.strip('\n').split('\t')
            tolNum = int(row[1]) + int(row[2]) + int(row[3]) + int(row[4]) \
                     + int(row[5]) + int(row[6]) + int(row[7]) + int(row[8])
            aveTN = (0 * int(row[1]) + 1 * int(row[2]) + 2 * int(row[3]) + 3 * int(row[4]) \
                     + 4 * int(row[5]) + 5 * int(row[6]) + 6 * int(row[7]) + 7 * int(row[8])) / tolNum
            fOut.write(row[0]+'\t'+str(aveTN)+'\n')
        pass
