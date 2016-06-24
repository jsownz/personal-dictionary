#!/usr/bin/env python

"""
    Author: John Vardanian
    Last Modified: 2016-06-24
    Python3.5 using PyCharm / Atom / Sublime Text 3

    r0.1.3-2016.06.24(a)

    Generate a dictionary list as a text file using permutations of terms
    stored in json file. Terms are intended to be accumulated during
    information gathering phase of a penetration test. The more relevant the
    terms, the higher chance of success.
"""

import argparse
import itertools
import json
import re


def number_swap(term):
    """
        Replace numeric chars within a string with common substitutions of
        letters.

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

        :param target_list: generic list of strings, typically only letters
        :return: list of 5 common permutations of all terms in 'target_list'
        :rtype: list
    """
    target_list = re.sub('\s+', ' ', ','.join(target_list)).replace(' ', ',')
    target_list = [x.strip() for x in target_list.split(',')]
    mangled_list = []
    for item in target_list:
        mangled_list.extend(letter_swap(item))
        mangled_list.extend(permute_casing(item))
        mangled_list.append(alternate_case(item, True))
        mangled_list.append(alternate_case(item, False))
    return mangled_list


def main():
    """
        ** All code below currently for testing and proof of concept **

        TODO: Rewrite logic of final dictionary generation after completing
            and expanding upon algorithms above.

        Generate personalized dictionary list of passwords, tailored towards a
        target with information gathered during initial phase of pen test.
    """
    print("\n*X* Personalized Dictionary Generator *X* \n")

    # list to hold all passwords after processing
    final_collection = []

    # user sets pw and list length parameters
    parser = argparse.ArgumentParser(
        description="Generate a dictionary list as a text file using " +
                    "permutations of terms.\nData imported from populated " +
                    "JSON template.\n\n")
    parser.add_argument('--min', type=int, required=True,
                        help='Minimum password length')
    parser.add_argument('--max', type=int, required=True,
                        help='Maximum password length')
    parser.add_argument('-n', '--num', type=int, required=True,
                        help='Number of passwords to be generated')
    parser.add_argument('-f', '--file', required=True, help='Criteria file')
    parser.add_argument('-o', '--out', help='Generated password file')
    args = parser.parse_args()
    min_length = args.min
    max_length = args.max
    password_count = args.num
    output_file = args.out if args.out else "dictionary.txt"

    try:
        criteria = json.loads("".join(open(args.file, "r").readlines()))
    except FileNotFoundError as e:
        print("Could not open criteria file: %s" % e)
        exit(1)
    else:
        print("\nPlease wait while your dictionary is generated... This may " +
              "take a while depending on the amount of data.\n")

        # use function 'mangle' for most common permutation
        pets = mangle(criteria["pets"]) if criteria["pets"] else []
        sports = mangle(criteria["sports"]) if criteria["sports"] else []
        family = mangle(criteria["family"]) if criteria["family"] else []
        music = mangle(criteria["music"]) if criteria["music"] else []
        states = mangle(criteria["states"]) if criteria["states"] else []
        cities = mangle(criteria["cities"]) if criteria["cities"] else []
        schools = mangle(criteria["schools"]) if criteria["schools"] else []
        colors = mangle(criteria["colors"]) if criteria["colors"] else []
        streets = mangle(criteria["street_numbers"]) if criteria[
            "streets"] else []
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

        # remove dupes and combine lists of words meeting length requisites
        final_collection.extend(combinations + final_suffix)
        collection = list(set(final_collection))
        collection = [word for word in collection if
                      max_length >= len(word) >= min_length]

        # push probable passwords higher
        numeric = []
        alpha_lower = []
        alpha_mixed = []
        alnum_lower = []
        alnum_mixed = []
        special = []

        for item in collection:
            if item.isdigit():
                numeric.append(item)
            elif item.isalpha() and (
                item.islower() or (
                    item[0].isupper() and item[1:].islower())):
                alpha_lower.append(item)
            elif item.isalpha():
                alpha_mixed.append(item)
            elif item.isalnum() and item.islower():
                alnum_lower.append(item)
            elif item.isalnum():
                alnum_mixed.append(item)
            else:
                special.append(item)

        final_collection = numeric + alpha_lower
        final_collection.extend(list(
            itertools.chain.from_iterable(
                zip(alnum_lower, alpha_mixed))))
        final_collection[
            len(final_collection):] = alnum_mixed + special

        # create list of words with length specified by user
        count = 0
        with open(output_file, 'w+') as my_file:
            for word in final_collection:
                if count == password_count:
                    break
                my_file.write(word + '\n')
                count += 1

        print("Dictionary list generated: " + output_file)

if __name__ == "__main__":
    main()
