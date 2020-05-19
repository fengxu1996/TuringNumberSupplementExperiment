# -*- coding: utf-8 -*-
# !/usr/bin/env python
path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_hIndex_paperNum" \
       r"_citationSum_TN_country.txt"
TN_avePaperNum_aveCitation_avehIndex_dict = dict()
with open(path, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.strip('\n').split('\t')
        if row[4] not in TN_avePaperNum_aveCitation_avehIndex_dict.keys():
            TN_avePaperNum_aveCitation_avehIndex_dict[row[4]] = []
        TN_avePaperNum_aveCitation_avehIndex_dict[row[4]].append(row)
        pass
    pass
pathOut = r"C:\桌面文件\代码_数据\图灵数补充实验\data\TN_avePaperNum_" \
        r"aveCitation_aveHIndex.txt"
with open(pathOut, 'w', encoding='utf-8') as f:
    f.write("TN\tavePaperNum\taveCitation\taveHIndex\n")
    for tn in range(0, 8):
        authorList = TN_avePaperNum_aveCitation_avehIndex_dict[str(tn)]
        avePaperNum = 0
        aveCitation = 0
        aveHIndex = 0
        for author in authorList:
            avePaperNum += int(author[2])
            aveCitation += int(author[3])
            aveHIndex += int(author[1])
        avePaperNum /= len(authorList)
        aveCitation /= len(authorList)
        aveHIndex /= len(authorList)
        f.write(str(tn)+'\t'+str(avePaperNum)+
                '\t'+str(aveCitation)+'\t'+str(aveHIndex)+'\n')
        pass
