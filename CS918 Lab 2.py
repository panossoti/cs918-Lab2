#!/usr/bin/env python
# coding: utf-8

# In[121]:


#Write a program  to read the file,then print the name of the team  with the smallest  difference in ‘for’ and ‘against’  goals.

#open and read the football file without the csv library
import pandas as pd

df=pd.read_csv('football.csv',index_col="Team")

df.head()


# In[115]:


df['Goal_diff']=abs(df['Goals']-df['Goals Allowed'])

#Index column to find team with minimum difference

result=df['Goal_diff'].idxmin()


# In[113]:


print("Team with smallest Goal Difference is : ",result)


# In[118]:


#second weather dataset

weather=pd.read_csv('weather.csv',index_col=0)

weather.head()


# In[117]:


weather['Temp_diff']=(weather['MxT']-weather['MnT'])

#result_1=(min(filter(lambda x: x>0,weather['Temp_diff'])))

result_1=weather['Temp_diff'].idxmin()

print("Day with smallest temperature difference is day : ",result_1)


# In[ ]:




