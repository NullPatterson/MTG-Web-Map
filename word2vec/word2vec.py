"""
Author: Nol Patterson
Date: 1/3/2024
File Name: word2vec.py
Purpose: Generate a word2vec graph of oracle text
"""

from gensim.models import Word2Vec
import gensim 
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import json

warnings.filterwarnings(action='ignore')

# Start of added bits for testing, but will be moved to main.py after testing. maybe(?)
f = open('oracle-cards-20231216220200.json')
oracle_cards = json.load(f)

# Iterate through each card's oracle_text
embedding_data = []
for text in oracle_cards['oracle_text']:
    text = text.replace("\n", " ") # Replace escape caharacter with space
    #Iterate through each sentence
    for i in sent_tokenize(text):
        temp = []

        # tokenize the sentence into words
        for j in word_tokenize(i):
            temp.append(j.lower())
        embedding_data.append(temp)

# Creating a CBOW model
cbow_model = gensim.models.Word2Vec(embedding_data, min_count=1, vector_size=100, window=7)

# Creating a Skip Gram Model
sg_model = gensim.models.Word2Vec(embedding_data, min_count=1, vector_size=100, window=7, sg=1)