# liste di parole
output = []
with open("sonetti.txt", "r", encoding='utf-8') as file:
    author = None
    title = None
    sonnet_body = []
    for line in file:
        if line.startswith("@"):
            author = line.strip("@").strip()
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
print(output)