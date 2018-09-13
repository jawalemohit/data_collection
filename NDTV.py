import requests as req
from bs4 import BeautifulSoup 
import pandas as pd
import numpy as np


#NDTV
data=req.get("https://www.ndtv.com/sitemap.xml")
soup=BeautifulSoup(data.text,'xml')
#print(soup)
sitemap=[]#this is list 
for url in soup.find_all('loc'):
	sitemap.append(url.text)





data=sitemap[0]
data=req.get(data)
soup=BeautifulSoup(data.text,'xml')
#print(soup)
link=[]
for url in soup.find_all('loc'):
	link.append(url.text)



url=link[0]
r=req.get(url)
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('div',attrs={'class':'ins_storybody'})#ndtv
feresult=results[0]
feresult=feresult.find_all('p')
l1=len(feresult)

article=[]
i=0
while i<l1:
  j=0
  ndtv=feresult[i]#this is pne array of paragraph
  l=len(ndtv)
  while j<l:

    article.append(ndtv.contents[j].string)
    j=j+1
  i=i+1


article=[x for x in article if x is not None]
#print(article)

file=open("article_data","a")

for x in article:
	file.write(x)



file.close()





