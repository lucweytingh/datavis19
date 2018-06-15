
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np
import matplotlib.pyplot 


data = pd.read_csv("data_clean.csv")


# In[22]:


#amount of entries per country
data.groupby(["country_name"]).country_name.count() 


# In[24]:


#landen
data["country_name"].unique()


# In[25]:


#aantal landen
len(data["country_name"].unique().tolist())


# In[19]:


#aantal markten
len(data["market_name"].unique().tolist())


# In[20]:


#gemiddeld aantal markten per land
data.groupby(["country_name"]).market_name.count().mean()


# In[26]:


#verkochte producten
data["item_name"].unique()


# In[27]:


#aantal verchillende prodcuten
len(data["item_name"].unique().tolist())


# In[29]:


#minimale jaar
data["year"].min()


# In[30]:


#maximale jaar
data["year"].max()


# In[47]:


#aantal verschillende producten per jaar
data.groupby(["year"]).item_name.count()


# In[39]:


#totale omzet in USD per jaar
df=data.groupby(["year"]).price_usd.sum()


# In[44]:


#plot van de meest omzet rijke jaren
ax=df.plot(lw=2, colormap='jet', marker='.', markersize=10, title='omzet alle landen per jaar')
ax.set_ylabel("USD")

