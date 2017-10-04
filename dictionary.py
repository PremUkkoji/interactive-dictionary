import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def getDefinition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        response = input("Did you mean %s instead ? Press Y for yes or N for no : " % get_close_matches(word, data.keys())[0])
        if response.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif response.lower() == "n":
            return "This word doesn't exists. Check it once more !"
        else:
            return "I'm not sure I Understand"
    else:
        return "This word doesn't exists. Check it once more !"


word = input("Enter word = ")
output = getDefinition(word)

if type(output) is list:
    i = 1
    for item in output:
        print(i, ". ", item)
        i+=1
else:
    print(output)
