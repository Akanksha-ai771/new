#!/usr/bin/env python
# coding: utf-8

# HOW I READ TABULAR DATA FILE INTO PANDAS

# In[4]:


import pandas as pd


# In[5]:


orders=pd.read_table('chipotle.tsv')
orders.head()


# pd.read_table('http://bit.ly/chiporders')

# In[6]:


cols=['id','age','gender','occupation','zipcode']
pd.read_table('http://bit.ly/movieusers',sep='|',header=None)


# SELECT PANDAS SERIES FROM DATAFRAME

# In[ ]:


new=pd.read_csv('http://bit.ly/uforeports')
new


# In[ ]:


new.head()


# In[ ]:


new['State'].head()


# In[ ]:


new.columns


# In[ ]:


new.rename(columns={'City':'Area'})


# In[ ]:


new. City.head


# In[ ]:


new['loc']=new['City']+' '+new['State']
new.head()


# In[ ]:


movies=pd.read_csv('http://bit.ly//imdbratings')
movies.head()


# In[ ]:


movies.describe(include=['float64']).head()


# In[ ]:


movies.shape


# In[ ]:


movies.dtypes
   


# In[ ]:


movies.rename(columns={'title':'Name','duration':'time'},inplace=True)
movies


# In[ ]:


movies_col=['rating','name','cr','category','time','Actors']
movies.columns=movies_col
movies.columns


# In[ ]:


movies


# In[ ]:


movies['name'].sort_values(ascending=True).head()


# In[ ]:


bools=[]
for value in movies['time']:
    if value>=150:
        bools.append(True)
    else:
        bools.append(False)
n=pd.Series(bools)     
movies[n]


# In[ ]:


movies[bools]


# In[ ]:


n2=movies.time>=200
type(n2)


# In[ ]:


movies[(movies.category=='Drama') | (movies.category=='Adventure')]


# In[ ]:


movies.dtypes


# In[ ]:


movies.time.mean(axis=0)


# #string methods

# In[ ]:


orders


# In[ ]:


orders['quantity']


# In[ ]:


orders[orders.item_name.str.contains('Chicken Bowl')]


# In[ ]:


import re
string='honeyplace'
pattern=r'honey'
match=re.search(pattern,string)
print(match)


# In[ ]:


ufo=pd.read_csv('http://bit.ly/uforeports')


# In[ ]:


ufo.tail()


# In[ ]:


ufo.isnull().tail()


# In[ ]:


ufo.isnull().sum(axis=1)


# In[ ]:


ufo[ufo.City.isnull()].State


# In[ ]:


ufo.dropna(how='any').shape


# In[ ]:


ufo['Colors Reported'].fillna(value='hi',inplace=True)


# In[ ]:


ufo.tail()


# In[ ]:


ufo['Colors Reported'].value_counts()


# In[ ]:


ufo[ufo.City.isin(['Ybor'])].State


# In[ ]:


drinks=pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()


# In[ ]:


drinks.continent.value_counts().index


# In[ ]:


drinks.describe().index


# In[ ]:


new1=pd.Series([110000,32222],index=['Albania','Algeria'],name='random')
new1


# In[ ]:


drinks.set_index('country',inplace=True)


# In[ ]:


drinks.continent.value_counts().values


# In[ ]:


drinks.beer_servings*new1


# In[ ]:


pd.concat([drinks,new1],axis=0)


# In[ ]:


drinks.loc[0,:]


# In[ ]:


drinks.set_index('country',inplace=True)
drinks


# In[ ]:


drinks.loc[0:2,:]


# In[ ]:


ufo


# In[ ]:


ufo.drop('Time',axis=1).head()


# In[ ]:


sorted(drinks.continent.unique())


# In[ ]:


train=pd.read_csv('http://bit.ly/kaggletrain')
train.head()


# In[ ]:


train['New']=train.Sex.map({'female':0,'male':1})


# In[ ]:


train.head()

pd.get_dummies(train.New)
# In[ ]:


pd.get_dummies(train.New)


# In[ ]:


ufo.head()


# In[ ]:


ufo['Time']=pd.to_datetime(ufo.Time)


# In[ ]:


ufo.Time.dt.


# In[ ]:


ufo['Year']=ufo.Time.dt.year


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


ufo.Year.value_counts()


# In[ ]:


ufo.Year.value_counts().plot(kind='bar')


# In[ ]:


users=pd.read_table('http://')


# In[ ]:


pd.describe_option(rows=)


# In[ ]:


def ek(r,m):
    return r[m]


# In[ ]:


train=pd.read_csv('http://bit.ly/kaggletrain')
train


# In[ ]:


=

