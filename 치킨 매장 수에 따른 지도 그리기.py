#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


commercial = pd.read_csv('./commercial.csv')
commercial


# In[3]:


# 끝에 5개 데이터만 추출
commercial.tail(5)


# In[5]:


list(commercial), len(list(commercial))


# In[7]:


commercial.groupby('상가업소번호')['상권업종소분류명'].count().sort_values(ascending=False)


# In[10]:


category_range = set(commercial['상권업종소분류명'])
category_range, len(category_range)


# In[11]:


commercial['도로명주소']


# In[15]:


# 서울시 데이터만 가져오기
# 3덩어리로 쪼갠 후 새로운 칼럼 추가
commercial[['시','구','상세주소']] = commercial['도로명주소'].str.split(' ',n=2, expand=True)


# In[16]:


commercial.tail(5)


# In[18]:


# 서울특별시의 데이터만 추출
seoul_data = commercial[ commercial['시'] == '서울특별시']
seoul_data.tail(5)


# In[22]:


# 서울만 있는지 확인하기(집합연산)
city_type = set(seoul_data['시'])
city_type


# In[24]:


# 서울 치킨집만 추출
seoul_chicken_data = seoul_data[ seoul_data['상권업종소분류명'] == '후라이드/양념치킨' ]
seoul_chicken_data


# In[31]:


sorted_chicken_count_by_gu = seoul_chicken_data.groupby('구')['상권업종소분류명'].count().sort_values(ascending=False)
sorted_chicken_count_by_gu


# In[33]:


import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'


# In[34]:


plt.figure(figsize=(10,5))
plt.bar(sorted_chicken_count_by_gu.index, sorted_chicken_count_by_gu)
plt.title('구에 따른 치킨 매장 수')
plt.xticks(rotation = 90)
plt.show()


# In[38]:


# 지도에 그리기
import folium
import json


# In[41]:


# 지도정보 불러오기
seoul_geo = './seoul_geo.json'
geo_data = json.load(open(seoul_geo, encoding = 'utf-8'))
geo_data


# In[50]:


# 지도 만들기
map = folium.Map(location=[37.5502, 126.982], zoom_start=11)
map


# In[51]:


folium.Choropleth(geo_data = geo_data,
                data=sorted_chicken_count_by_gu,
                colums=[sorted_chicken_count_by_gu.index, sorted_chicken_count_by_gu],
                fill_color='PuRd',
                key_on='properties.name').add_to(map)
map


# In[ ]:




