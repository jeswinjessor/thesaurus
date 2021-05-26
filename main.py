import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def translate(word):        # function to find the word from a json file
    word = word.lower()     # if the entered word have any uppercase letters it will change it in to lower
    if word in data:
        return data[word]   # will pull out the data Correspondent to the word
    elif word.title() in data:      # some of the keys are starting with caps like nouns so...
        return data[word.title()]
    elif word.upper() in data:      # some of the keys are all caps like USA so...
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:     # checking if we have the mathces in the json 
        ans = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])      #  getting the most suitable match [0 ] from the result which is also a list
        if ans == "Y" or ans == "y":    # making sure the user typed in the right word
            return data[get_close_matches(word, data.keys())[0]]        # if yes, print the result
        elif ans == "N" or ans == "n":  # making sure the user typed in the wrong word
            return "The word does not exist."   # if no, print the message
        else:
            return "We didn't understand your query" # for letters other than y and n
    else:                   # will give a message if the entered word does not exist
        return "The word does not exist. Please double check it"


word = input("Enter word: ")

output = translate(word)    # saving the output to a variable so we can play around
if type(output) == list:    # checking if the output is the result or message
    for item in output:     # if yes then
        print(item)
else:
    print(output)