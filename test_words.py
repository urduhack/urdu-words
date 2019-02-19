# coding: utf8
""" Test cases """
import pickle

from urduhack import normalize
from urduhack.urdu_characters import URDU_ALPHABETS

file_name: str = "words.txt"
file_bigram_name: str = "bigram_words.txt"
file_trigram_name: str = "trigram_words.txt"


def test_words():
    """ Test case"""
    handler = open(file_name, encoding="utf8")
    for word in handler:
        for character in word.strip():
            if character is '_':
                continue
            assert character in URDU_ALPHABETS, F"Incorrect word: {word} and char: {character}"
    handler.close()


def test_bigram_words():
    """ Test case"""
    handler = open(file_bigram_name, encoding="utf8")
    for word in handler:
        for character in word.strip():
            if character is '_':
                continue
            assert character in URDU_ALPHABETS, F"Incorrect word: {word} and char: {character}"
    handler.close()


def test_trigram_words():
    """ Test case"""
    handler = open(file_trigram_name, encoding="utf8")
    for word in handler:
        for character in word.strip():
            if character is '_':
                continue
            assert character in URDU_ALPHABETS, F"Incorrect word: {word} and char: {character}"
    handler.close()


def sorted_words():
    """Sorted the words.txt file"""
    handler = open(file_name, encoding="utf8")
    words_set = set()
    for word in handler:
        word = normalize(word.strip())
        word = '_'.join(word.split())
        words_set.add(word.strip())
    handler.close()
    print(F"Total words: {len(words_set)}")

    words_set = sorted(words_set)
    with open(file_name, 'w', encoding="utf8") as the_file:
        for word in words_set:
            the_file.write(word + '\n')


def duplicate_words():
    """ find duplicate words"""
    words_dict = {}
    handler = open(file_name, encoding="utf8")
    for word in handler:

        inner_handler = open(file_name, encoding="utf8")
        inner_list = []
        for inner_word in inner_handler:
            if word.strip() in inner_word.strip():
                inner_list.append(inner_word.strip())

        inner_handler.close()

        if inner_list:
            words_dict[word.strip()] = inner_list

    handler.close()

    with open('words.dict', 'wb') as fp:
        pickle.dump(words_dict, fp)


def load_pkl():
    """Load the save dict file"""

    with open('words.dict', 'rb') as fp:
        word_dict = pickle.load(fp)

    for key, values in word_dict.items():
        print("=" * 50)
        print(key)
        print(values)
