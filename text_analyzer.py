import json
from copy import deepcopy

import italian_dictionary
import pyphen
from italian_dictionary import exceptions


def analyze(file_name):
    """
    Extracts wanted data from json file
    """
    with open(file_name, "r", encoding="utf-8") as file:
        file_to_analyze = json.load(file)

    # extract last word form each verse
    analysis = []
    for poem in file_to_analyze:
        last_syllables = []
        author = poem["author"]
        for verse in poem["sonnet_body"]:
            last_word = verse[-1].strip(",.:»;?!").split("’")[-1]
            last_syllable = divide_into_syllables(last_word)
            last_syllables.append(last_syllable)
        mydict = {"author": author, "last_syllables": last_syllables}
        analysis.append(deepcopy(mydict))
        last_syllables.clear()

    with open(file="analysis.json", mode="w", encoding="utf-8") as file:
        json.dump(analysis, file)


def divide_into_syllables(word) -> str:
    """
    Divides into syllables
    """
    try:
        data = italian_dictionary.get_definition(word)
        lemma = data["lemma"]
        if "," in lemma:
            lemma = lemma.strip(" ").split(",")[0]
        return get_last_syllable(lemma)

    except exceptions.WordNotFoundError:
        dic = pyphen.Pyphen(lang="it-IT")
        word = dic.inserted(word)
        # print(f"Word: {word}")
        return word


def get_last_syllable(lemma) -> str:
    # print(f"Lemma: {lemma}")
    last_syllable = []
    last_syllable.clear()
    for i in lemma:
        if i in ('à', 'á', 'è', 'é', 'ì', 'í', 'ó', 'ò', 'ù', 'ú'):
            last_syllable.clear()
            last_syllable.append(i)
        else:
            last_syllable.append(i)
    last_syllable = ''.join(last_syllable)
    # print(f"Last syllable: {last_syllable}")
    return last_syllable
