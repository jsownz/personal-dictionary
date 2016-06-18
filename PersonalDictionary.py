#!/usr/bin/env python

"""
    Author: John Vardanian
    Last Modified: 2016-06-18
    Python3.5 using PyCharm / Atom

    r0.0.9-2016-06-18(a)

    Generate a dictionary list as a text file using permutations of terms
    delimited by a comma. Terms are intended to be accumulated during
    information gathering phase of a penetration test. The more relevant the
    terms, the higher chance of success.

    Usage:
    Currently no type checking. Enter each categorized set of terms separated
    by commas- no spaces at this time.
"""

import itertools
import shlex


def numeric_alternatives(term):
    """
        Replace numeric chars within a string with common substitutions of
        letters, spelling, and symbols.

        :param term: string
        :return new_term: term with all numbers replaced by common alternatives
        :rtype: string
    """
    new_term = ""
    number_alt_dict = {'0': ['O', 'zero'], '1': ['l', 'i', '|', 'one'],
                       '2': ['z', 'two'], '3': ['E', 'three'],
                       '4': ['A', 'four'], '5': ['S', 'five'],
                       '6': ['G', 'six'], '7': ['T', 'seven'],
                       '8': ['B', 'eight'], '9': ['G', 'nine']}
    for letter in term:
        if letter in number_alt_dict:
            new_term += number_alt_dict[letter][0]
        else:
            new_term += letter
    return new_term


def simple_letter_alternatives_full(term):
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


def letter_alternatives_permute(term):
    """
        Replace alpha chars within a string with common substitutions of
        numbers and symbols.

        :param term: string
        :return new_terms: list of strings derived from term with replacements
        :rtype: list
    """
    letter_alt_dict = {'a': ['@', '4'], 'b': ['8'], 'c': ['(', '['],
                       'e': ['3'], 'g': ['6', '9'], 'h': ['#'],
                       'i': ['!', '|', 'eye'], 'l': ['1', 'el'],
                       'o': ['0', 'oh'], 's': ['5', '$'], 't': ['+', '7'],
                       'Z': ['2', 'zee']}
    new_terms = []
    index = 0
    while index < len(term):
        letter_list = list(term)
        if letter_list[index] in letter_alt_dict:
            letter_list[index] = letter_alt_dict[letter_list[index]][0]
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

        :param phone:
        :return: list of 6 phone number permutations of arg phone
        :rtype: list
    """
    return [phone, phone[3:], phone[0:3], phone[6:], phone[::-1],
            reverse_term(phone[0:3])]


def permute_case(term):
    """
        Return list of term with title case, all lower, and all upper.

        :param term: base string to case upper, title, & lower
        :return: list
        :rtype: list
    """
    return [term.upper(), term.lower(), term.capitalize()]


def permute_year(year):
    """
        Return list of common year perms. (last 2 digits, backwards, etc).

        :param year: string
        :return: list of 4 permuted strings derived from argument year
        :rtype: list
    """
    return [year[2:], year, year[::-1], '_' + str(year)]


def reverse_term(term):
    """
        Return string in reverse.

        :param term: string
        :return: argument term in reverse as string
        :rtype: string
    """
    return term[::-1]


def full_string_permutation(term):
    """
        Return all permutations of a string in a list.

        :param term: string
        :return: list of all permutations of argument 'term'
        :rtype: list
    """
    words = []
    res = itertools.permutations(term, len(term))
    for i in res:
        words.append(''.join(i))
    return words


def split_by_comma(prompt):
    """
        Return list of items exploded by char ',' and trimmed of whitespace.

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

        :param zip_code: string
        :return: list of strings of permuted zip code argument
        :rtype: list
    """
    return [reverse_term(zip_code), numeric_alternatives(zip_code), zip_code]


def permute_music(music):
    """
        Return common permutations of music related terms.

        :param music: string
        :return: list of permuted variations of string 'music'
        :rtype: list
    """
    return permute_case(music) + [reverse_term(music)] + [
        alternate_case(music, True)] + [alternate_case(music, False)] + [
               simple_letter_alternatives_full(music)]


def permute_street_number(street_number):
    """
        Return common permutations of street numbers.

        :param street_number: string
        :return: list of permutations of a street number
        :rtype: list
    """
    return [street_number, reverse_term(street_number),
            numeric_alternatives(street_number), "_" + str(street_number),
            str(street_number) + "_"]


def generic_permuted_list(temp_list):
    """
        Return a list containing most frequently used permutation functions

        :param temp_list:
        :return new_list: most common variations of terms to be used in dict
        :rtype: list
    """
    new_list = []
    for temp in temp_list:
        new_list += letter_alternatives_permute(temp)
        new_list += letter_alternatives_permute(alternate_case(temp, True))
        new_list += letter_alternatives_permute(alternate_case(temp, False))
        new_list += letter_alternatives_permute(permute_case(temp))
        new_list += permute_case(temp)
        new_list.append(alternate_case(temp, True))
        new_list.append(alternate_case(temp, False))
        new_list.append(reverse_term(temp))
    return new_list


def main():
    """
        All code below currently for testing and proof of concept. Generate
        text file of potential passwords (dictionary list), tailored towards
        information gathered during initial phase of pen test.
    """
    final_collection = []

    years = split_by_comma("Years")
    pet_names = split_by_comma("Pets")
    sports = split_by_comma("Sports")
    music = split_by_comma("Music")
    family_members = split_by_comma("Family")
    phone_numbers = split_by_comma("Phones")
    states = split_by_comma("States")
    cities = split_by_comma("Cities")
    zip_codes = split_by_comma("Zip codes")
    streets = split_by_comma("Street names")
    street_numbers = split_by_comma("Street numbers")
    schools = split_by_comma("Schools")
    colors = split_by_comma("Colors")
    other_terms = split_by_comma("Other terms")

    print("\nPlease wait while your dictionary is generated. " +
          "This may take several minutes.\n")

    year_list = []
    for year in years:
        year_list += permute_year(year)
    pet_list = generic_permuted_list(pet_names)
    sports_list = generic_permuted_list(sports)
    family_list = generic_permuted_list(family_members)
    music_list = generic_permuted_list(music)
    states_list = generic_permuted_list(states)
    city_list = generic_permuted_list(cities)
    phone_list = []
    for phone in phone_numbers:
        phone_list += permute_phone(phone)
    zip_list = []
    for zip_code in zip_codes:
        zip_list += permute_zip_code(zip_code)
    school_list = generic_permuted_list(schools)
    color_list = generic_permuted_list(colors)
    street_list = generic_permuted_list(streets)
    street_num_list = []
    for street_number in street_numbers:
        street_num_list += permute_street_number(street_number)
    other_list = generic_permuted_list(other_terms)

    word_combinations = []
    for pet in pet_list:
        word_combinations.append(pet)
        for family in family_list:
            word_combinations.append(pet + family)
            word_combinations.append(family + pet)
        for sport in sports_list:
            word_combinations.append(pet + sport)
            word_combinations.append(sport + pet)
        for school in school_list:
            word_combinations.append(school + pet)
            word_combinations.append(pet + school)
        for state in states_list:
            word_combinations.append(state + pet)
            word_combinations.append(pet + state)
        for city in city_list:
            word_combinations.append(city + pet)
            word_combinations.append(pet + city)
        for other in other_list:
            word_combinations.append(other + pet)
            word_combinations.append(pet + other)
        for street in street_list:
            word_combinations.append(street + pet)
            word_combinations.append(pet + street)
        for music in music_list:
            word_combinations.append(music + pet)
            word_combinations.append(pet + music)
        for color in color_list:
            word_combinations.append(color + pet)
            word_combinations.append(pet + color)
    for family in family_list:
        word_combinations.append(family)
        for sport in sports_list:
            word_combinations.append(sport + family)
            word_combinations.append(family + sport)
        for school in school_list:
            word_combinations.append(school + family)
            word_combinations.append(family + school)
        for state in states_list:
            word_combinations.append(state + family)
            word_combinations.append(family + state)
        for city in city_list:
            word_combinations.append(city + family)
            word_combinations.append(family + city)
        for other in other_list:
            word_combinations.append(other + family)
            word_combinations.append(family + other)
        for street in street_list:
            word_combinations.append(street + family)
            word_combinations.append(family + street)
        for music in music_list:
            word_combinations.append(music + family)
            word_combinations.append(family + music)
        for color in color_list:
            word_combinations.append(color + family)
            word_combinations.append(family + color)
    for sport in sports_list:
        word_combinations.append(sport)
        for school in school_list:
            word_combinations.append(sport + school)
            word_combinations.append(school + sport)
        for state in states_list:
            word_combinations.append(sport + state)
            word_combinations.append(state + sport)
        for city in city_list:
            word_combinations.append(sport + city)
            word_combinations.append(city + sport)
        for other in other_list:
            word_combinations.append(other + sport)
            word_combinations.append(sport + other)
        for street in street_list:
            word_combinations.append(street + sport)
            word_combinations.append(sport + street)
        for music in music_list:
            word_combinations.append(music + sport)
            word_combinations.append(sport + music)
        for color in color_list:
            word_combinations.append(color + sport)
            word_combinations.append(sport + color)
    for school in school_list:
        word_combinations.append(school)
        for state in states_list:
            word_combinations.append(school + state)
            word_combinations.append(state + school)
        for city in city_list:
            word_combinations.append(school + city)
            word_combinations.append(city + school)
        for other in other_list:
            word_combinations.append(other + school)
            word_combinations.append(school + other)
        for street in street_list:
            word_combinations.append(street + school)
            word_combinations.append(school + street)
        for music in music_list:
            word_combinations.append(music + school)
            word_combinations.append(school + music)
        for color in color_list:
            word_combinations.append(color + school)
            word_combinations.append(school + color)
    for state in states_list:
        word_combinations.append(state)
        for city in city_list:
            word_combinations.append(state + city)
            word_combinations.append(city + state)
        for other in other_list:
            word_combinations.append(other + state)
            word_combinations.append(state + other)
        for street in street_list:
            word_combinations.append(street + state)
            word_combinations.append(state + street)
        for music in music_list:
            word_combinations.append(music + state)
            word_combinations.append(state + music)
        for color in color_list:
            word_combinations.append(color + state)
            word_combinations.append(state + color)
    for city in city_list:
        word_combinations.append(city)
        for other in other_list:
            word_combinations.append(other + city)
            word_combinations.append(city + other)
        for street in street_list:
            word_combinations.append(street + city)
            word_combinations.append(city + street)
        for music in music_list:
            word_combinations.append(music + city)
            word_combinations.append(city + music)
        for color in color_list:
            word_combinations.append(color + city)
            word_combinations.append(city + color)
    for other in other_list:
        word_combinations.append(other)
        for street in street_list:
            word_combinations.append(street + other)
            word_combinations.append(other + street)
        for music in music_list:
            word_combinations.append(music + other)
            word_combinations.append(other + music)
        for color in color_list:
            word_combinations.append(color + other)
            word_combinations.append(other + color)
    for street in street_list:
        word_combinations.append(street)
        for music in music_list:
            word_combinations.append(music + street)
            word_combinations.append(street + music)
        for color in color_list:
            word_combinations.append(color + street)
            word_combinations.append(street + color)
    for music in music_list:
        word_combinations.append(music)
        for color in color_list:
            word_combinations.append(color)
            word_combinations.append(color + music)
            word_combinations.append(music + color)
    for number in phone_list:
        word_combinations.append(number)

    length = len(other_list)
    index = 0
    while index < length:
        for item in other_list[index:]:
            word_combinations.append(other_list[index] + item)
            word_combinations.append(item + other_list[index])
        index += 1

    temp_list = []
    for word in word_combinations:
        temp_list.append(word + "!")
        temp_list.append(word + "1")
        temp_list.append(word + "123")
        for year in year_list:
            temp_list.append(word + year)
        for zip_code in zip_codes:
            temp_list.append(word + zip_code)
        for street_number in street_num_list:
            temp_list.append(word + street_number)
        for number in phone_list:
            temp_list.append(word + number)

    final_collection += temp_list
    collection = list(set(final_collection))
    collection = [
        word for word in collection if len(word) <= 15 and len(word) > 5
    ]

    with open('dictionary.txt', 'a') as my_file:
        for word in collection:
            my_file.write(word + '\n')


if __name__ == "__main__":
    main()
