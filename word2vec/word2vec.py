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
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import nltk
#nltk.download('punkt')
warnings.filterwarnings(action='ignore')

# Start of added bits for testing, but will be moved to main.py after testing. maybe(?)
f = open(r"C:\Users\nolpa\Documents\GitHub\sudo-deckbuilder\word2vec\oracle-cards-20231216220200.json", errors='ignore')
oracle_cards = json.load(f)

# Iterate through each card's oracle_text
embedding_data = []
counter = 0
for card in oracle_cards:
    #print(card)
    if 'oracle_text' in card:
        text = card['oracle_text']
        if text:
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

# Creating a Graph from the CBOW model
cbow_words = []
cbow_vectors = []
for word in cbow_model.wv.index_to_key:
    cbow_words.append(word)
    cbow_vectors.append(cbow_model.wv[word])
    
# Reduceing the dimensionality of word vectors to 2d
tsne = TSNE(n_components=2, random_state=42)
cbow_2d_vectors = tsne.fit_transform(np.array(cbow_vectors))

# Creating a scatter plot
plt.figure(figsize=(20,20))
plt.scatter(cbow_2d_vectors[:, 0], cbow_2d_vectors[:, 1], c='blue', alpha=0.5)

plt.title('Magic Word Model???')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.show()

# Creating a Skip Gram Model
#sg_model = gensim.models.Word2Vec(embedding_data, min_count=1, vector_size=100, window=7, sg=1)