"""
Author: Nol Patterson
Date: 12/16/2023
File Name: deck_list.py
Purpose: Store a list of cards used in a deck
"""

class Deck:
    def __init__(self, game_format, commander, sub_commander):
        self.__game_format__ = game_format
        self.__commander__ = commander
        self.__sub_commander__ = sub_commander
        self.__cards__ = []
        self.__colors__ = []
        