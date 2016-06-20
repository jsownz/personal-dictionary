#!/usr/bin/env python

"""
    Author: John Vardanian
    Last Modified: 2016-06-20
    Python3.5 using PyCharm / Atom / Sublime Text 3

    r0.0.9-2016-06-20(a)

    Generate a dictionary list as a text file using permutations of terms
    delimited by a comma. Terms are intended to be accumulated during
    information gathering phase of a penetration test. The more relevant the
    terms, the higher chance of success.

    Usage:
    Currently no type checking. Enter each categorized set of terms separated
    by commas.

    Contributions:
    This project is open source and everyone is welcome to contribute in
    development, testing, and feature suggestions. All pull requests approved
    by John Vardanian at this time.
"""

import itertools
import shlex


def number_swap(term):
    """
        Replace numeric chars within a string with common substitutions of
        letters, spelling, and symbols.

        :param term: string
        :return new_terms: term with all numbers replaced by common subs
        :rtype: list
    """
    number_alt_dict = {'0': ['O', 'zero'], '1': ['l', 'i', '|', 'one'],
                       '2': ['Z', 'two'], '3': ['E', 'three'],
                       '4': ['A', 'four'], '5': ['S', 'five'],
                       '6': ['b', 'G', 'six'], '7': ['T', 'L', 'seven'],
                       '8': ['B', 'eight'], '9': ['g', 'q', 'nine']}
    new_terms = []
    index = 0
    while index < len(term):
        number_list = list(term)
        if number_list[index] in number_alt_dict:
            for replace in number_alt_dict[number_list[index]]:
                number_list[index] = replace
                new_terms.append(''.join(number_list))
        index += 1

    return new_terms


def letter_swap_simple_full(term):
    """
        Replace alpha chars within a string with common substitutions of
        numbers and symbols.

        :param term: string
        :return new_term: term with all letters replaced by common alternatives
        :rtype: string
    """
    new_term = ""
    letter_alt_dict = {'a': ['@'], 'b': ['8'], 'e': ['3'], 'i': ['!'],
                       'l': ['1'], 'o': ['0'], 's': ['$'], 't': ['7'],
                       'Z': ['2']}
    for letter in term:
        if letter in letter_alt_dict:
            new_term += letter_alt_dict[letter][0]
        else:
            new_term += letter
    return new_term


def letter_swap(term):
    """
        Replace alpha chars within a string with common substitutions of
        numbers and symbols.

        :param term: string
        :return new_terms: list of strings derived from term with replacements
        :rtype: list
    """
    letter_alt_dict = {'a': ['@', '4'], 'b': ['8'], 'c': ['(', '['],
                       'e': ['3'], 'g': ['6', '9'], 'h': ['#'],
                       'i': ['!', '|'], 'l': ['1'],
                       'o': ['0', 'oh'], 's': ['5', '$'], 't': ['+', '7'],
                       'Z': ['2']}
    new_terms = []
    index = 0
    while index < len(term):
        letter_list = list(term)
        if letter_list[index] in letter_alt_dict:
            for replace in letter_alt_dict[letter_list[index]]:
                letter_list[index] = replace
                new_terms.append(''.join(letter_list))
        index += 1

    return new_terms


def alternate_case(term, first):
    """
        Change case to alternate_case between lower and upper; if first is true
        begin with the fist char in caps.

        :param term: string
        :param first: boolean
        :return ret: permutation of term with alternating casing on letters
        :rtype: string
    """
    ret = ""
    for char in term:
        if first:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            first = not first
    return ret


def permute_phone(phone):
    """
        Return list of various phone permutations (area code, reversed etc).

        :param phone: string - intended to be 10 digits
        :return: list of 6 phone number permutations of arg phone
        :rtype: list
    """
    return [phone, phone[3:], phone[0:3], phone[6:], phone[::-1],
            reverse_string(phone[0:3])] + number_swap(phone)


def permute_casing(term):
    """
        Return list of term with title case, all lower, and all upper.

        :param term: base string to case upper, title, & lower
        :return: list of 3 casing permutations of 'term'
        :rtype: list
    """
    return [term.upper(), term.lower(), term.capitalize()]


def permute_year(year):
    """
        Return list of common year perms. (last 2 digits, backwards, etc).

        :param year: string
        :return: list of 4 permuted strings derived from argument 'year'
        :rtype: list
    """
    return [year[2:], year, year[::-1]] + number_swap(year)


def reverse_string(term):
    """
        Return string in reverse.

        :param term: string to be reversed
        :return: argument term in reverse as string
        :rtype: string
    """
    return term[::-1]


def swap_char_positions(term):
    """
        Return all permutations of a string in a list.

        :param term: string to have all letters locations swapped
        :return: list of all permutations of argument 'term'
        :rtype: list
    """
    words = []
    res = itertools.permutations(term, len(term))
    for i in res:
        words.append(''.join(i))
    return words


def store_info(prompt):
    """
        Return list of items exploded by char ',' and trimmed of whitespace.
        Spaces are replaced by commas to treat multi word entries as separate
        words.

        :param prompt: string
        :return: list exploded by commas
        :rtype: list
    """
    temp = input(prompt + ": ")
    temp = ','.join(shlex.split(temp))
    return [x.strip() for x in temp.split(',')]


def permute_zip_code(zip_code):
    """
        Return list of string zip_code with 3 variations.

        :param zip_code: string intended to be 5 digits
        :return: list of strings of permuted zip code argument
        :rtype: list
    """
    return [reverse_string(zip_code)] + number_swap(zip_code) + [zip_code]


def permute_music(music):
    """
        Return common permutations of music related terms.

        :param music: string
        :return: list of permuted variations of string 'music'
        :rtype: list
    """
    return permute_casing(music) + [reverse_string(music)] + [
        alternate_case(music, True)] + [alternate_case(music, False)] + [
        letter_swap_simple_full(music)]


def permute_street_number(street_number):
    """
        Return common permutations of street numbers.

        :param street_number: string
        :return: list of permutations of a street number
        :rtype: list
    """
    return [street_number, reverse_string(street_number)] + number_swap(
        street_number)


def mangle(temp_list):
    """
        Return a list containing most frequently used permutation functions

        :param temp_list: list of typically non numeric strings to permute
        :return new_list: most common variations of terms to be used in dict
        :rtype: list
    """
    new_list = []
    for temp in temp_list:
        new_list += letter_swap(temp)
        new_list += permute_casing(temp)
        new_list.append(reverse_string(temp))
        new_list.append(alternate_case(temp, True))
        new_list.append(alternate_case(temp, False))
    return new_list


def permute_lists(first, second):
    """
        Return list of all combinations of words from lists sent as args

        :param first: list to permute with 'second'
        :param second: list to permute with 'first'
        :return temp_list: list of combined words from arguments
        :rtype: list
    """
    temp_list = []
    for first_item in first:
        for second_item in second:
            temp_list.append(first_item + second_item)
            temp_list.append(second_item + first_item)
    return temp_list


def main():
    """
        **All code below currently for testing and proof of concept**

        @TODO: Rewrite logic of final dictionary generation after completing
            and expanding upon algorithms above.

        Generate text file of potential passwords (dictionary list), tailored
        towards information gathered during initial phase of pen test.
    """
    print("\n** Personalized Dictionary Generator ** \n\nEnter data in the " +
          "prompts below, separated with commas.\nE.G. Phones: " +
          "5555555555, 9995550000\n\nEach category is similar to that of a " +
          "security question to recover a password, or a category that is " +
          "commonly used by individuals to remember their passwords. " +
          "When the script completes a file titled 'dictionary.txt' " +
          "will be generated in the same directory as the script. The " +
          "dictionary will contain a large number of permutations of the " +
          "information entered.\n\nThe more relevant information entered " +
          "the higher chance of success. The information entered determines " +
          "the quality of dictionary that is generated.\n")

    final_collection = []

    year_info = store_info("Years")
    pet_terms = store_info("Pets")
    sports = store_info("Sports")
    music = store_info("Music")
    family_terms = store_info("Family")
    phone_numbers = store_info("Phones")
    states = store_info("States")
    cities = store_info("Cities")
    zip_codes = store_info("Zip codes")
    streets = store_info("Street names")
    street_numbers = store_info("Street numbers")
    schools = store_info("Schools")
    colors = store_info("Colors")
    other_terms = store_info("Other terms")

    print("\nPlease wait while your dictionary is generated. " +
          "This may take several minutes.\n")

    pets = \
        mangle(pet_terms)  # pet names, animal types, anything animals
    sports = \
        mangle(sports)  # sports teams, mascots, anything sports
    family = \
        mangle(family_terms)  # close friends, family, family traditions, etc.
    music = \
        mangle(music)  # music genres, bands, songs, anything music
    states = \
        mangle(states)  # states of importance, e.g: resident of or vacations
    cities = \
        mangle(cities)  # cities of importance, e.g: resident of or vacations
    schools = \
        mangle(schools)  # school names, mascots, teams, abbreviations, etc.
    colors = \
        mangle(colors)  # colors of significance to target, e.g. team colors
    streets = \
        mangle(streets)  # names of streets of importance, e.g: residence of
    other = \
        mangle(other_terms)  # terms of significance that don't meet a category

    phones = []
    for phone in phone_numbers:
        phones += permute_phone(phone)
    years = []
    for year in year_info:
        years += permute_year(year)
    zips = []
    for zip_code in zip_codes:
        zips += permute_zip_code(zip_code)
    street_nums = []
    for street_number in street_numbers:
        street_nums += permute_street_number(street_number)

    for number in phones:
        final_collection.append(number)

    collections = [cities, colors, family, music, other, pets, schools, sports,
                   states, streets]

    combinations = []
    collection_count = len(collections)
    marker = 0
    while marker < collection_count:
        for temp_list in collections[(marker + 1):]:
            for item in collections[marker]:
                combinations.append(item)
            combinations += permute_lists(collections[marker], temp_list)
        marker += 1

    length = len(other)
    index = 0
    while index < length:
        for item in other[index:]:
            combinations.append(other[index] + item)
            combinations.append(item + other[index])
        index += 1

    temp_list = []
    for word in combinations:
        temp_list.append(word + "!")
        temp_list.append(word + "1")
        temp_list.append(word + "123")
        for year in years:
            temp_list.append(word + year)
        for zip_code in zip_codes:
            temp_list.append(word + zip_code)
        for street_number in street_nums:
            temp_list.append(word + street_number)

    final_collection += combinations
    final_collection += temp_list
    collection = list(set(final_collection))
    collection = [word for word in collection if 14 >= len(word) > 6]

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
                item.islower() or (item[0].isupper() and item[1:].islower())):
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
    final_collection += alpha_lower
    final_collection += alpha_numeric_lower
    final_collection += alpha_numeric_mixed_case
    final_collection += alpha_mixed_case
    final_collection += special_chars

    count = 0
    with open('dictionary.txt', 'a') as my_file:
        for word in final_collection:
            if count == 200000:
                break
            my_file.write(word + '\n')
            count += 1

    print("Dictionary list generation complete. File is \"dictionary.txt\"" +
          " in script directory")

if __name__ == "__main__":
    main()
