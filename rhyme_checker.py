import json


def rhyme_check():
    with open("parsed_file.json", "r") as file:
        file_to_analyze = json.load(file)

    # temp
    for poem in file_to_analyze:
        author = poem["author"]
        title = poem["title"]
        print(f"{author}\n{title}\n\n")
