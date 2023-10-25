
# Developer Name :- Ravi Kumawat
# Date :- 24-10-2023
# Code :- To read any image in our Pc

import os
from datetime import datetime

from bs4 import BeautifulSoup
import requests
#

current_path = os.getcwd()
current_date = "\\" + str(datetime.now()).split(" ")[0].replace("-","_")

path = current_path+current_date
try:
    os.mkdir(path)
except Exception as e:
    print(e)

urls= ['https://baccabucci.com/products/copy-of-bacca-bucci-hypersoft-series-with-ultra-rebounce-outsole-iconic-breathable-engineered-knit-upper-running-shoes',"https://baccabucci.com/products/bacca-bucci-stunner-hi-top-streetwear-sneakers-with-360-degree-cushioning-2","https://baccabucci.com/products/bacca-bucci-spark-running-shoes-trainers-for-men"]
num = 1
for url in urls:
    page = requests.get(url)

    text = page.content

    soup = BeautifulSoup(text, "html.parser")

    with open(f"{path}\\{num}.html", "w", encoding = 'utf-8') as file:
        file.write(str(soup.prettify()))
        print(f"page save {num}")
        num+=1
