# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pandas as pd
path_format = r"C:\桌面文件\代码_数据\图灵数补充实验\data\countrysScholar\{}.txt".format
# data = pd.read_csv(path, sep='\t', header=0,
#                    dtype={'ID': str, 'hIndex': int, 'paperNum': int, 'citationSum': int, 'TN': int, 'country': str})
countries = ['US', 'CN', 'DE', 'FR', 'CA', 'GB', 'JP', 'BR', 'KR', 'IT', 'ES', 'IN', 'TW', 'AU', 'IL', 'NL', 'SG', 'CH',
             'PL', 'IR', 'SE', 'AT', 'TR', 'HK', 'PT', 'DK', 'GR', 'BE', 'NO', 'CZ', 'FI', 'PK', 'HU', 'MX', 'RU', 'IE',
             'NZ', 'AR', 'RO', 'MY', 'SI', 'CL', 'EG', 'TH', 'AE', 'SA', 'UY', 'TN', 'JO', 'CO', 'CY', 'ID', 'HR', 'DZ',
             'SK', 'ZA', 'RS', 'BG', 'BD', 'VN', 'MA', 'LU', 'EE', 'LK', 'PR', 'IS', 'UA', 'QA', 'LB', 'CR', 'LT', 'MK',
             'KW']
             # 'KW'], 'PH', 'CU', 'MO', 'KZ', 'HT', 'JM', 'VE', 'BY', 'GP', 'PA', 'EC', 'OM', 'MT', 'PF', 'BH', 'IQ', 'AL',
             # 'NG', 'FJ', 'BN', 'SN', 'ET', 'TT', 'GE', 'MD', 'DJ', 'ME', 'CW', 'AM', 'VA', 'HN', 'GF', 'NP', 'ZW', 'BA',
             # 'KE', 'LV', 'GH', 'GT', 'PE', 'BO', 'GU', 'SD', 'KH', 'RW', 'TZ']
pathOut = r"C:\桌面文件\代码_数据\图灵数补充实验\data\eachCountryCorrForTN(spearman).txt"
f = open(pathOut,'w', encoding='utf-8')
f.write("country\thIndex\tpaperNum\tcitationSum\tTN\n")
for c in countries:
    path_i  = path_format(c)
    data = pd.read_csv(path_i, sep='\t', header=None, names=['ID', 'hIndex', 'paperNum', 'citationSum', 'TN', 'country'],
                       dtype={'ID': str, 'hIndex': int, 'paperNum': int, 'citationSum': int, 'TN': int, 'country': str})
    # print(data.columns)
    data = data.drop(['country'], axis=1)
    # 'pearson', 'kendall', 'spearman'
    corrDF = data.corr('spearman')
    print(c)
    # print(corrDF)
    print(corrDF['TN']['hIndex'], corrDF['TN']['paperNum'], corrDF['TN']['citationSum'], corrDF['TN']['TN'])
    x = [corrDF['TN']['hIndex'], corrDF['TN']['paperNum'], corrDF['TN']['citationSum'], corrDF['TN']['TN']]
    f.write(c+'\t'+'\t'.join(list(map(str, x)))+'\n')
    # break
f.close()
