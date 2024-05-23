from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://sahiluppal2k:atlaspassword@cluster0.bpxf7y2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)#, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

db = client.list_database_names()
db = client.sqltopython.sqltopython

import pandas as pd
df = pd.read_csv("random.csv")
df.columns = ['username', 'sql_query', 'python_query', 'converted_query']

from tqdm import tqdm
for idx, item in tqdm(df.iterrows()):
    element = item.to_dict()
    element['status'] = "Pending" # Pending/Done
    db.insert_one(element)