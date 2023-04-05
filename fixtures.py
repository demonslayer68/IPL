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


# In[4]:


# read and format fixtures data
# got fixtures json from the webpage
pd.read_json( 'fixtures.json' )[ 'Data' ].Value
fixtures = pd.json_normalize( pd.read_json( 'fixtures.json' )[ 'Data' ].Value )
fixtures = fixtures[[ 'MatchId', 'HomeTeamShortName', 'AwayTeamShortName' ]]


# In[5]:


# default values for nextmatch
fixtures['HomeNextMatch'] = 10
fixtures['AwayNextMatch'] = 10


# In[6]:


# populate next match
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


# pd options to see full data
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
 
#display(fixtures)


# In[13]:


# Get distribution of next match distance

NextArray = list(fixtures['AwayNextMatch'].values) + list( fixtures['HomeNextMatch'].values )
print('total number of matches * 2:', len(NextArray))
count = Counter(NextArray)
count = dict(count)
count = OrderedDict(sorted(count.items()))
count


# In[14]:


# map of number of transfers for each next match distance
# 1 and 10 are bogus so putting 0
transfers = { 1 : 0, 2 : 4, 3 : 4, 4 : 1, 5 : 1, 6: 0, 7 : 0, 8 : 0, 10 : 0 }


# In[15]:


# populate populate transfers by match
home_transfers = [ transfers[x] for x in fixtures['HomeNextMatch'].values ]
away_transfers = [ transfers[x] for x in fixtures['AwayNextMatch'].values ]
fixtures[ 'HomeTransfers' ] = home_transfers
fixtures[ 'AwayTransfers' ] = away_transfers
fixtures[ 'TotalTransfers' ] = fixtures[ 'AwayTransfers' ] + fixtures[ 'HomeTransfers' ] 


# In[16]:


print( 'number of proposed transfers: ', fixtures['TotalTransfers'].sum() )


# In[19]:


fixtures.to_csv('proposed_transfers.csv')


# In[20]:


fixtures


# In[ ]:




