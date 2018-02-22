print ("Welcome to Interactive Dictionary")
import json
from difflib import get_close_matches

dataset = json.load(open("data.json")) #Loading dataset

def translator(word):
    word = word.lower() #changing word into lower case
    if word in dataset:
        return dataset[word]
    elif len(get_close_matches(word, dataset.keys())) > 0: #Returning the closest match for the wrong word entered
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, dataset.keys())[0])
        if yn == "Y":
            return dataset[get_close_matches(word, dataset.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter the word: ")
output = translator(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
