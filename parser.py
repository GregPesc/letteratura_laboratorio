# liste di parole
import json


# parse input file
def parse_file(file_name):
    output = []
    with open(file_name, "r", encoding='utf-8') as file:
        author = None
        title = None
        sonnet_body = []
        for line in file:
            if line.startswith("@"):
                author = line.strip("@").split(",")[0]
            elif line.startswith("#"):
                if title:
                    sonnet_body = list(filter(None, sonnet_body))
                    output.append({
                        "author": author,
                        "title": title,
                        "sonnet_body": sonnet_body
                    })
                    sonnet_body = []
                title = line.strip("#").strip()
            else:
                sonnet_body.append(line.strip().split())

        sonnet_body = list(filter(None, sonnet_body))
        output.append({
            "author": author,
            "title": title,
            "sonnet_body": sonnet_body
        })
        save_file(output)


# save parsed input
def save_file(output):
    with open("parsed_file.json", "w") as file:
        json.dump(output, file)
