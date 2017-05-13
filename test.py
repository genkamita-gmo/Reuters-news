# coding: utf-8
import pandas as pd

# title
df = pd.read_csv("title.txt",names="a")
print df.a.shape
print df.a

# timestamp
#df = pd.read_csv("timestamp.txt",names="a")
#df2 = pd.to_datetime(df.a)
