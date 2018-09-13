import requests as req
from bs4 import BeautifulSoup 
import pandas as pd
import numpy as np

#the guardian

url=req.get("https://www.theguardian.com/sitemaps/news.xml")

soup=BeautifulSoup(url.text,'xml')

sitemap=[]

j=0;
for i in soup.find_all('loc'):
	if j%2==0:
	 sitemap.append(i.text)
	j=j+1


print(len(sitemap))
link=sitemap[70]

print(link)
link=req.get(link)
soup=BeautifulSoup(link.text,'html.parser')
result=soup.find_all('div',attrs={'class':"content__article-body from-content-api js-article__body"})
ares=result[0]
result=soup.find_all('p')

article=[]
l1=len(result)
i=0
while i<l1:
  j=0
  guard=result[i]#this is pne array of paragraph
  l=len(guard)
  while j<l:

    article.append(guard.contents[j].string)
    j=j+1
  i=i+1

headline=article[0]
article.pop(0)
article=[x for x in article if x is not None]

file=open("article_data","a")

file.write(headline)
for x in article:
	file.write(x)



file.close()






