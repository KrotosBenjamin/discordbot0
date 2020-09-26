import datetime
import pymongo

client = pymongo.MongoClient("mongodb+srv://kjbenjamin90:cd0n%265_0%249gB@pokeball-0.jjroz.mongodb.net/discordbot0")
   
def save_data_to_mongo(data):
    db = client["discordbot0"]
    collection = db["test_data"]
    response = collection.insert_one(data)

if __name__ == "__main__":
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {}
    data["text"] = "Hello World"
    data["date_time"] = date_time
    save_data_to_mongo(data)
