# -*- coding: utf-8 -*-
# !/usr/bin/env python
import networkx as nx
import queue
class zeroModel:
    def __init__(self, G, originPoints):
        self.G = G
        self.usedSet = set()  # 标记已使用过的节点
        self.originPoints = originPoints
        self.point_TN = {}  # 节点，TN
    def bfsTN(self):
        Q = queue.Queue()
        for e in self.originPoints:  # 初始点TN设置为零
            Q.put(e)
            self.point_TN[e] = 0
            self.usedSet.add(e)
        while Q.empty() is False:
            p = Q.get()
            for x in G.neighbors(p):
                if x in self.usedSet:
                    continue
                else:
                    Q.put(x)
                    self.usedSet.add(x)
                    self.point_TN[x] = self.point_TN[p] + 1
    def check(self):
        finded = set(list(self.point_TN.keys()))
        if len(finded)!=len(G):
            print(len(G)-len(finded))
            print(list(set(list(G.nodes))-finded))
    def save_data(self, pathOut):
        with open(pathOut, 'w', encoding='utf-8') as f:
            f.write("ID\tTN\n")
            for k, v in self.point_TN.items():
                f.write(k+'\t'+str(v)+'\n')
            pass

if __name__ == "__main__":
    path1 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\zeroModel\originPoints.txt"
    path2 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_hIndex_paperNum_citationSum_TN_country.txt"
    # path3 = r"C:\桌面文件\代码_数据\TuringNumberSupplementExperiment\data\networkEdge.txt"
    path3 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\networkEdge_final.txt"
    G = nx.Graph()
    originPoints_set = set()
    with open(path1, 'r', encoding='utf-8') as f:
        for row in f:
            row = row.rstrip('\n')
            originPoints_set.add(row)
        pass
    with open(path2, 'r', encoding='utf-8') as f:
        flag = 0
        for row in f:
            if flag == 0:
                flag = 1
                continue
            row = row.rstrip('\n').split('\t')
            G.add_node(row[0])
        pass
    with open(path3, 'r', encoding='utf-8') as f:
        for row in f:
            row = row.rstrip('\n').split('\t')
            G.add_edge(row[0], row[1])
        pass

    # turingSet = set()
    # turingPath = r"C:\桌面文件\代码_数据\TuringNumberSupplementExperiment\data\data1\turingID.txt"
    # with open(turingPath, 'r', encoding='utf-8') as f:
    #     flag = 0
    #     for row in f:
    #         if flag == 0:
    #             flag = 1
    #             continue
    #         row = row.strip('\n').split(',')[0]
    #         turingSet.add(row)
    zmodel = zeroModel(G, originPoints_set)

    # zmodel = zeroModel(G, turingSet)
    zmodel.bfsTN()
    zmodel.check()
    pathOut = r"C:\桌面文件\代码_数据\图灵数补充实验\data\zeroModel\zeroMode_IDTN.txt"
    zmodel.save_data(pathOut)
