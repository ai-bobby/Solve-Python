import re
from bs4 import BeautifulSoup
import requests


result=requests.get("https://conferenceindex.org/conferences/programming-languages")
soup = BeautifulSoup(result.content,'html.parser')
# print(result.status_code)
# print(soup)



# 1)
# res = soup.find('h1')
# print(res)
# print(res.text)
# print(res.text.strip())


# 2)
# res = soup.select('ul.list-unstyled li')
# for item in res:
#     print(item.text.strip())


# 4)
# res = soup.select('ul.list-unstyled li')
# data_list = list()
# for item in res:
#     text = item.text.strip()    
#     data = re.findall(r'[a-zA-Z]{3}\s\d\d',text)
#     data_list.extend(data)

# print(data_list)


# 5)
# res = soup.select('ul.list-unstyled>li>a')
# for item in res:
#     print(item['href'])