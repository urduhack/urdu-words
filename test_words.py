# coding: utf8
""" Test cases """

from urduhack.urdu_characters import URDU_ALPHABETS

file_name: str = "words.txt"


def test_words():
    """ Test case"""
    handler = open(file_name, encoding="utf8")
    for word in handler:
        for character in word.strip():
            assert character in URDU_ALPHABETS, F"Incorrect word: {word} and char: {character}"
    handler.close()
