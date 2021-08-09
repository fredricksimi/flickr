from ast import literal_eval
with open('ourdata.json') as fileobj:
    for line in fileobj:
        new_line = line.strip()
        alaa = literal_eval(new_line)
        new_file = open('links.txt', 'a')
        new_file.write(f"{alaa['image_url']}\n")
new_file.close()