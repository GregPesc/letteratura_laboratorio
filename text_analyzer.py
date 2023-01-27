import json

import italian_dictionary
import pyphen
from italian_dictionary import exceptions


def analyze(file_name) -> None:
    """
    Extracts wanted data from json file
    """
    with open(file_name, "r", encoding="utf-8") as file:
        file_to_analyze = json.load(file)

    # extract last word form each verse
    last_syllables = []
    analysis = []
    for poem in file_to_analyze:
        author = poem["author"]
        for verse in poem["sonnet_body"]:
            last_word = verse[-1].strip(",.:»;?!").split("’")[-1]
            last_syllables.append(divide_into_syllables(last_word))
        analysis.append({"author": author, "last_syllables": last_syllables})

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
            lemmi = lemma.strip(" ").split(",")
            for x in lemmi:
                return get_last_syllable(x)
        return get_last_syllable(lemma)

    except exceptions.WordNotFoundError:
        dic = pyphen.Pyphen(lang="it-IT")
        word = dic.inserted(word)
        return word


def get_last_syllable(lemma) -> str:
    print(f"Lemma: {lemma}")
    last_syllable = []
    last_syllable.clear()
    for i in lemma:
        if i in ('à', 'á', 'è', 'é', 'ì', 'í', 'ó', 'ò', 'ù', 'ú'):
            last_syllable.clear()
            last_syllable.append(i)
        else:
            last_syllable.append(i)
    last_syllable = ''.join(last_syllable)
    print(f"Last syllable: {last_syllable}")
    return last_syllable
