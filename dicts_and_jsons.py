import json

l1 = 'all_letters/Letter  1_On saving time.txt'
with open(l1, 'r') as fo:
    letter_1 = fo.read()

letters_dict = {}
letters_dict['letter 1'] = letter_1


fn = 'practice data/practice_dict.json'
with open(fn, 'w') as fo:
    json.dump(letters_dict, fo)