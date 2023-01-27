import json
import italian_dictionary
from italian_dictionary import exceptions


def analyze(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        file_to_analyze = json.load(file)

    # extract last word form each verse
    for poem in file_to_analyze:
        for verse in poem["sonnet_body"]:
            last_word = verse[-1].strip(",.:»;?!").split("’")[-1]
            get_rhyme(last_word)

def get_rhyme(word):
    try:
        data = italian_dictionary.get_definition(word)
        lemma = data["lemma"]
        print(lemma)
    except exceptions.WordNotFoundError:
        print(word)