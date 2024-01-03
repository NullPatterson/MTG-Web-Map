"""
Author: Nol Patterson
Date: 12/16/2023
File Name: deck_list.py
Purpose: Store a list of cards used in a deck
"""

from typing import *
from card_info import Card

class Deck:
    def __init__(self, game_format: str, commander: Card, sub_commander: Card):
        self.__game_format__ = game_format      
        self.__commander__ = commander          
        self.__sub_commander__ = sub_commander 
        self.__cards__: List[Card] = []         
        self.__colors__: List[str]= []         
        self.__price__ = commander.price
        # Determing initial Card Count/adding subcommander price
        if self.__sub_commander__ != None:
            self.__card_count__ = 2
            self.__price__ += sub_commander.price
        else: self.__card_count__ = 1
        
        
    # Getters
    @property
    def game_format(self):
        return self.__game_format__
    
    @property
    def commander(self):
        return self.__commander__
    
    @property 
    def sub_commander(self):
        return self.__sub_commander__
    
    @property
    def cards(self):
        return self.__cards__
    
    @property
    def colors(self):
        return self.__colors__
    
    @property
    def price(self):
        return f'${self.__price__}'
    
    @property
    def card_count(self):
        return self.__card_count__
    
    # Setters
    @game_format.setter
    def game_format(self, game_format: str):
        self.__game_format__ = game_format
    
    @commander.setter
    def commander(self, commander: Card):
        self.__commander__ = commander
    
    @sub_commander.setter
    def sub_commander(self, sub_commander: Card):
        self.__sub_commander__ = sub_commander
    
    @price.setter
    def price(self, addCard: bool, card: Card): 
        #if addCard is True increase the deck price, and if False decrease price
        if addCard: price += card.price
        else: price -= card.price
            
    
    # Setter to only add one cards
    @cards.setter
    def cards(self, addCard: bool, card: Card):
        #if addCard is True increase the deck price, and if False decrease price
        if addCard: self.__cards__.append(card)
        else: self.__cards__.remove(card)
        self.price(addCard, card)
    
    # Overwride function 
    @cards.setter
    def cards(self, addCard: bool, cards: List[Card]):
        #if addCard is True increase the deck price, and if False decrease price
        for card in cards:
            if addCard: self.__cards__.append(card)
            else: self.__cards__.remove(card)
            self.price(addCard, card)
