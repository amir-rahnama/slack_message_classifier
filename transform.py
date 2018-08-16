from pymongo import MongoClient
from keras.preprocessing.text import Tokenizer

client = MongoClient("localhost", 27017, maxPoolSize=50)
db = client.sc
collection = db['messages']
cursor = collection.find({})
samples = []

for document in cursor:
        samples.append(document)


tokenizer = Tokenizer(num_words=1000)
tokenizer.fit_on_texts(samples)
sequences = tokenizer.texts_to_sequences(samples)
one_hot_results = tokenizer.texts_to_matrix(samples, mode='binary')

word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))

