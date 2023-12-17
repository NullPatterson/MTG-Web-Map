"""
Author: Nol Patterson
Date: 12/16/2023
File Name: card_info.py
Purpose: Define a Card Class to store all the info about a particular card
"""

class Card():
    def __init__(self, name, lang, mana_cost, cmc, type_line, oracle_text, 
                 colors, color_identity, keywords, legalities, price):
        self.__name__ = name
        self.__lang__ = lang
        self.__mana_cost__ = mana_cost
        self.__cmc__ = cmc
        self.__type_line__ = type_line
        self.__oracle__ = oracle_text
        self.__colors__ = colors
        self.__color_identity__ = color_identity
        self.__keywords__ = keywords
        self.__legalities__ = legalities
        self.__price__ = price   
        