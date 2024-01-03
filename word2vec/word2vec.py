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

warnings.filterwarnings(action='ignore')