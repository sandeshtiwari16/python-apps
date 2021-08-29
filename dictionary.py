import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("did u mean %s instead"%get_close_matches(word,data.keys())[0])
        decide=input("press y for yes or n for no: ")
        if decide=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide=="n":
            return("Word does not exist")
        else:
            return("You have entered wrong variable")
    else:
        print("Word does not exist")


word=input("Enter the word to be searched: ")
output=translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
