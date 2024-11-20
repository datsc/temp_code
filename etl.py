import pymongo

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

pg = create_engine('postgres://postgres@postgresdb:5432')
pg.execute('''CREATE TABLE IF NOT EXISTS sentences (
    text VARCHAR(512),
    sentiment NUMERIC
);
''')

client = pymongo.MongoClient("mongodb://mongodb:27017/")
db = client.sentences


def read_sentence_from_mongo():
    
    sentence = list(db.collections.sentences.find())
    
    s = random.choice(sentences)
        
    return s
