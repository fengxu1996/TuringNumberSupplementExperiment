# -*- coding: utf-8 -*-
# !/usr/bin/env python
from collections import defaultdict
import math
path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_hIndex_paperNum" \
       r"_citationSum_TN_country.txt"
TN_IDs = dict()
with open(path, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.strip('\n').split('\t')
        if row[4] not in TN_IDs.keys():
            TN_IDs[row[4]] = []
        TN_IDs[row[4]].append(row[0])
        pass
    pass

path_betweeness = r"C:\桌面文件\代码_数据\图灵数补充实验\data\node_centrality\ID_betweenness_centrality.txt"
path_closeness = r"C:\桌面文件\代码_数据\图灵数补充实验\data\node_centrality\ID_closeness_centrality.txt"
path_degree = r"C:\桌面文件\代码_数据\图灵数补充实验\data\node_centrality\ID_degree_centrality.txt"
path_eigenvector = r"C:\桌面文件\代码_数据\图灵数补充实验\data\node_centrality\ID_eigenvector_centrality.txt"
path_load = r"C:\桌面文件\代码_数据\图灵数补充实验\data\node_centrality\ID_load_centrality.txt"

# TN_aveBetweenness_aveCloseness_aveDegree_aveEigenvector_aveLoad_dict = {}
# TN_Betweenness_Closeness_Degree_Eigenvector_Load_FullSum_dict = {}
ID_betweenness_centrality_dict = dict()
ID_closeness_centrality_dict = dict()
ID_degree_centrality_dict = dict()
ID_eigenvector_centrality_dict = dict()
ID_load_centrality_dict = dict()
with open(path_betweeness, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.strip('\n').split('\t')
        ID_betweenness_centrality_dict[row[0]] = float(row[1])
        # TN_Betweenness_Closeness_Degree_Eigenvector_Load_FullSum_dict
    pass

with open(path_closeness, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.strip('\n').split('\t')
        ID_closeness_centrality_dict[row[0]] = float(row[1])
    pass

with open(path_degree, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.strip('\n').split('\t')
        ID_degree_centrality_dict[row[0]] = float(row[1])
    pass

with open(path_eigenvector, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.strip('\n').split('\t')
        ID_eigenvector_centrality_dict[row[0]] = float(row[1])
    pass

with open(path_load, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.strip('\n').split('\t')
        ID_load_centrality_dict[row[0]] = float(row[1])
    pass
pathOut = r"C:\桌面文件\代码_数据\图灵数补充实验\data\TN_" \
          r"aveBetweenness_aveCloseness_aveDegree_aveEigenvector_aveLoad.txt"
with open(pathOut, 'w', encoding='utf-8') as f:
    f.write("TN\taveBetweenness_centrality\t"
            "aveCloseness_centrality\taveDegree_centrality\t"
            "aveEigenvector_centrality\taveLoad_centrality\n")
    for i in range(0, 8):
        IDs = TN_IDs[str(i)]
        aveBetweenness_centrality = 0
        aveCloseness_centrality = 0
        aveDegree_centrality = 0
        aveEigenvector_centrality = 0
        aveLoad_centrality = 0
        for id in IDs:
            aveBetweenness_centrality += ID_betweenness_centrality_dict[id]
            aveCloseness_centrality += ID_closeness_centrality_dict[id]
            aveDegree_centrality += ID_degree_centrality_dict[id]
            aveEigenvector_centrality += ID_eigenvector_centrality_dict[id]
            aveLoad_centrality += ID_load_centrality_dict[id]
        aveBetweenness_centrality /= len(IDs)
        aveCloseness_centrality /= len(IDs)
        aveDegree_centrality /= len(IDs)
        aveEigenvector_centrality /= len(IDs)
        aveLoad_centrality /= len(IDs)
        f.write(str(i)+'\t'+str(aveBetweenness_centrality)+'\t'+str(aveCloseness_centrality)+'\t'+
                str(aveDegree_centrality)+'\t'+str(aveEigenvector_centrality)+'\t'+
                str(aveLoad_centrality)+'\n')


pathOut = r"C:\桌面文件\代码_数据\图灵数补充实验\data\TN_" \
          r"Betweenness_Closeness_Degree_Eigenvector_Load_Sum.txt"
with open(pathOut, 'w', encoding='utf-8') as f:
    f.write("TN\tbetweenness_centrality\t"
            "closeness_centrality\tdegree_centrality\t"
            "eigenvector_centrality\tload_centrality\n")
    for i in range(0, 8):
        IDs = TN_IDs[str(i)]
        betweenness_centrality = 0
        closeness_centrality = 0
        degree_centrality = 0
        eigenvector_centrality = 0
        load_centrality = 0
        for id in IDs:
            betweenness_centrality += ID_betweenness_centrality_dict[id]
            closeness_centrality += ID_closeness_centrality_dict[id]
            degree_centrality += ID_degree_centrality_dict[id]
            eigenvector_centrality += ID_eigenvector_centrality_dict[id]
            load_centrality += ID_load_centrality_dict[id]
        f.write(str(i) + '\t' + str(betweenness_centrality) + '\t' + str(closeness_centrality) + '\t' +
                str(degree_centrality) + '\t' + str(eigenvector_centrality) + '\t' +
                str(load_centrality) + '\n')

pathOut = r"C:\桌面文件\代码_数据\图灵数补充实验\data\TN_" \
          r"aveBetweenness_aveCloseness_aveDegree_aveEigenvector_aveLoad_ln.txt"
with open(pathOut, 'w', encoding='utf-8') as f:
    f.write("TN\taveBetweenness_centrality_ln\t"
            "aveCloseness_centrality_ln\taveDegree_centrality_ln\t"
            "aveEigenvector_centrality_ln\taveLoad_centrality_ln\n")
    for i in range(0, 8):
        IDs = TN_IDs[str(i)]
        aveBetweenness_centrality = 0
        aveCloseness_centrality = 0
        aveDegree_centrality = 0
        aveEigenvector_centrality = 0
        aveLoad_centrality = 0
        for id in IDs:
            aveBetweenness_centrality += ID_betweenness_centrality_dict[id]
            aveCloseness_centrality += ID_closeness_centrality_dict[id]
            aveDegree_centrality += ID_degree_centrality_dict[id]
            aveEigenvector_centrality += ID_eigenvector_centrality_dict[id]
            aveLoad_centrality += ID_load_centrality_dict[id]
        aveBetweenness_centrality /= len(IDs)
        aveCloseness_centrality /= len(IDs)
        aveDegree_centrality /= len(IDs)
        aveEigenvector_centrality /= len(IDs)
        aveLoad_centrality /= len(IDs)
        f.write(str(i)+'\t'+str(math.log(aveBetweenness_centrality))+'\t'+str(math.log(aveCloseness_centrality))+'\t'+
                str(math.log(aveDegree_centrality))+'\t'+str(math.log(aveEigenvector_centrality))+'\t'+
                str(math.log(aveLoad_centrality))+'\n')

pathOut = r"C:\桌面文件\代码_数据\图灵数补充实验\data\TN_" \
          r"aveBetweenness_aveCloseness_aveDegree_aveEigenvector_aveLoad_e.txt"
with open(pathOut, 'w', encoding='utf-8') as f:
    f.write("TN\taveBetweenness_centrality_e\t"
            "aveCloseness_centrality_e\taveDegree_centrality_e\t"
            "aveEigenvector_centrality_e\taveLoad_centrality_e\n")
    for i in range(0, 8):
        IDs = TN_IDs[str(i)]
        aveBetweenness_centrality = 0
        aveCloseness_centrality = 0
        aveDegree_centrality = 0
        aveEigenvector_centrality = 0
        aveLoad_centrality = 0
        for id in IDs:
            aveBetweenness_centrality += ID_betweenness_centrality_dict[id]
            aveCloseness_centrality += ID_closeness_centrality_dict[id]
            aveDegree_centrality += ID_degree_centrality_dict[id]
            aveEigenvector_centrality += ID_eigenvector_centrality_dict[id]
            aveLoad_centrality += ID_load_centrality_dict[id]
        aveBetweenness_centrality /= len(IDs)
        aveCloseness_centrality /= len(IDs)
        aveDegree_centrality /= len(IDs)
        aveEigenvector_centrality /= len(IDs)
        aveLoad_centrality /= len(IDs)
        f.write(str(i)+'\t'+str(math.e**aveBetweenness_centrality)+'\t'+str(math.e**aveCloseness_centrality)+'\t'+
                str(math.e**aveDegree_centrality)+'\t'+str(math.e**aveEigenvector_centrality)+'\t'+
                str(math.e**aveLoad_centrality)+'\n')
