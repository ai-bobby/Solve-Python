from pymongo import MongoClient,version
import json 


class File:
    def __init__(self,file_path,file_mode):
        self.file_path = file_path
        self.file_mode=file_mode
        self.file_object = None

    
    def __enter__(self):
        self.file_object = open(self.file_path,self.file_mode)
        return self.file_object

    def __exit__(self,*exe):
        if self.file_object:
            self.file_object.close()


def read_json_file(file_path):
    try:
        with File(file_path,'r') as file_obj:
            return json.load(file_obj)
    except Exception as error:
        print(error)


# print(read_json_file('Mongodb//restaurant_Information.json'))

def connection():
    try:
        return MongoClient(host='localhost',port=27017)
    except:
        print('error connection')

def create_database(client,database_name):
    try:
        return client[database_name]
    except:
        print('error create_database')

def create_collection(db,collection_name):
    try :
        return db[collection_name]
    except:
        print('Error create_collection')


def add_resturant(collection,resturant):
    try:
        collection.insertOne(resturant)
        print('inser is successful')
    except:
        print("Error add_resturant")


 
client=connection()
db = create_database(client,'db_resturants_ads')
collection = create_collection(db,'resturant')
add_resturant(collection,{'code':1,'name':'test'})