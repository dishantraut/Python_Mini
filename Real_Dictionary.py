"""
Download 'data.json' file before running the program
Its a Dictionary that takes words as input from user and give meaning as the output

"""
import json
from difflib import get_close_matches

db = json.load(open("data.json"))

def dict1(w):
    if w in db:
        return db[w]
    elif len(get_close_matches(w, db.keys())) > 0:
        yn = input("Do you mean %s instead? Enter Y if yes, N if no: " % get_close_matches(w, db.keys())[0])
        if yn == "Y":
            return db[get_close_matches(w, db.keys())[0]]
        elif yn == "N":
            return "The word does not exist. Please check it again."
        else:
            return "You are hard to understand."
    else:
        return "The word does not exist. Please check it again."


word = input("Enter Keyword: ")
output = dict1(word)
if type(output) == list:
    for items in output:
        print(items)
else:
    print(output)