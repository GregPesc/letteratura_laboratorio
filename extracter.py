import json


def extract_rhymes(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        analysis = json.load(file)
    # write a function to count the frequency of each rhyme
    rhymes = {}
    for poem in analysis:
        for syllable in poem["last_syllables"]:
            if syllable not in rhymes.keys():
                rhymes.update({syllable: 1})
            elif syllable in rhymes.keys():
                rhymes.update({syllable: rhymes.get(syllable) + 1})

    rhymes = sorted(rhymes.items(), key=lambda x:x[1], reverse=True)
    return rhymes


def extract_words(file_name):
    words = {}
    with open(file_name, "r", encoding="utf-8") as file:
        file_to_analyze = json.load(file)
    for poem in file_to_analyze:
        for verse in poem["sonnet_body"]:
            for word in verse:
                if word not in words.keys():
                    words.update({word: 1})
                else:
                    words.update({word: words.get(word) + 1})
    words = sorted(words.items(), key=lambda x:x[1], reverse=True)
    return words
