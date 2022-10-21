from bs4 import BeautifulSoup as bs
import requests as requests
link='https://www.flipkart.com/oneplus-nord-ce-2-lite-5g-black-dusk-128-gb/product-reviews/itm7acae55b999e6?pid=MOBGDWF8GJTFAXVH&lid=LSTMOBGDWF8GJTFAXVHYFEUTE&marketplace=FLIPKART'
page=requests.get(link)
print(page)
page.content
soup=bs(page.content,'html.parser')
soup
names=soup.find_all(class_="_2sc7ZR _2V5EHH")
names
cust_names=[]
for i in range(len(names)):
    cust_names.append(names[i].get_text())
cust_names
reviews=soup.find_all(class_="t-ZTKy")
reviews
cust_reviews=[]
for i in range(len(reviews)):
    cust_reviews.append(reviews[i].get_text())
cust_reviews
#create csv file
import pandas as pd
df=pd.DataFrame()
df["names"]=cust_names
df["reviews"]=cust_reviews
df
df.to_csv("C:\\Users\\suchi\\Desktop\\python idle files\\projects\\flipkart scarpping.csv")
