import json



def extract(analysis):
    rhymes = {}
    for poem in analysis:
        for syllable in poem["last_syllables"]:
            if '-' in syllable:
                continue
            if syllable not in rhymes.keys():
                rhymes.update({syllable: 1})
            else:
                rhymes.update({syllable: rhymes.get(syllable)+1})
    
    # rhymes = sorted(rhymes.items(), key=lambda x:x[1])
    print(f"\n\nRIME\n{rhymes}")

    words = {}
    with open("parsed_file.json", "r", encoding="utf-8") as file:
        file_to_analyze = json.load(file)
    
    for poem in file_to_analyze:
        for verse in poem["sonnet_body"]:
            for word in verse:
                if word not in words.keys():
                    words.update({word: 1})
                else:
                    words.update({word: words.get(word)+1})
    # words = sorted(words.items(), key=lambda x:x[1])
    print(f"\n\nPAROLE{words}")