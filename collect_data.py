import pymongo

client = pymongo.MongoClient("mongodb://mongodb:27017/")
db = client.fake_data


sentence = {"id": "uu", "sentence_content":"Hello Students"}

db.collections.data_science.insert_one(sentence)
