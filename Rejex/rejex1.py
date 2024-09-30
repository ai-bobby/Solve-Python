import re

conf="""
Conference1
Topic: Object Oriented Programming
Date: 09/20/2022
Location: USA
Web: conf.usa/09/2022
Cost: $1200
Conference2
Topic:    Python3
Date: 01/31/2022
Location: France
Web: conf.france/01/2022
Cost: $6
Conference3
Topic: Data Science
Date:        07/09/2022
Location: UK
Web: conf.org
Cost: $900
Conference4
Topic: Web Development
Date: 09/29/2022
Location: Canada
Web: conf.ca
Cost: $1100
Conference5
Topic: Python for Beginners
Date: 05/09/2022
Location: Turkey
Web: confr.com/03/2022
Cost: $900000
"""


# topic_List = re.findall(r"Topic:\s*(.+)",conf)
# print(topic_List)


# data_list = re.findall(r"Date:\s*((\d\d)/\d\d/\d\d\d\d)",conf)
# print(data_list)


# Web_list = re.findall(r"Web:\s*(conf\.\w+/\d\d/2022)",conf)
# print(Web_list)

# topic_list=re.findall(r"Topic:\s*(.+)\sDate:\s*09/\d{2}/\d{4}",conf)
# print(topic_list)


newCost=re.sub(r"Cost:\s*\$\d{2,4}\s","Cost: $555\n",conf)
print(newCost)