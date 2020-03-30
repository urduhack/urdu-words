# coding: utf8
""" Test cases """
import pickle

from urduhack import normalize
from urduhack.urdu_characters import URDU_ALPHABETS

file_name: str = "words.txt"
file_bigram_name: str = "bigram_words.txt"
file_trigram_name: str = "trigram_words.txt"
location_file: str = "ner/locations.txt"
person_file: str = "ner/persons.txt"
organization_file: str = "ner/organizations.txt"


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


def test_locations():
    """Test Case"""
    with open(location_file, "r") as file:
        for word in file:
            word = word.strip()
            for char in word:
                if char is " ":
                    continue
                assert char in URDU_ALPHABETS, f"Incorrect word: {word} and char: {char}"


def test_persons():
    """Test Case"""
    with open(person_file, "r") as file:
        for word in file:
            word = word.strip()
            for char in word:
                if char is " ":
                    continue
                assert char in URDU_ALPHABETS, f"Incorrect word: {word} and char: {char}"


def test_organizations():
    """Test Case"""
    with open(organization_file, "r") as file:
        for word in file:
            word = word.strip()
            for char in word:
                if char is " ":
                    continue
                assert char in URDU_ALPHABETS, f"Incorrect word: {word} and char: {char}"


def test_ner_duplicates():
    """Test Case"""
    locations = []
    persons = []
    organizations = []
    with open(location_file, "r") as loc_file, open(person_file, "r") as per_file, open(
            organization_file, "r") as org_file:
        for word in loc_file:
            word = word.strip()
            locations.append(word)
        for word in per_file:
            word = word.strip()
            persons.append(word)
        for word in org_file:
            word = word.strip()
            organizations.append(word)

    for word in locations:
        assert word not in organizations
        assert word not in persons

    for word in persons:
        assert word not in locations
        assert word not in organizations

    for word in organizations:
        assert word not in persons
        assert word not in locations