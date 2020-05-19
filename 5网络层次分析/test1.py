# -*- coding: utf-8 -*-
# !/usr/bin/env python
import networkx as nx
import queue
G = nx.Graph()

G.add_node('1')
G.add_node('2')
G.add_node('3')
G.add_node('4')
G.add_node('5')
G.add_node('6')
G.add_edge('1', '2')
G.add_edge('3', '5')
G.add_edge('1', '4')
G.add_edge('2', '4')
# print(G.__len__(), len(G))
# print(G.number_of_nodes())
# print(G.nodes)
# print(G.number_of_edges())
print(nx.degree_centrality(G))
print(nx.betweenness_centrality(G))
print(nx.load_centrality(G))
print(nx.closeness_centrality(G))
print(nx.eigenvector_centrality(G))
# for k, v in nx.closeness_centrality(G).items():
#     print(k, v)
#     pass


# print(G['1'])
# for k, v in G['1'].items():
#     print(k, v)

# print(G.neighbors('6'))
# for x in G.neighbors('6'):
#     print(x)
#     print('-')

# Q = queue.Queue()
# Q.put('1')
# Q.put('2')
# Q.put('3')
# Q.put('4')
#
# while Q.empty() is False:
#     print(Q.get())
#
#
#
# x = {}
# x[1]=1
# print(set(list(x.keys())))

# set_nodes = set()
# path2 = r"C:\桌面文件\代码_数据\TuringNumberSupplementExperiment\data\ID_hIndex_paperNum_citationSum_TN_country.txt"
# with open(path2, 'r', encoding='utf-8') as f:
#     flag = 0
#     for row in f:
#         if flag == 0:
#             flag = 1
#             continue
#         row = row.rstrip('\n').split('\t')
#         set_nodes.add(row[0])
#
# with open(r"C:\桌面文件\代码_数据\TuringNumberSupplementExperiment\data\networkEdge_final.txt", 'w', encoding='utf-8') as fOut:
#     with open(r"C:\桌面文件\代码_数据\TuringNumberSupplementExperiment\data\networkEdge.txt", 'r', encoding='utf-8') as f:
#         for row in f:
#             row = row.strip('\n').split('\t')
#             if row[0] not in set_nodes or row[1] not in set_nodes:
#                 continue
#             fOut.write(row[0]+'\t'+row[1]+'\n')

