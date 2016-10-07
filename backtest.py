import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os

df = pd.read_csv('Desktop/stock_research/sz300_data/150101_160922/603993.SH.CSV')
use_df = df[[0,7]]
use_df.columns = ['code', 'close']

n_short = 2
n_long = 20
SD = 1

ma_short = pd.rolling_mean(use_df.close, n_short)
ma_long = pd.rolling_mean(use_df.close, n_long)

regime = np.where(ma_short / ma_long > SD, 1, 0)
regime = pd.Series(regime, index = ma_short.index)

pp_ratio_bnh = np.log(use_df.close / use_df.close.shift(1) )
pp_ratio_strategy = regime.shift(1) * pp_ratio_bnh

norm_return_bnh = pp_ratio_bnh.cumsum().apply(np.exp)
norm_return_strategy = pp_ratio_strategy.cumsum().apply(np.exp)

fig = plt.figure() # create a new figure
norm_return_strategy.plot(lw=1.5, figsize=(8,4), label=u'Strategy')
norm_return_bnh.plot(lw=1.5, label=u'BnH')