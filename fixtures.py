#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
import json
from collections import Counter
from collections import OrderedDict


# In[ ]:


pd.read_json( 'fixtures.json' )[ 'Data' ].Value


# In[3]:


fixtures = pd.json_normalize( pd.read_json( 'fixtures.json' )[ 'Data' ].Value )


# In[4]:


fixtures = fixtures[[ 'MatchId', 'HomeTeamShortName', 'AwayTeamShortName' ]]


# In[5]:


fixtures['HomeNextMatch'] = 10
fixtures['AwayNextMatch'] = 10


# In[6]:


for i in range(len(fixtures)):
    for team in [ fixtures['HomeTeamShortName'][i], fixtures['AwayTeamShortName'][i] ]:
        for j in range(i+1,len(fixtures)):
            if team == fixtures['HomeTeamShortName'][j] or team == fixtures['AwayTeamShortName'][j]:
                if team == fixtures['HomeTeamShortName'][i]:
                    fixtures.loc[i, ['HomeNextMatch']] = [j - i]
                else:
                    fixtures.loc[i, ['AwayNextMatch']] = [j - i]
                break        


# In[7]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
 
# All dataframes hereafter reflect these changes.
display(fixtures)


# In[8]:


NextArray = list(fixtures['AwayNextMatch'].values) + list( fixtures['HomeNextMatch'].values )


# In[9]:


len(NextArray)


# In[10]:


count = Counter(NextArray)
count = dict(count)


# In[11]:


count = OrderedDict(sorted(count.items()))
count


# In[12]:


transfers = { 1 : 0, 2 : 4, 3 : 4, 4 : 1, 5 : 1, 6: 0, 7 : 0, 8 : 0, 10 : 0 }
home_transfers = [ transfers[x] for x in fixtures['HomeNextMatch'].values ]
away_transfers = [ transfers[x] for x in fixtures['AwayNextMatch'].values ]
fixtures[ 'HomeTransfers' ] = home_transfers
fixtures[ 'AwayTransfers' ] = away_transfers
fixtures[ 'TotalTransfers' ] = fixtures[ 'AwayTransfers' ] + fixtures[ 'HomeTransfers' ] 


# In[13]:


fixtures['TotalTransfers'].sum()


# In[14]:


fixtures


# In[31]:


3 * 0 + 1 * 3 + 18 * 3 + 31 * 1 + 31 * 1 + 33 * 0 + 11 * 0 + 5 * 0 + 15 * 0


# In[20]:


sum(list(count.values()))


# In[ ]:





# In[21]:


31 * 1 + 11 * 0 + 31 * 1 + 33 * 0 + 5 * 0 + 18 * 3 + 1 * 5 + 10 * 0


# In[ ]:




