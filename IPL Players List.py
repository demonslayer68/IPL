#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
import json


# In[31]:


data = pd.json_normalize( pd.read_json( 'players.json' )[ 'Data' ].Value['Players'] )


# In[38]:


output = data[ ['Name', 'ShortName', 'TeamName', 'TeamShortName', 'SkillName', 'IS_FP', 'Value'] ]


# In[39]:


output.to_csv('player list.csv')

