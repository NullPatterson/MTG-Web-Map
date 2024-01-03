"""
Author: Nol Patterson
Date: 1/3/2024
File Name: card_info.py
Purpose: Define a Card Class to store all the info about a particular card
"""

from typing import *

class Card:
    def __init__(self, name: str, lang: str, mana_cost: str, cmc: int, type_line: str, oracle_text: str, uid: str, 
                 colors: str, color_identity: List[str], keywords: List[str], legalities: List[List[str], List[str]], price: int):
        self.__name__ = name
        self.__lang__ = lang
        self.__mana_cost__ = mana_cost
        self.__cmc__ = cmc
        self.__type_line__ = type_line
        self.__oracle__ = oracle_text
        self.__uid__ = uid
        self.__colors__ = colors
        self.__color_identity__ = color_identity
        self.__keywords__ = keywords
        self.__legalities__ = legalities
        self.__price__ = price   
        
    
    # Getters
    @property
    def name(self):
        return self.__name__
        
    @property
    def lang(self):
        return self.__lang__
    
    @property
    def mana_cost(self):
        return self.__mana_cost__
    
    @property
    def cmc(self):
        return self.__cmc__
    
    @property
    def type_line(self):
        return self.__type_line__
    
    @property
    def oracle(self):
        return self.__oracle__
    
    @property
    def uid(self):
        return self.__uid__
    
    @property
    def colors(self):
        return self.__colors__
    
    @property
    def color_identity(self):
        return self.__color_identity__
    
    @property
    def keywords(self):
        return self.__keywords__
    
    @property
    def legalities(self):
        return self.__legalities__
    
    @property
    def price(self):
        return self.__price__
    
    # Setters
    # For the time being there will only be setters for keywords, legalities, and price as these are the only ones
    # That I expect change from in the foreseeable future
    @keywords.setter
    def keywords(self, words):
        self.__keywords__ = words
    
    @legalities.setter
    def legalities(self, legalities):
        self.__legalities__ = legalities
    
    @price.setter
    def price(self, price):
        self.__price__ = price