# Developer Name :- Ravi Kumawat
# Date :- 05-12-2023
# Code :- mongo_db to csv


import csv
import pymongo
from bson.json_util import dumps, loads
# ==================== mongodb cantion ==============
con = pymongo.MongoClient(f'mongodb://localhost:27017/')
mydb = con["linkdin_data"]
conn = mydb["output_db"]

x = conn.find()
# ============= list of dict keys ==========================
csv_columns = ['_id','linkedin_id','personal_info','experience','skills','accomplishments','interests','recommendation','influencers','companies','groups','schools']
csv_file = "linkdin_data.csv"

try:
    # ============= file open and write csv fromate ==================
    with open(csv_file, 'w', encoding='utf-8', newline='') as csvfile:
        #  ================ inserst data in csv file ==========
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns,dialect='unix')
        writer.writeheader()
        # ================== date write in file ================
        for data in x:
            data.pop('_id')
            try:
                writer.writerow(data)
            except Exception as e:
                print(e)
except Exception as e:
    print("I/O error",e)
