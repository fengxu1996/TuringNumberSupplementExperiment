# -*- coding: utf-8 -*-
# !/usr/bin/env python
import networkx as nx
path2 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_hIndex_paperNum_citationSum_TN_country.txt"
path3 = r"C:\桌面文件\代码_数据\图灵数补充实验\data\networkEdge_final.txt"
G = nx.Graph()
with open(path2, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.rstrip('\n').split('\t')
        G.add_node(row[0])

with open(path3, 'r', encoding='utf-8') as f:
    for row in f:
        row = row.rstrip('\n').split('\t')
        G.add_edge(row[0], row[1])
# print(nx.degree_centrality(G))
# print(nx.betweenness_centrality(G))
# print(nx.load_centrality(G))
# print(nx.closeness_centrality(G))
# print(nx.eigenvector_centrality(G))
path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\node_centrality\ID_degree_centrality.txt"
with open(path, 'w', encoding='utf-8') as f:
    f.write("ID\tdegree_centrality\n")
    for k, v in nx.degree_centrality(G).items():
        f.write(k+'\t'+str(v)+'\n')
    pass
path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\node_centrality\ID_load_centrality.txt"
with open(path, 'w', encoding='utf-8') as f:
    f.write("ID\tload_centrality\n")
    for k, v in nx.load_centrality(G).items():
        f.write(k+'\t'+str(v)+'\n')
    pass
path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\node_centrality\ID_closeness_centrality.txt"
with open(path, 'w', encoding='utf-8') as f:
    f.write("ID\tcloseness_centrality\n")
    for k, v in nx.closeness_centrality(G).items():
        f.write(k+'\t'+str(v)+'\n')
    pass
path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\node_centrality\ID_eigenvector_centrality.txt"
with open(path, 'w', encoding='utf-8') as f:
    f.write("ID\teigenvector_centrality\n")
    for k, v in nx.eigenvector_centrality(G).items():
        f.write(k+'\t'+str(v)+'\n')
    pass
path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\node_centrality\ID_betweenness_centrality.txt"
with open(path, 'w', encoding='utf-8') as f:
    f.write("ID\tbetweenness_centrality\n")
    for k, v in nx.betweenness_centrality(G).items():
        f.write(k+'\t'+str(v)+'\n')
    pass
# print(G.__len__(), len(G))
# print(G.number_of_nodes())
# print(G.nodes)
# print(G.number_of_edges())
# print(nx.degree_centrality(G))
# print(nx.betweenness_centrality(G))
# print(nx.load_centrality(G))
# print(nx.closeness_centrality(G))
# print(nx.eigenvector_centrality(G))
