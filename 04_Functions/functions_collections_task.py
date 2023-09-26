from string import ascii_lowercase
from random import randint, choices


def generate_dict():
    """Create dictionary with three random key-value pairs where
    key is a unique random lowercase letter
    and value is a random value form 0 to 100"""

    # Select 3 unique random letters.
    letter_keys = choices(ascii_lowercase, k=3)
    # Create new dictionary.
    new_dict = {k: randint(0, 100) for k in letter_keys}

    return new_dict


def generate_list_of_dicts():
    """Create a list of random number of dicts (from 2 to 10)."""
    list_of_dicts = []
    num_of_dicts = randint(2, 10)

    for i in range(num_of_dicts):
        # Add dictionary to the list.
        list_of_dicts.append(generate_dict())

    return list_of_dicts


def create_tracking_dictionary():
    """
    Transforms given list of dictionaries and create one common dictionary
    that tracks number of occurrences of one key, saves
    key maximum value noticed and matching dictionary number.
    """
    list_of_dictionaries = generate_list_of_dicts()
    tracking_dict = {}

    for i in range(len(list_of_dictionaries)):
        dict_num = i + 1

        for key, new_value in list_of_dictionaries[i].items():
            # If the key already exists in the working directory then:
            if tracking_dict.get(key):
                # Update number of occurrences.
                tracking_dict[key]['occurrence'] += 1
                old_key_value = tracking_dict[key]['value']

                # If new value is bigger than the previous one than update
                # this value and dictionary number.
                if new_value > old_key_value:
                    tracking_dict[key].update(
                        {'dict_num': dict_num, 'value': new_value})

            else:
                # Save key, dictionary number and value in the tracking dictionary.
                tracking_dict[key] = {
                    'dict_num': dict_num,
                    'value': new_value,
                    'occurrence': 1
                }

    return tracking_dict


def create_common_dictionary():
    """
    Returns restructured tracking dictionary according to the following rules:
    1. If the key have occurred more than once then rename this key that it
    holds the information about the dictionary number with the biggest value.
    2. If the ket have occurred only once then leave it as it is.
    """

    tracking_dict = create_tracking_dictionary()
    common_dict = {}

    for k, v in tracking_dict.items():
        # If key occurred more than once add to the key name dictionary number.
        if v['occurrence'] > 1:
            dict_num = tracking_dict[k]['dict_num']
            common_dict[f'{k}_{dict_num}'] = v['value']
        else:
            common_dict[k] = v['value']

    return common_dict


common_dictionary = create_common_dictionary()
print(common_dictionary)
