#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[48]:


df = pd.read_excel('Desna-Chernihiv.xlsx', index_col = "Date", parse_dates = True)
df2 = pd.read_excel('Desna-Litky.xlsx', index_col = "Date", parse_dates = True)


# In[52]:


# Plot options: ### daily ###   ### mean ### ("mean" is set as a default in drop-list menu)
df.plot()
plt.xlabel(None)
plt.ylabel("Вирати води, м3/с")
plt.axis([None,None,0,None])
plt.title("р. Десна - м. Чернігів")
plt.legend().set_visible(False)
plt.show()


# In[57]:


# Plot options: ### monthly ###   ### mean ###
df.resample('M').mean().plot()
plt.xlabel(None)
plt.ylabel("Вирати води, м3/с")
plt.axis([None,None,0,None])
plt.title("р. Десна - м. Чернігів")
plt.legend().set_visible(False)
plt.show()


# In[58]:


# Plot options: ### yearly ###   ### mean ###
df.resample('Y').mean().plot()
plt.xlabel(None)
plt.ylabel("Вирати води, м3/с")
plt.axis([None,None,0,None])
plt.title("р. Десна - м. Чернігів")
plt.legend().set_visible(False)
plt.show()


# In[59]:


# Plot options: ### monthly ###   ### max ### (аналогічно yearly)
df.resample('M').max().plot() #я б хотів, щоби цей графік був у вигляді стовбців (див. excel), а не лінії. Але hist будує інше.
plt.xlabel(None)
plt.ylabel("Вирати води, м3/с")
plt.axis([None,None,0,None])
plt.title("р. Десна - м. Чернігів")
plt.legend().set_visible(False)
plt.show()


# In[60]:


# Plot options: ### monthly ###   ### min ###
df.resample('M').min().plot() #я б хотів, щоби цей графік був у вигляді стовбців (див. excel), а не лінії. Але hist будує інше.
plt.xlabel(None)
plt.ylabel("Вирати води, м3/с")
plt.axis([None,None,0,None])
plt.title("р. Десна - м. Чернігів")
plt.legend().set_visible(False)
plt.show()


# In[61]:


# Plot options: ### daily ###   ### frequency curve ###
df_sorted = df.sort_values("Q", ascending=False)
df_sorted["sort_index"] = range(1,len(df_sorted) + 1)
df_sorted["P"] = df_sorted["sort_index"]/(len(df_sorted) + 1)
df_sorted.plot(x = "P", y = "Q")
plt.ylabel("Вирати води, м3/с")
plt.xlabel("Забезпеченість")
plt.axis([0,None,0,None])
plt.title("р. Десна - м. Чернігів")
plt.legend().set_visible(False)
plt.show()


# In[62]:


# Plot options: ### monthly ###   ### frequency curve ###
df_sorted = df.resample("M").mean().sort_values("Q", ascending=False)
df_sorted["sort_index"] = range(1,len(df_sorted) + 1)
df_sorted["P"] = df_sorted["sort_index"]/(len(df_sorted) + 1)
df_sorted.plot(x = "P", y = "Q")
plt.ylabel("Вирати води, м3/с")
plt.xlabel("Забезпеченість")
plt.axis([0,None,0,None])
plt.title("р. Десна - м. Чернігів")
plt.legend().set_visible(False)
plt.show()


# In[63]:


# Plot options: ### yearly ###   ### frequency curve ###
df_sorted = df.resample("Y").mean().sort_values("Q", ascending=False)
df_sorted["sort_index"] = range(1,len(df_sorted) + 1)
df_sorted["P"] = df_sorted["sort_index"]/(len(df_sorted) + 1)
df_sorted.plot(x = "P", y = "Q")
plt.ylabel("Вирати води, м3/с")
plt.xlabel("Забезпеченість")
plt.axis([0,None,0,None])
plt.title("р. Десна - м. Чернігів")
plt.legend().set_visible(False)
plt.show()


# In[64]:


# Plot options: ### year daily ###   ### mean ###
df.groupby(df.index.dayofyear).mean().plot()
plt.xlabel(None)
plt.ylabel("Вирати води, м3/с")
plt.xlabel("День у році")         #бажано зробити вісь дат, тоді підпис осі не потрібно
plt.axis([None,None,0,None])
plt.title("р. Десна - м. Чернігів")
plt.legend().set_visible(False)
plt.show()


# In[65]:


# Plot options: ### year monthly ###   ### mean ###
df.groupby(df.index.month).mean().plot()
plt.xlabel(None)                       # треба номера місяців замінити на символи: Січ, Лют, Бер,...
plt.ylabel("Вирати води, м3/с")
plt.axis([1,None,0,None])
plt.title("р. Десна - м. Чернігів")
plt.legend().set_visible(False)
plt.show()


# In[66]:


# Plot options: ### year daily ###   ### mean ###
Q1 = df["1990":"2019"].groupby(df["1990":"2019"].index.dayofyear).mean()
Q2 = df["1960":"1989"].groupby(df["1960":"1989"].index.dayofyear).mean()
plt.plot(Q1)
plt.plot(Q2)
plt.xlabel(None)
plt.ylabel("Вирати води, м3/с")
plt.xlabel("День у році")         #бажано зробити вісь дат, тоді підпис осі не потрібно
plt.axis([1,366,0,None])
plt.legend(["1990-2019","1960-1989"])
plt.title("р. Десна - м. Чернігів")
plt.show()                     #Якщо це можливо (однакова вісь х), то графіки зображуються в одному вікні, 
                               #якщо користувач його не закрив


# In[69]:


# Plot options: ### year daily ###   ### mean ###
Q1 = df["1990":"2018"].groupby(df["1990":"2018"].index.dayofyear).mean()
Q2 = df2["1990":"2018"].groupby(df["1990":"2018"].index.dayofyear).mean()
plt.plot(Q1)
plt.plot(Q2)
plt.xlabel(None)
plt.ylabel("Вирати води, м3/с")
plt.xlabel("День у році")         #бажано зробити вісь дат, тоді підпис осі не потрібно
plt.axis([1,366,0,None])
plt.legend(["м. Чернігів, 1990-2018","с. Літки, 1990-2018"])
plt.title("р. Десна")
plt.show()                     #Якщо це можливо (однакова вісь х), то графіки зображуються в одному вікні, 
                               #якщо користувач його не закрив


# In[ ]:




