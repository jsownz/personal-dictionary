#!/usr/bin/env python

"""
    Author: John Vardanian
    Last Modified: 2016-06-22
    Python3.5 using PyCharm / Atom / Sublime Text 3

    r0.1.11-2016.06.22(a)

    Generate a dictionary list as a text file using permutations of terms
    delimited by a comma. Terms are intended to be accumulated during
    information gathering phase of a penetration test. The more relevant the
    terms, the higher chance of success.

    NOTE: Currently arguments are not validated. See 'README.md' for more.
"""

import itertools
import shlex
import argparse
import json


def number_swap(term):
    """
        Replace numeric chars within a string with common substitutions of
        letters, spelling, and symbols.

        :param term: numeric string
        :return: list of argument 'term' variations with number substitutions
        :rtype: list
    """
    number_alt_dict = {
        '0': ['O'],
        '1': ['l'],
        '2': ['Z'],
        '3': ['E'],
        '4': ['A'],
        '5': ['S'],
        '6': ['b', 'G'],
        '7': ['T', 'L'],
        '8': ['B'],
        '9': ['g', 'q']
    }
    new_terms = []
    marker = 0
    while marker < len(term):
        number_list = list(term)
        if number_list[marker] in number_alt_dict:
            for replace in number_alt_dict[number_list[marker]]:
                number_list[marker] = replace
                new_terms.append(''.join(number_list))
        marker += 1

    return new_terms


def letter_swap(term):
    """
        Replace alpha chars within a string with common substitutions of
        numbers and symbols.

        :param term: string of letters
        :return: list of argument 'term' variations with letter substitutions
        :rtype: list
    """
    term = term.lower()
    letter_alt_dict = {
        'a': ['@', '4'],
        'b': ['8'],
        'c': ['('],
        'e': ['3'],
        'g': ['6', '9'],
        'h': ['#'],
        'i': ['!'],
        'l': ['1'],
        'o': ['0'],
        's': ['5', '$'],
        't': ['+', '7'],
        'z': ['2']
    }
    new_terms = []
    marker = 0
    while marker < len(term):
        letter_list = list(term)
        if letter_list[marker] in letter_alt_dict:
            for replace in letter_alt_dict[letter_list[marker]]:
                letter_list[marker] = replace
                new_terms.append(''.join(letter_list))
        marker += 1

    return new_terms


def alternate_case(term, first):
    """
        Change case to alternate_case between lower and upper; if first is true
        begin with the fist char in caps.

        :param term: string of letters to permute
        :param first: boolean true if first letter is cased upper
        :return: string 'term' with letters alternating upper/lower case
        :rtype: string
    """
    new_string = ""
    for letter in term:
        if first:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
        if letter != ' ':
            first = not first
    return new_string


def permute_phone(phone):
    """
        Return list of various phone permutations (area code, reversed etc).

        :param phone: string of 10 digits
        :return: list of 'phone' number permutations
        :rtype: list
    """
    return [
        phone,
        phone[3:],
        phone[0:3],
        phone[6:],
        phone[::-1],
        reverse_string(phone[0:3])] + \
        number_swap(phone)


def permute_casing(term):
    """
        Return list of term with title case, all lower, and all upper.

        :param term: string of letters
        :return: list of 'term' with variations using 2 common casing styles
        :rtype: list
    """
    return [
        term.lower(),
        term.capitalize()
    ]


def permute_year(year):
    """
        Return list of common year perms. (last 2 digits, backwards, etc).

        :param year: string of 4 digits
        :return: list of 'year' using 4 common styles
        :rtype: list
    """
    return [
        year[2:],
        year,
        year[::-1]] + \
        number_swap(year)


def reverse_string(term):
    """
        Return string in reverse.

        :param term: string of any character type
        :return: string of 'term' after being reversed
        :rtype: string
    """
    return term[::-1]


def permute_zip_code(zip_code):
    """
        Return list of string zip_code with 3 variations.

        :param zip_code: string of 5 digits
        :return: list of 3 common permutation styles for zip codes
        :rtype: list
    """
    return [
        reverse_string(zip_code)] + \
        number_swap(zip_code) + \
        [zip_code]


def permute_music(music):
    """
        Return common permutations of music related terms.

        :param music: string of music related term
        :return: list of 5 common permutations of generic terms
        :rtype: list
    """
    return \
        permute_casing(music) + \
        [reverse_string(music)] + \
        [alternate_case(music, True)] + \
        [alternate_case(music, False)] + \
        letter_swap(music)


def perm_st_num(street_number):
    """
        Return common permutations of street numbers.

        :param street_number: string of any number of digits
        :return: list of 'street_number' with 3 common permutation styles
        :rtype: list
    """
    return [
        street_number,
        reverse_string(street_number)] + \
        number_swap(street_number)


def mangle(target_list):
    """
        Return a list containing most frequently used permutation functions

        :param target_list: generic string, typically only letters
        :return: list of 5 common permutations of all terms in 'target_list'
        :rtype: list
    """
    mangled_list = []
    for item in target_list:
        mangled_list.extend(letter_swap(item))
        mangled_list.extend(permute_casing(item))
        mangled_list.append(alternate_case(item, True))
        mangled_list.append(alternate_case(item, False))
    return mangled_list


def store_info(prompt):
    """
        Return list of items exploded by char ',' and trimmed of whitespace.
        Spaces are replaced by commas to treat multi word entries as separate
        words.

        :param prompt: to be displayed to user for input
        :return: list stored after changing spaces to commas, exploding, trim
        :rtype: list
    """
    user_input = input(prompt + ": ")
    user_input = ','.join(shlex.split(user_input))
    return [x.strip() for x in user_input.split(',')]


def main():
    """
        ** All code below currently for testing and proof of concept **

        TODO: Rewrite logic of final dictionary generation after completing
            and expanding upon algorithms above.

        Generate personalized dictionary list of passwords, tailored towards a
        target with information gathered during initial phase of pen test.
    """
    print("\n** Personalized Dictionary Generator ** \n\nEnter words in the " +
          "prompts below, separated with commas.\nE.G. Phones: " +
          "5555555555, 9995550000\n\nEach category is similar to that of a " +
          "security question to recover a password, or a topic that is " +
          "commonly used by individuals to remember a password. Enter terms " +
          "of greater relevance towards the beginning of each prompt. " +
          "When the script completes a file titled 'dictionary.txt' " +
          "will be generated in the same directory as the script. The " +
          "dictionary will contain a large number of permutations of the " +
          "information entered.\n\nThe more relevant information entered " +
          "the higher chance of success, as the significance determines " +
          "the quality of the dictionary that is generated.\nTo be used "
          "only for authorized testing.\n\nLarge amounts of information may " +
          "take several minutes.\n\n")

    # list to hold all passwords after processing
    final_collection = []

    # user sets pw and list length parameters
    parser = argparse.ArgumentParser(description='Generate password file.')
    parser.add_argument('--min', type=int, required=True, help='Minimum password length')
    parser.add_argument('--max', type=int, required=True, help='Maximum password length')
    parser.add_argument('-n', '--num', type=int, required=True,
                        help='Number of passwords to be generated')
    parser.add_argument('-f', '--file', required=True, help='Criteria file')
    args = parser.parse_args()
    min_length = args.min
    max_length = args.max
    password_count = args.num

    try:
        criteria = json.loads("".join(open(args.file, "r").readlines()))
    except FileNotFoundError as e:
        print("Could not open criteria file: %s" % e)
        exit(1)

    print("\nPlease wait while your dictionary is generated... This may " +
          "take several minutes.\n")

    # use function 'mangle' for most common permutation, typically alpha only
    pets = mangle(criteria["pets"]) if criteria["pets"] else []
    sports = mangle(criteria["sports"]) if criteria["sports"] else []
    family = mangle(criteria["family"]) if criteria["family"] else []
    music = mangle(criteria["music"]) if criteria["music"] else []
    states = mangle(criteria["states"]) if criteria["states"] else []
    cities = mangle(criteria["cities"]) if criteria["cities"] else []
    schools = mangle(criteria["schools"]) if criteria["schools"] else []
    colors = mangle(criteria["colors"]) if criteria["colors"] else []
    streets = mangle(criteria["street_numbers"]) if criteria["streets"] else []
    other = mangle(criteria["other"]) if criteria["other"] else []
    jobs = mangle(criteria["employment"]) if criteria["employment"] else []

    zip_codes = criteria["zip_codes"] if criteria["zip_codes"] else []
    phone_numbers = criteria["phone"] if criteria["phone"] else []

    # lists that don't make use of function 'mangle'
    phones = []
    years = []
    zips = []
    street_nums = []

    # populate lists that don't use function 'mangle'
    for phone in criteria["phone"]:
        phones.extend(permute_phone(phone))

    for year in criteria["years"]:
        years.extend(permute_year(year))

    for zip_code in criteria["zip_codes"]:
        zips.extend(permute_zip_code(zip_code))

    for street_number in criteria["street_numbers"]:
        street_nums.extend(perm_st_num(street_number))

    # add phone number to top of list
    final_collection[:0] = phones

    # lists to permute for base passwords
    collections = [
        pets,
        family,
        sports,
        schools,
        cities,
        music,
        states,
        jobs,
        streets,
        colors,
        other
    ]

    # permute collections to combine 2 of every list from collections
    combinations = []
    list_count = len(collections)
    marker = 0
    while marker < list_count:
        for list_portion in collections[(marker + 1):]:
            for item in collections[marker]:
                combinations.append(item)
            variations = list(
                itertools.product(collections[marker], list_portion))
            for term_one, term_two in variations:
                combinations.append(term_one + term_two)
                combinations.append(term_two + term_one)
        marker += 1

    # permute category 'other' against itself
    length = len(other)
    marker = 0
    while marker < length:
        for item in other[marker:]:
            combinations.append(other[marker] + item)
            combinations.append(item + other[marker])
        marker += 1

    # add suffix of additional common variations to existing combinations
    final_suffix = []
    for word in combinations:

        # add generic numeric and special chars
        final_suffix.append(word + "!")
        final_suffix.append(word + "1")
        final_suffix.append(word + "123")

        for year in years:
            final_suffix.append(word + year)

        for zip_code in zip_codes:
            final_suffix.append(word + zip_code)

        for street_number in street_nums:
            final_suffix.append(word + street_number)

        # append area code from phone numbers to base words
        for phone in phone_numbers:
            final_suffix.append(word + phone[0:3])

    # remove duplicates and combine lists of words meeting length requisites
    final_collection.extend(combinations + final_suffix)
    collection = list(set(final_collection))
    collection = [word for word in collection if
                  max_length >= len(word) >= min_length]

    # pending algorithm - sorting process to push probable passwords higher
    numeric = []
    alpha_lower = []
    alpha_mixed_case = []
    alpha_numeric_lower = []
    alpha_numeric_mixed_case = []
    special_chars = []

    for item in collection:
        if item.isdigit():
            numeric.append(item)
        elif item.isalpha() and (
            item.islower() or (
                item[0].isupper() and item[1:].islower())):
            alpha_lower.append(item)
        elif item.isalpha():
            alpha_mixed_case.append(item)
        elif item.isalnum() and item.islower():
            alpha_numeric_lower.append(item)
        elif item.isalnum():
            alpha_numeric_mixed_case.append(item)
        else:
            special_chars.append(item)

    final_collection = numeric
    final_collection.extend(alpha_lower)
    final_collection.extend(list(
        itertools.chain.from_iterable(
            zip(alpha_numeric_lower, alpha_mixed_case))))
    final_collection.extend(alpha_numeric_mixed_case)
    final_collection.extend(special_chars)

    # create list of words with length specified by user
    count = 0
    with open('dictionary.txt', 'w+') as my_file:
        for word in final_collection:
            if count == password_count:
                break
            my_file.write(word + '\n')
            count += 1

    print("Dictionary list generation complete. File is \"dictionary.txt\"" +
          " in script directory.")

if __name__ == "__main__":
    main()
