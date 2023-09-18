from string import ascii_lowercase
from random import randint, choices


# 1. Create a list of random number of dicts (from 2 to 10).
list_of_dicts = []
num_of_dicts = randint(2, 10)

for i in range(num_of_dicts):
    # Select 3 unique random letters.
    letter_keys = choices(ascii_lowercase, k=3)
    # Create new dictionary.
    new_dict = {k: randint(0, 100) for k in letter_keys}
    # Add dictionary to the list.
    list_of_dicts.append(new_dict)

print(list_of_dicts)

# 2. Get previously generated list of dicts and create one common dict:
working_dict = {}

for i in range(len(list_of_dicts)):
    dict_num = i+1

    for key, new_value in list_of_dicts[i].items():
        if working_dict.get(key):
            working_dict[key]['occurance'] += 1
            
            old_key_value = working_dict[key]['value']

            if new_value > old_key_value:
                working_dict[key].update({'dict_num': dict_num, 'value': new_value})

        else:
            working_dict[key] = {
                'dict_num': dict_num,
                'value': new_value,
                'occurance': 1
            }

common_dict = {}

for k, v in working_dict.items():
    if v['occurance'] > 1:
        dict_num = working_dict[k]['dict_num']
        common_dict[f'{k}_{dict_num}'] = v['value']
    else:
        common_dict[k] = v['value']

print(common_dict)
