# coding: utf-8
import pandas as pd
df = pd.read_csv("timestamp.txt",names="a")
df2 = pd.to_datetime(df.a)
