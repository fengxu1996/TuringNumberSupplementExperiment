
# import scipy.stats
# import pandas as pd
# x = [1,2,3,4,5]
# y = [6,7,8,9,6]
# df = pd.DataFrame({'x':x, 'y':y})
#
# xx = scipy.stats.pearsonr(x, y)
# print(xx)
#
# xx = scipy.stats.spearmanr(x, y)
# print(xx.correlation, xx.pvalue)
#
# print(scipy.stats.kendalltau(x, y))

import pandas as pd
import scipy.stats
path = r"C:\桌面文件\代码_数据\图灵数补充实验\data\ID_hIndex_paperNum_citationSum_TN_country.txt"
# data = pd.read_csv(path, sep='\t', header=0,
#                    dtype={'ID': str, 'hIndex': int, 'paperNum': int, 'citationSum': int, 'TN': int, 'country': str})
# print(data.head())
# data = data.drop(['country'], axis=1)
# print(data.columns)
# print('pearson', data.corr('pearson'), 'kendall', data.corr('kendall'), 'spearman', data.corr('spearman'), sep='\n\n')

data = {'hIndex':[], 'paperNum': [], 'citationSum': [], 'TN': []}
with open(path, 'r', encoding='utf-8') as f:
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            continue
        row = row.strip('\n').split('\t')
        data['hIndex'].append(int(row[1]))
        data['paperNum'].append(int(row[2]))
        data['citationSum'].append(int(row[3]))
        data['TN'].append(int(row[4]))
    pass
df = pd.DataFrame(data)
f = open(r"C:\桌面文件\代码_数据\图灵数补充实验\data\相关系数-显著性检验系数.txt", 'w', encoding='utf-8')

xx = scipy.stats.pearsonr(data['TN'], data['hIndex'])
print("TN-hIndex(pearsonr):", "correlation:", xx[0], "pvalue:", xx[1], file=f)
xx = scipy.stats.pearsonr(data['TN'], data['paperNum'])
print("TN-paperNum(pearsonr):", "correlation:", xx[0], "pvalue:", xx[1], file=f)
xx = scipy.stats.pearsonr(data['TN'], data['citationSum'])
print("TN-citationSum(pearsonr):", "correlation:", xx[0], "pvalue:", xx[1], file=f)

xx = scipy.stats.spearmanr(data['TN'], data['hIndex'])
print("TN-hIndex(spearmanr):", "correlation:", xx.correlation, "pvalue:", xx.pvalue, file=f)
xx = scipy.stats.spearmanr(data['TN'], data['paperNum'])
print("TN-paperNum(spearmanr):", "correlation:", xx.correlation, "pvalue:", xx.pvalue, file=f)
xx = scipy.stats.spearmanr(data['TN'], data['citationSum'])
print("TN-citationSum(spearmanr):", "correlation:", xx.correlation, "pvalue:", xx.pvalue, file=f)

xx = scipy.stats.kendalltau(data['TN'], data['hIndex'])
print("TN-hIndex(kendalltau):", "correlation:", xx.correlation, "pvalue:", xx.pvalue, file=f)
xx = scipy.stats.kendalltau(data['TN'], data['paperNum'])
print("TN-paperNum(kendalltau):", "correlation:", xx.correlation, "pvalue:", xx.pvalue, file=f)
xx = scipy.stats.kendalltau(data['TN'], data['citationSum'])
print("TN-citationSum(kendalltau):", "correlation:", xx.correlation, "pvalue:", xx.pvalue, file=f)

f.close()