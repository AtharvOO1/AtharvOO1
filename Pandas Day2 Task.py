#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Find out there average rating on weekly basis keep this in mind that they take two days of leave.
#2. Total working days for each agents 
#3. Total query that you have taken 
#4. Total Feedback that you have received 
#5. An agent name who have average rating between 3.5 to 4 
#6. Agent name who have rating lesss then 3.5 
#7. agent name who have rating more then 4.5 
#8. how many feedaback agents have received more then 4.5 average 
#9. average weekly response time for each agent 
#10. average weekely resolution time for each agents 
#11. list of all agents name 
#12. Percentage of chat on which they have received a feedback 
#13. Total contributation hour for each and every agents weekly basis 
#14. total percentage of active hour for a month


# In[2]:


import pandas as pd


# In[3]:


pd.read_csv(r'C:\Users\ADIXIT\Desktop\Pandas Day 2\AgentPerformance.csv')


# In[4]:


df= pd.read_csv(r'C:\Users\ADIXIT\Desktop\Pandas Day 2\AgentPerformance.csv')


# In[5]:


df.dtypes


# In[10]:


df['Conv_Date']= pd.to_datetime(df['Date'])


# In[11]:


type(Conv_Date[0])


# In[12]:


df


# In[17]:


df['week'] =df['Conv_Date'].dt.weekofyear


# In[18]:


df


# In[24]:


df.groupby('week')['Average Rating'].mean()


# In[25]:


df.drop('Overall_avg_rating', axis=1, inplace= True)


# In[37]:


df.drop('Total Working Days', axis=1, inplace= True)


# In[38]:


df


# In[27]:


pd.read_csv(r'C:\Users\ADIXIT\Desktop\Pandas Day 2\AgentLogingReport.csv')


# In[28]:


df2= pd.read_csv(r'C:\Users\ADIXIT\Desktop\Pandas Day 2\AgentLogingReport.csv')


# In[29]:


df2.dtypes


# In[31]:


df2['New Date']= pd.to_datetime(df2['Date'])


# In[32]:


df2


# In[40]:


#2. Total working days for each agents  

df2.groupby('Agent')['New Date'].count()


# In[42]:


#3. Total query that you have taken 

df.groupby('Agent Name')['Total Chats'].sum()


# In[45]:


#4. Total Feedback that you have received

df.groupby('Agent Name')['Total Feedback'].sum()


# In[51]:


#5. An agent name who have average rating between 3.5 to 4 

df[df['Average Rating']>= 3.5]


# In[52]:


#6. Agent name who have rating less than 3.5 

df[df['Average Rating']< 3.5]


# In[63]:


#7. Agent name who have rating more than 4.5 

df3= df[df['Average Rating']> 4.5]


# In[64]:


df3


# In[65]:


#8. How many feedaback agents have received more than 4.5 average 

df3.groupby('Agent Name')['Total Feedback'].sum()


# In[69]:


df['New_Avg_Resp_Time']= pd.to_datetime(df['Average Response Time'])


# In[70]:


df


# In[ ]:


#9. average weekly response time for each agent 


# In[ ]:


#10. Confusion


# In[73]:


#11. list of all agents name 

df['Agent Name']


# In[76]:


#12. Percentage of chat on which they have received a feedback 

df.groupby('Total Feedback')['Total Chats'].


# In[ ]:




