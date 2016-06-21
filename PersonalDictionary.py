#!/usr/bin/env python

"""
    Author: John Vardanian
    Last Modified: 2016-06-21
    Python3.5 using PyCharm / Atom / Sublime Text 3

    r0.0.10-2016.06.21(a)

    Generate a dictionary list as a text file using permutations of terms
    delimited by a comma. Terms are intended to be accumulated during
    information gathering phase of a penetration test. The more relevant the
    terms, the higher chance of success.
"""

import itertools
import shlex


def number_swap(term):
    """
        Replace numeric chars within a string with common substitutions of
        letters, spelling, and symbols.
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


def letter_swap(term):
    """
        Replace alpha chars within a string with common substitutions of
        numbers and symbols.
    """
    letter_alt_dict = {'a': ['@', '4'], 'b': ['8'], 'c': ['('],
                       'e': ['3'], 'g': ['6', '9'], 'h': ['#'],
                       'i': ['!'], 'l': ['1'],
                       'o': ['0'], 's': ['5', '$'], 't': ['+', '7'],
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
    """
    return [
        phone,
        phone[3:],
        phone[0:3],
        phone[6:],
        phone[::-1],
        reverse_string(phone[0:3])] + number_swap(phone)


def permute_casing(term):
    """
        Return list of term with title case, all lower, and all upper.
    """
    return [
        term.upper(),
        term.lower(),
        term.capitalize()
    ]


def permute_year(year):
    """
        Return list of common year perms. (last 2 digits, backwards, etc).
    """
    return [
        year[2:],
        year,
        year[::-1]] + \
        number_swap(year)


def reverse_string(term):
    """
        Return string in reverse.
    """
    return term[::-1]


def permute_zip_code(zip_code):
    """
        Return list of string zip_code with 3 variations.
    """
    return [
        reverse_string(zip_code)] + \
        number_swap(zip_code) + \
        [zip_code]


def permute_music(music):
    """
        Return common permutations of music related terms.
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
    """
    return [
        street_number,
        reverse_string(street_number)] + \
        number_swap(street_number)


def mangle(target_list):
    """
        Return a list containing most frequently used permutation functions
    """
    new_list = []
    for item in target_list:
        new_list[len(new_list):] = letter_swap(item)
        new_list[len(new_list):] = permute_casing(item)
        new_list.append(reverse_string(item))
        new_list.append(alternate_case(item, True))
        new_list.append(alternate_case(item, False))
    return new_list


def store_info(prompt):
    """
        Return list of items exploded by char ',' and trimmed of whitespace.
        Spaces are replaced by commas to treat multi word entries as separate
        words.
    """
    user_input = input(prompt + ": ")
    user_input = ','.join(shlex.split(user_input))
    return [x.strip() for x in user_input.split(',')]


def main():
    """
        **All code below currently for testing and proof of concept**

        @TODO: Rewrite logic of final dictionary generation after completing
            and expanding upon algorithms above.

        Generate text file of potential passwords (dictionary list), tailored
        towards information gathered during initial phase of pen test.
    """
    print("\n** Personalized Dictionary Generator ** \n\nEnter words in the " +
          "prompts below, separated with commas.\nE.G. Phones: " +
          "5555555555, 9995550000\n\nEach category is similar to that of a " +
          "security question to recover a password, or a topic that is " +
          "commonly used by individuals to remember a password. " +
          "When the script completes, a file titled 'dictionary.txt' " +
          "will be generated in the same directory as the script. The " +
          "dictionary will contain a large number of permutations of the " +
          "information entered.\n\nThe more relevant information entered " +
          "the higher chance of success. The information entered determines " +
          "the quality of dictionary that is generated.\nTo be used only " +
          "authorized testing.\n\nLarge amounts of information may take " +
          "several minutes.\n\n")

    # list to hold all passwords after processing
    final_collection = []

    # user sets pw and list length parameters
    min_length = int(input("Min length: "))
    max_length = int(input("Max length: "))
    password_count = int(input("Number of passwords: "))

    # prompts user for terms to generate dictionary
    pet_terms = store_info("Pets")
    year_info = store_info("Years")
    phone_numbers = store_info("Phones")
    sports = store_info("Sports")
    family_terms = store_info("Family")
    employment_terms = store_info("Employment")
    states = store_info("States")
    cities = store_info("Cities")
    zip_codes = store_info("Zip codes")
    streets = store_info("Street names")
    street_numbers = store_info("Street numbers")
    schools = store_info("Schools")
    music = store_info("Music")
    colors = store_info("Colors")
    other_terms = store_info("Other terms")

    print("\nPlease wait while your dictionary is generated... This may " +
          "take several minutes.\n")

    # use function 'mangle' for most common permutation, typically alpha only
    pets = mangle(pet_terms)
    sports = mangle(sports)
    family = mangle(family_terms)
    music = mangle(music)
    states = mangle(states)
    cities = mangle(cities)
    schools = mangle(schools)
    colors = mangle(colors)
    streets = mangle(streets)
    other = mangle(other_terms)
    jobs = mangle(employment_terms)

    # lists that don't make use of function 'mangle'
    phones = []
    years = []
    zips = []
    street_nums = []

    # populate lists that don't use function 'mangle'
    for phone in phone_numbers:
        phones[len(phones):] = permute_phone(phone)

    for year in year_info:
        years[len(years):] = permute_year(year)

    for zip_code in zip_codes:
        zips[len(zips):] = permute_zip_code(zip_code)

    for street_number in street_numbers:
        street_nums[len(street_nums):] = perm_st_num(street_number)

    # add phone number to top of list
    final_collection[:0] = phone_numbers

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

    # permute collections to combine 2 of every category
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
        marker += 1

    # permute other against itself
    length = len(other)
    marker = 0
    while marker < length:
        for item in other[marker:]:
            combinations.append(other[marker] + item)
            combinations.append(item + other[marker])
        marker += 1

    # add additional common variations to base passwords
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

    # combine lists, remove duplicates, enforce length limitations
    final_collection[len(final_collection):] = combinations + final_suffix
    collection = list(set(final_collection))
    collection = [word for word in collection if
                  max_length >= len(word) >= min_length]

    # unfinished sorting process to push probable passwords higher
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
    final_collection[len(final_collection):] = alpha_lower
    final_collection[len(final_collection):] = alpha_numeric_lower
    final_collection[len(final_collection):] = alpha_numeric_mixed_case
    final_collection[len(final_collection):] = alpha_mixed_case
    final_collection[len(final_collection):] = special_chars

    # create list based on size set by user
    count = 0
    with open('dictionary.txt', 'a') as my_file:
        for word in final_collection:
            if count == password_count:
                break
            my_file.write(word + '\n')
            count += 1

    print("Dictionary list generation complete. File is \"dictionary.txt\"" +
          " in script directory.")

if __name__ == "__main__":
    main()
