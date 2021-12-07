import pandas as pd
import numpy as np
import os
import glob
from typing import Union

os.chdir('data')
filename_list = glob.glob(r'*_lvr_land_a.csv')
df_list = [(pd.read_csv(filename)).drop(0) for filename in filename_list]  # remove english header
df_all = pd.concat(df_list, axis=0, ignore_index=True)


def conversion(floor: Union[str, float]) -> int:
    if pd.isna(floor):
        return 0
    else:
        map_dict = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10}
        str_list = list(floor)

        if len(str_list) == 2:  # <= 10
            return map_dict[str_list[0]]
        elif str_list[0] == '十':  # 11~19
            return map_dict[str_list[0]] + map_dict[str_list[1]]
        elif len(str_list) == 3:  # 20, 30, 40...
            return map_dict[str_list[0]] * 10
        else:  # 2x, 3X, 4X...
            return map_dict[str_list[0]] * 10 + map_dict[str_list[2]]


df_all['總樓層數_int'] = df_all['總樓層數'].apply(conversion)

filter_a = df_all.loc[(df_all['主要用途'] == '住家用') & (df_all['建物型態'].str.contains("住宅大樓")) & (df_all['總樓層數_int'] >= 13)]
filter_a = filter_a.sort_values(by=['總樓層數_int'])
filter_a.to_csv('filter_a.csv', index=False)

df_all['車位數'] = df_all['交易筆棟數'].apply(lambda x: list(x)[-1])

d = {'總件數': [df_all.shape[0]],
     '總車位數': [df_all['車位數'].astype(int).sum()],
     '平均總價元': [df_all['總價元'].astype(int).mean()],
     '平均車位總價元': [df_all['車位總價元'].astype(int).mean()]}

filter_b = pd.DataFrame(data=d)
filter_b.to_csv('filter_b.csv', index=False)
