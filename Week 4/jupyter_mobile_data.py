#!/usr/bin/env python
# coding: utf-8
# In[3]:
import pandas as pd
# In[4]:
import seaborn
# In[5]:
from matplotlib import pyplot
# In[22]:
md = pd.read_csv("Week 4\mcss.csv")
# In[23]:
print(pd.set_option('display.max_rows', 50))
# In[8]:
print(md.shape)
# In[9]:
print(md.describe)
# In[10]:
print(md.head())
# In[11]:
print(md.tail())
# In[13]:
print(md.columns)
# In[19]:
mds = md.sort_values("1990")
# In[20]:
print(mds.to_csv("Week 4\1990_s.csv"))
# In[69]:
mdnew = pd.read_csv("Week 4\mcss.csv")
# In[71]:
year = list(mdnew.loc[:, "1980":"2021"].columns)
# In[72]:
canada = list(mdnew[mdnew['Country Name'] == "Canada"].loc[:, "1980":"2021"].values[0])
# In[73]:
belgium = list(mdnew[mdnew["Country Name"] == "Belgium"].loc[:, "1980":"2021"].values[0])
# In[75]:
switzerland = list(mdnew[mdnew["Country Name"] == "Switzerland"].loc[:, "1980":"2021"].values[0])
# In[79]:
pyplot.plot(year, canada)
pyplot.plot(year, belgium)
pyplot.plot(year, switzerland)
pyplot.xlabel('Year')
pyplot.ylabel('Mobile subscriptions (10million)')
pyplot.xticks(rotation=60)
pyplot.title("Mobile phone users")
pyplot.legend(["Canada", "Belgium", "Switzerland"])
print(pyplot.show())


# In[ ]:




