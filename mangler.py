"""
    mangler.py
    Python 3
    Last Modified: 2016-07-26

    Functions:
     - store_cli_args()
     - parse_json(path)
     - letter_swap(term)
     - permute_casing(term)
     - alternate_case(term, first=True)
     - mangle(target_list)
     - number_swap(term)
     - permute_phone(phone)
     - permute_year(year)
     - reverse_string(term)
     - permute_zip_code(zip_code)
     - perm_st_num(street_number)
     - permute_criteria(criteria)
     - permute_collections(collections)
     - permute_other(combinations, other)
     - add_suffixes(combinations, phone_numbers, street_nums, years, zips)
     - consolidate_final(word_groups)
     - term_types(collection)
     - calculate_ord(term)
     - compare_num_of_chars(term)
     - ord_sort(list_to_sort)
     - sort_words(collection)
     - clean_list(max_length, min_length, results)
     - read_input_list(args, max_length, min_length)
     - generate_dictionary(input_terms, output, pw_count, results)
"""

import argparse
import itertools
import json
import re


def store_cli_args():
    """
        Parse CLI arguments; assign defaults where needed.

        :return: arguments passed to ManifestDictionary via CLI & defaults
        :rtype: dictionary
    """
    parser = argparse.ArgumentParser(
        description="Generate a dictionary list as a text file using " +
        "permutations of terms.\nData imported from populated " +
        "JSON template.\n\n")
    parser.add_argument(
        '--min', type=int, required=False,
        help='Minimum password length')
    parser.add_argument(
        '--max', type=int, required=False,
        help='Maximum password length')
    parser.add_argument(
        '-n', '--num', type=int, required=False,
        help='Number of passwords to be generated')
    parser.add_argument(
        '-f', '--file', required=True,
        help='Criteria file (JSON)')
    parser.add_argument(
        '-i', '--input', required=False,
        help='Wordlist to mix with results generated from criteria')
    parser.add_argument(
        '-o', '--out', help='Generated password file')

    args = parser.parse_args()
    min_length = args.min or 6
    max_length = args.max or 12
    pw_count = args.num or 20000
    input_file = args.input or False
    output_file = args.out or "dictionary.txt"

    return {
        'args': args,
        'input_file': input_file,
        'max_length': max_length,
        'min_length': min_length,
        'output_file': output_file,
        'pw_count': pw_count
    }


def parse_json(path):
    """
        Handle parsing of JSON file to load into criteria

        :param path: file to read JSON data from
        :type path: string
        :return: decoded dictionary of file contents
        :rtype: dictionary
    """
    handle = open(path, "r+")
    try:
        data = handle.read()
        opened = json.loads(data)
    except ValueError as val_e:
        exit(u"Invalid formatting in JSON file: {0:s}".format(val_e.__str__()))
    else:
        return opened
    finally:
        handle.close()


def letter_swap(term):
    """
        Replace alpha chars within a string with common substitutions of
        numbers and symbols.

        :param term: string of letters
        :type term: string
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
                new_terms.append("".join(letter_list))
        marker += 1

    return new_terms


def permute_casing(term):
    """
        Return list of term with title case, all lower, and all upper.

        :param term: term of any length containing alpha chars
        :type term: string
        :return: list of 'term' with variations using 2 common casing styles
        :rtype: list
    """

    return [term.lower(), term.capitalize()]


def alternate_case(term, first=True):
    """
        Change case to alternate_case between lower and upper;
        if first is true begin with the fist char in caps.

        :param term: target term to alter
        :type term: string
        :param first: boolean true if first letter is cased upper
        :type first: boolean
        :return: string 'term' with letters alternating upper/lower case
        :rtype: string
    """
    new_string = ""
    for letter in term:
        if first:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
        if letter != " ":
            first = not first

    return new_string


def mangle(target_list):
    """
        Return a list containing most frequently used permutation functions

        :param target_list: generic list of strings, typically only letters
        :type target_list: list
        :return: 5 common permutations of all terms in 'target_list'
        :rtype: list
    """
    target_list = re.sub(r"\s+", " ", ",".join(target_list)).replace(" ", ",")
    target_list = [x.strip() for x in target_list.split(",")]
    mangled_list = []
    for term in target_list:
        mangled_list.extend(letter_swap(term))
        mangled_list.extend(permute_casing(term))
        mangled_list.append(alternate_case(term))
        mangled_list.append(alternate_case(term, first=False))

    return mangled_list


def number_swap(term):
    """
        Replace numeric chars within a string with common substitutions of
        letters.

        :param term: contains numeric chars
        :type term: string
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
                new_terms.append("".join(number_list))
        marker += 1

    return new_terms


def permute_phone(phone):
    """
        Return list of various phone permutations (area code, reversed etc).

        :param phone: phone number of format 10 digits
        :type phone: string
        :return: list of 'phone' number permutations
        :rtype: list
    """

    return [
        phone,
        phone[3:],
        phone[0:3],
        phone[6:],
        reverse_string(phone),
        reverse_string(phone[0:3])
    ] + number_swap(phone)


def permute_year(year):
    """
        Return list of common year perms. (last 2 digits, backwards, etc).

        :param year: term containing year made of digits
        :type year: string
        :return: list of 'year' using 4 common styles
        :rtype: list
    """

    return [
        year[2:],
        year,
        reverse_string(year)
    ] + number_swap(year)


def reverse_string(term):
    """
        Return string in reverse.

        :param term: term to be reversed
        :type term: string
        :return: string of 'term' after being reversed
        :rtype: string
    """

    return term[::-1]


def permute_zip_code(zip_code):
    """
        Return list of string zip_code with 3 variations.

        :param zip_code: 5 digits zip/postal code
        :type zip_code: string
        :return: list of 3 common permutation styles for zip codes
        :rtype: list
    """

    return [reverse_string(zip_code)] + number_swap(zip_code) + [zip_code]


def perm_st_num(street_number):
    """
        Return common permutations of street numbers.

        :param street_number: string of any number of digits
        :type street_number: string
        :return: list of 'street_number' with 3 common permutation styles
        :rtype: list
    """

    return [
        street_number,
        reverse_string(street_number)
    ] + number_swap(street_number)


def permute_criteria(criteria):
    """
        Use function 'mangle' for most common permutation

        :param criteria: data from JSON file template
        :return: various collections of permuted data from JSON template
    """
    collections = {
        "cities": criteria["cities"] if criteria["cities"] else [],
        "colors": criteria["colors"] if criteria["colors"] else [],
        "family": criteria["family"] if criteria["family"] else [],
        "jobs": criteria["employment"] if criteria["employment"] else [],
        "music": criteria["music"] if criteria["music"] else [],
        "other": criteria["other"] if criteria["other"] else [],
        "pets": criteria["pets"] if criteria["pets"] else [],
        "phone_numbers": criteria["phone"] if criteria["phone"] else [],
        "schools": criteria["schools"] if criteria["schools"] else [],
        "sports": criteria["sports"] if criteria["sports"] else [],
        "states": criteria["states"] if criteria["states"] else [],
        "streets": criteria["street_numbers"] if criteria["streets"] else [],
        "zip_codes": criteria["zip_codes"] if criteria["zip_codes"] else []
    }

    # permute lists for base passwords using function mangle
    to_mangle = [
        collections["cities"],
        collections["colors"],
        collections["family"],
        collections["jobs"],
        collections["music"],
        collections["other"],
        collections["pets"],
        collections["schools"],
        collections["sports"],
        collections["states"],
        collections["streets"]
    ]
    mangled = [mangle(x) for x in to_mangle]

    # permute lists using category specific functions
    phones = []
    for phone in criteria["phone"]:
        phones.extend(permute_phone(phone))

    years = []
    for year in criteria["years"]:
        years.extend(permute_year(year))

    zips = []
    for zip_code in collections["zip_codes"]:
        zips.extend(permute_zip_code(zip_code))

    street_nums = []
    for street_number in criteria["street_numbers"]:
        street_nums.extend(perm_st_num(street_number))

    return mangled, collections["other"], collections["phone_numbers"], \
        phones, street_nums, years, zips


def permute_collections(collections):
    """
        Permute collections to combine 2 of every list from collections

        :param collections: group of categorized terms to permute
        :type collections: list
        :return: permutations of combinations of categorized terms
    """
    combinations = []
    list_count = len(collections)
    marker = 0
    while marker < list_count:
        for list_portion in collections[(marker + 1):]:
            for item in collections[marker]:
                combinations.append(item)
            variations = list(
                itertools.product(collections[marker], list_portion))
            for term in variations:
                combinations.extend(
                    [term[0] + term[1], term[1] + term[0]])
        marker += 1

    return combinations


def permute_other(combinations, other):
    """
        Permute category 'other' against itself

        :param combinations: list of word permutations
        :param other: list of miscellaneous info to permute against itself
    """
    length = len(other)
    marker = 0
    while marker < length:
        for item in other[marker:]:
            combinations.extend(
                [other[marker] + item, item + other[marker]])
        marker += 1


def add_suffixes(combinations, phone_numbers, street_nums, years, zips):
    """
        Add suffix of additional common variations to existing combinations

        :param combinations: current collection of words
        :param phone_numbers: permutations of phones
        :param street_nums: permutations of street numbers
        :param years: permutations of years
        :param zips: permutations of zip
        :return: list of words with common suffixes appended
        :rtype: list
    """
    with_suffix = []
    for word in combinations:
        # add generic numeric and special chars
        with_suffix.extend([
            str(word) + "!",
            str(word) + "1",
            str(word) + "123"
        ])

        for year in years:
            with_suffix.append(word + year)

        for zip_code in zips:
            with_suffix.append(word + zip_code)

        for street_number in street_nums:
            with_suffix.append(word + street_number)

        # append area code from phone numbers to base words
        for phone in phone_numbers:
            with_suffix.append(word + phone[0:3])

    return with_suffix


def consolidate_final(word_groups):
    """
        Combine password types for results

        :param word_groups: dictionary of categorized words
        :return: intertwined list of different groups of words
    """
    results = word_groups["numeric"] + word_groups["alpha_lower"]
    results.extend(list(
        itertools.chain.from_iterable(
            zip(word_groups["alnum_lower"], word_groups["alpha_mixed"]))))
    results.extend(list(
        itertools.chain.from_iterable(
            zip(word_groups["alnum_mixed"], word_groups["special"]))))

    return results


def term_types(collection):
    """
        Take list and split into categorized lists inside of a dictionary

        :param collection: list of strings
        :type collection: list
        :return: dictionary with lists of terms separated by casing and chars
        :rtype: dictionary
    """
    numeric = []
    special = []
    alpha_lower = []
    alpha_mixed = []
    alnum_lower = []
    alnum_mixed = []

    for item in collection:
        if item.isdigit():
            numeric.append(item)
        elif item.isalpha():
            if item.islower() or (
                    item[0].isupper() and item[1:].islower()):
                alpha_lower.append(item)
            else:
                alpha_mixed.append(item)
        elif item.isalnum():
            if item.islower():
                alnum_lower.append(item)
            else:
                alnum_mixed.append(item)
        else:
            special.append(item)

    return dict(
        numeric=numeric,
        special=special,
        alpha_lower=alpha_lower,
        alpha_mixed=alpha_mixed,
        alnum_lower=alnum_lower,
        alnum_mixed=alnum_mixed)


def calculate_ord(term):
    """
        Return summation of ordinance of chars in arg term

        :param term: term to be evaluated for complexity
        :type term: string
        :return: summation of 'ord' function called on each char
        :rtype: integer
    """

    return sum([ord(x) for x in term])


def compare_num_of_chars(term):
    """
        Return number of chars in term

        :param term: string to be evaluated
        :type term: string
        :return: length of argument term
        :rtype: integer
    """

    return len(term)


def ord_sort(list_to_sort):
    """
        Return list sorted for simplicity then sorted by length

        :param list_to_sort: list of strings to sort to reduce chaos.
        :type list_to_sort: list
    """
    list_to_sort.sort(key=calculate_ord, reverse=True)
    list_to_sort.sort(key=compare_num_of_chars)


def sort_words(collection):
    """
        Push probable passwords towards top of the list

        :param collection: words to be sorted
        :return: sorted list of passwords
        :rtype: list
    """
    word_groups = term_types(collection)
    for word in word_groups:
        ord_sort(word_groups[word])
    return word_groups


def clean_list(max_length, min_length, results):
    """
        Remove duplicates and enforce length params

        :param max_length: maximum characters per password
        :param min_length: minimum characters per password
        :param results: collection of passwords to process
        :return: passwords meeting criteria in length without duplicates
    """
    collection = list(set(results))
    return [
        word for word in collection if max_length >= len(word) >= min_length
    ]


def read_input_list(args, max_length, min_length):
    """
        Take words form imported list and enforce length boundaries

        :param args: cli args for 'input'
        :param max_length: upper bound pw length
        :param min_length: lower bound pw length
        :return: input list parsed to meet criteria
    """
    input_terms = []
    if args.input:
        try:
            with open(str(args.input), "r") as other_file:
                for line in other_file:
                    if max_length >= len(line.strip()) >= min_length:
                        input_terms.append(line)
        except FileNotFoundError:
            print("Unable to find: " + args.input + ". Finishing...")

    return input_terms


def generate_dictionary(input_terms, output, pw_count, results):
    """
        Save list with filename & length specified by user (or defaults)

        :param input_terms: 3rd party dictionary list to combine
        :param output: file to print new dictionary as
        :param pw_count: number of passwords to generate
        :param results: list of consolidated pw's to print
    """
    count = 0
    pws = iter(input_terms) if input_terms else input_terms
    lines_left = True
    with open(output, "w+") as my_file:
        for word in results:
            if count == pw_count:
                break
            if input_terms:
                try:
                    if count % 2 and lines_left:
                        my_file.write(next(pws))
                    else:
                        my_file.write(word + "\n")
                except StopIteration:
                    lines_left = False
                    continue
            else:
                my_file.write(word + "\n")
            count += 1
