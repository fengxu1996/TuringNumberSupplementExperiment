# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_hIndex_paperNum_citationSum_TN_country.txt"
data = pd.read_csv(path, sep='\t', header=0,
                   dtype={'ID': str, 'hIndex': int, 'paperNum': int, 'citationSum': int, 'TN': int, 'country': str})
print(data.head())
data = data.drop(['country'], axis=1)
print(data.columns)
print('pearson', data.corr('pearson'), 'kendall', data.corr('kendall'), 'spearman', data.corr('spearman'), sep='\n\n')
# 'pearson', 'kendall', 'spearman'

# pearson
#
#                hIndex  paperNum  citationSum        TN
# hIndex       1.000000  0.863195     0.742841 -0.439536
# paperNum     0.863195  1.000000     0.650009 -0.330402
# citationSum  0.742841  0.650009     1.000000 -0.257893
# TN          -0.439536 -0.330402    -0.257893  1.000000
#
# kendall
#
#                hIndex  paperNum  citationSum        TN
# hIndex       1.000000  0.804712     0.792349 -0.408444
# paperNum     0.804712  1.000000     0.619382 -0.380894
# citationSum  0.792349  0.619382     1.000000 -0.393120
# TN          -0.408444 -0.380894    -0.393120  1.000000
#
# spearman
#
#                hIndex  paperNum  citationSum        TN
# hIndex       1.000000  0.897436     0.899842 -0.490111
# paperNum     0.897436  1.000000     0.772262 -0.463069
# citationSum  0.899842  0.772262     1.000000 -0.499687
# TN          -0.490111 -0.463069    -0.499687  1.000000
