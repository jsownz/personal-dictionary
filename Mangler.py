"""
    Various algorithms used in the permutation of strings and lists
    for the generation of a personalized dictionary list.
"""

import re
from itertools import product


def full_number_swap(term):
    """
        Replace numeric chars within a string with common substitutions of
        letters. Return all permutations.
        Author: th3xer0

        :param term: numeric string
        :return: list of argument 'term' variations w/ number substitutions
        :rtype: list
    """
    number_alt_dict = {
        '0': 'O',
        '1': 'l',
        '2': 'Z',
        '3': 'E',
        '4': 'A',
        '5': 'S',
        '6': 'bG',
        '7': 'TL',
        '8': 'B',
        '9': 'gq'
    }
    new_terms = []
    for character in term:
        alt_number = number_alt_dict.get(character, character)
        new_terms.append([character, ] if alt_number == character else [
            char for char in ",".join(character + alt_number).split(",")])
    return [''.join(t) for t in product(*new_terms)]


def full_letter_swap(term):
    """
        Replace alpha chars within a string with common substitutions of
        numbers and symbols. Return all permutations
        Author: th3xer0

        :param term: string of letters
        :return: list of argument 'term' variations w/ letter substitutions
        :rtype: list
    """
    term = term.lower()
    letter_alt_dict = {
        'a': '@4',
        'b': '8',
        'c': '(',
        'e': '3',
        'g': '69',
        'h': '#',
        'i': '!1',
        'l': '1!',
        'o': '0',
        's': '5$',
        't': '+7',
        'z': '2'
    }
    new_terms = []
    for character in term:
        alt_letter = letter_alt_dict.get(character, character)
        new_terms.append([character, ] if alt_letter == character else [
            char for char in ",".join(character + alt_letter).split(",")])
    return [''.join(t) for t in product(*new_terms)]


def number_swap(term):
    """
        Replace numeric chars within a string with common substitutions of
        letters.

        :param term: numeric string
        :return: list of argument 'term' variations w/ number substitutions
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
        :return: list of argument 'term' variations w/ letter substitutions
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
        Change case to alternate_case between lower and upper;
        if first is true begin with the fist char in caps.

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


def calculate_ord(term):
    """
        Return summation of ordinance of chars

        :param term: string to be evaluated
        :return: integer
    """
    return sum([ord(x) for x in term])


def compare_num_of_chars(term):
    """
        Return number of chars in term

        :param term: string to be evaluated
        :return: integer
    """
    return len(term)


def sort_by_ord(list_to_sort):
    """
        Return list sorted for simplicity then sorted by length

        :param list_to_sort: list of strings to sort to reduce chaos.
        :type list_to_sort: list
        :rtype: list
    """
    list_to_sort.sort(key=calculate_ord, reverse=True)
    list_to_sort.sort(key=compare_num_of_chars)


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
