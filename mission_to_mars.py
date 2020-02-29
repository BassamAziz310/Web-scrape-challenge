#!/usr/bin/env python
# coding: utf-8

# In[2]:


from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd 
import requests
import pymongo
import json


# In[3]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# In[5]:


db = client.nhl_db
collection = db.articles


# In[6]:


url = "https://mars.nasa.gov/news/8613/a-year-of-surprising-science-from-nasas-insight-mars-mission/"


# In[7]:


response = requests.get(url)

response 


# In[8]:


soup = BeautifulSoup(response.text, 'lxml')

soup


# In[9]:


results = soup.find_all('div', class_="article-item__top")

results


# In[10]:


for result in results:
    # scrape the article header 
    header = result.find('h1', class_='article-item__headline').text
    
    # scrape the article subheader
    subheader = result.find('h2', class_='article-item__subheader').text
    
    # scrape the datetime
    datetime = result.find('span', class_="article-item__date")['data-date']
    
    # get only the date from the datetime
    date = datetime.split('T')[0]
    
    # print article data
    print('-----------------')
    print(header)
    print(subheader)
    print(date)

    # Dictionary to be inserted into MongoDB
    post = {
        'header': header,
        'subheader': subheader,
        'date': date
    }

    

    


# In[11]:


articles = db.articles.find()
for article in articles:
    print(article)


# In[12]:


news_p = soup.body.find_all('p')

news_p


# In[13]:


soup.body.find('p').text


# In[14]:


news_title = soup.find_all("title")

news_title


# In[15]:


featured_image_url = "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA18846_ip.jpg"


# In[16]:


mars_weather = "InSight sol 445 (2020-02-26), low -92.8ºC (-135.0ºF), high -12.8ºC (8.9ºF),winds, from the SSE at 5.9 m/s (13.3 mph), gusting to 21.1 m/s, (47.3 mph),pressure at 6.30 hPa"


# In[17]:


mars_url = "https://space-facts.com/mars/"

browser.visit(url)


# In[ ]:





# In[ ]:





# In[18]:


results = soup.find_all('div', class_="widget-header")


# In[21]:


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg"},
]


# In[27]:


get_ipython().system('jupyter nbconvert --to py mission_to_mars.ipynb')


# In[ ]:




