# -*- coding: utf-8 -*-
# !/usr/bin/env python
path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\zeroModel\NullModel_country_TN_distribution.txt"
pathOut = r"C:\桌面文件\代码_数据\图灵数补充实验\data\zeroModel\NullModel_country_aveTN.txt"
with open(pathOut, 'w', encoding='utf-8') as fOut:
    fOut.write("country\taveTN\n")
    with open(path, 'r', encoding='utf-8') as f:
        flag = 0
        for row in f:
            if flag == 0:
                flag = 1
                continue
            row = row.strip('\n').split('\t')
            pnum = 0
            aveTN = 0
            for i in range(1, len(row)-1):
                aveTN += int(row[i])*(i-1)
                pnum += int(row[i])
                pass
            aveTN /= pnum
            fOut.write(row[0]+'\t'+str(aveTN)+'\n')
        pass
    pass
