import json
import string
with open ("dictionary.json") as file:
    dictionary = json.load(file)


def reverse_dict(dictionary):
    keys = dictionary.keys()
    values = dictionary.values()
    new_keys = []
    new_values = []
    new_dictionary = {}
    
    for category in values: #Get all the values into an array
        for item in category:
            new_values.append(item)
    
    for category in keys: #Get all the keys into an array
        for item in dictionary[category]:
            new_keys.append(category)
    
    for value in new_values:
        new_dictionary[value] = new_keys[new_values.index(value)]
    return new_dictionary
    
print str(reverse_dict(dictionary))