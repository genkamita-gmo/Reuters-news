# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("title-brexit-count.txt",names=["date","brexit_news"])
time = pd.to_datetime(df.date, format='%Y%m%d')
plt.plot(time, df.brexit_news.tolist())
plt.show()
