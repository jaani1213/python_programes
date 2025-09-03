import requests
import pandas as pd
from bs4 import BeautifulSoup

response=requests.get("https://www.mi.com/in/product-list/tv/redmi-tv/")
# print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)

# Names
names = soup.find_all('div', class_='item__info-section')
print(names)
name = []
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
print(name)


# # Images
images=soup.find_all('img',class_='mi-image__img')
image=[]
for i in images[0:10]:
    d=i["src"]
    image.append(d)
print(image) 

# # Links
links=soup.find_all('a',class_='mi-btn mi-btn--default mi-btn--normal mi-btn--light')
link=[]
for i in links[0:10]:
    d="https://www.mi.com"+i['href']
    link.append(d)
print(link)  

df=pd.DataFrame() #rows columns
# print(df)
df["Names"]=name
df["Names"]=image
df["Names"]=link
df.to_csv("MItvs.csv")