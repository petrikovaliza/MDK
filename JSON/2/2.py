import json

book = {
    "title": "Tututu",
    "author": "Papapa",
    "year_of_publication": "1683"
}

with open('book.json', 'w') as json_file:
    json.dump(book, json_file)
