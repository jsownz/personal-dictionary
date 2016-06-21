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
    return [phone, phone[3:], phone[0:3], phone[6:], phone[::-1],
            reverse_string(phone[0:3])] + number_swap(phone)


def permute_casing(term):
    """
        Return list of term with title case, all lower, and all upper.
    """
    return [term.upper(), term.lower(), term.capitalize()]


def permute_year(year):
    """
        Return list of common year perms. (last 2 digits, backwards, etc).
    """
    return [year[2:], year, year[::-1]] + number_swap(year)


def reverse_string(term):
    """
        Return string in reverse.
    """
    return term[::-1]


def permute_zip_code(zip_code):
    """
        Return list of string zip_code with 3 variations.
    """
    return [reverse_string(zip_code)] + number_swap(zip_code) + [zip_code]


def permute_music(music):
    """
        Return common permutations of music related terms.
    """
    return permute_casing(music) + [reverse_string(music)] + [
        alternate_case(music, True)] + [alternate_case(music, False)] + \
        letter_swap(music)


def permute_street_number(street_number):
    """
        Return common permutations of street numbers.
    """
    return [street_number, reverse_string(street_number)] + number_swap(
        street_number)


def mangle(temp_list):
    """
        Return a list containing most frequently used permutation functions
    """
    new_list = []
    for temp in temp_list:
        new_list += letter_swap(temp)
        new_list += permute_casing(temp)
        new_list.append(reverse_string(temp))
        new_list.append(alternate_case(temp, True))
        new_list.append(alternate_case(temp, False))
    return new_list


def store_info(prompt):
    """
        Return list of items exploded by char ',' and trimmed of whitespace.
        Spaces are replaced by commas to treat multi word entries as separate
        words.
    """
    temp = input(prompt + ": ")
    temp = ','.join(shlex.split(temp))
    return [x.strip() for x in temp.split(',')]


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

    final_collection = []

    # set pw and list length parameters
    min_length = int(input("Min length: "))
    max_length = int(input("Max length: "))
    password_count = int(input("Number of passwords: "))

    # prompt user for terms to form dictionary
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

    # use generic list permutation function 'mangle' for common permutations
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

    # use specialized functions for numeric and less common data / permutations
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

    # add phone number to top of list
    for number in phones:
        final_collection.append(number)

    # lists to permute for base passwords
    collections = [cities, colors, family, music, other, pets, schools, sports,
                   states, streets, jobs]

    # permute collections to combine 2 of every category
    combinations = []
    collection_count = len(collections)
    marker = 0
    while marker < collection_count:
        for temp_list in collections[(marker + 1):]:
            for item in collections[marker]:
                combinations.append(item)
            combos = list(
                itertools.product(collections[marker], temp_list))
            for fst, snd in combos:
                combinations.append(fst + snd)
        marker += 1

    # permute other against itself
    length = len(other)
    marker = 0
    while marker < length:
        for item in other[marker:]:
            combinations.append(other[marker] + item)
            combinations.append(item + other[marker])
        marker += 1

    # add additional common variations
    temp_list = []
    for word in combinations:
        # add generic numeric and special chars to base words
        temp_list.append(word + "!")
        temp_list.append(word + "1")
        temp_list.append(word + "123")
        # append year permutations to base words
        for year in years:
            temp_list.append(word + year)
        # append zip code permutations to base words
        for zip_code in zip_codes:
            temp_list.append(word + zip_code)
        # append street number permutations to base words
        for street_number in street_nums:
            temp_list.append(word + street_number)
        # append area code from phone numbers to base words
        for phone in phone_numbers:
            temp_list.append(word + phone[0:3])

    # combine lists, remove duplicates, and enforce length limitations
    final_collection += (combinations + temp_list)
    collection = list(set(final_collection))
    collection = [word for word in collection if
                  max_length >= len(word) >= min_length]

    # temporary sort algorithm to push more probable passwords higher
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
