from pymongo import MongoClient
from core import config
import ssl

ssl._create_default_https_context = ssl._create_unverified_context



client = MongoClient("mongodb+srv://"+config.settings.user_name+":"+config.settings.pass_word+"@"+config.settings.host+"/myFirstDatabase?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
# client = MongoClient("mongodb+srv://pptrpw:pptrpw123@cluster0.dgmid.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)


db = client.todo_app

collection_name = db["todos_app"]
students_collection = db["students"]
courses_collection = db["courses"]
years_collection = db["years"]
