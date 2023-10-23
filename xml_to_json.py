import xmltodict    #========= import library
import requests     #========= import library
import json         #========= import library

url = "" #========= pass url

request = requests.get(url=url)
data = request.text         # ===== chaque response in text


json_dtas = xmltodict.parse(data)['urlset']['url']  #========= json seletour
dict ={}
for json_dta in json_dtas:
    dict['urll'] = json_dta['loc']
    dict['date'] = json_dta['lastmod']

    print(json.loads(dict))

