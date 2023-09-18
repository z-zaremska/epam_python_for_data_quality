from string import ascii_lowercase
from random import randint, choices


# 1. Create a list of random number of dicts (from 2 to 10).
list_of_dicts = []
# Choose random number of dictionaries from 2 to 10.
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
        # If the key already exists in the working directory then:
        if working_dict.get(key):
            # Update number of occurrences.
            working_dict[key]['occurrence'] += 1
            
            old_key_value = working_dict[key]['value']

            # If new value is bigger than the previous one than update
            # this value and dictionary number.
            if new_value > old_key_value:
                working_dict[key].update({'dict_num': dict_num, 'value': new_value})

        else:
            # Save key, dictionary number and value in the working dictionary.
            working_dict[key] = {
                'dict_num': dict_num,
                'value': new_value,
                'occurrence': 1
            }

common_dict = {}

for k, v in working_dict.items():
    # If key occurred more than once add to the key name dictionary number.
    if v['occurrence'] > 1:
        dict_num = working_dict[k]['dict_num']
        common_dict[f'{k}_{dict_num}'] = v['value']
    else:
        common_dict[k] = v['value']

print(common_dict)
