import requests
import re
from bs4 import BeautifulSoup

class Mobile:
    def __init__(self,title,img,price):
        self.title = title
        self.img = img
        self.price = price
        
    def __str__(self):
        return f"{self.title}\t{self.img}\t{self.price}"
#----------------------------------------------------------
mobile_list=[]
for i in range(1,6):
    result=requests.get("https://www.technolife.ir/product/list/69_800_801/%D8%AA%D9%85%D8%A7%D9%85%DB%8C-%DA%AF%D9%88%D8%B4%DB%8C%E2%80%8C%D9%87%D8%A7?keywords=&sort=order-desc&page="+str(i))
    soup=BeautifulSoup(result.content,"html.parser")
    res=soup.find_all("li",attrs={"class": "ProductPrlist_product__3oA2g"})

    for mobile in res:
        imgSrc=mobile.a.figure.img["src"]
        title=re.findall("<strong>(.*)</strong>",str(mobile))[0]  
        price=re.sub(r",","",mobile.section.div.span.text.strip())
        m=Mobile(title,imgSrc,price)
        mobile_list.append(m)
    
    for mobile in  mobile_list:
        print(mobile) 

    print("=========================================================")