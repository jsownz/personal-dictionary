#!/usr/bin/env python

"""
    Author: MC_GitFlow
    Last Modified: 2016-07-03
    Python3.5 using PyCharm

    r0.2.1-2016.07.03(b)

    Generate a dictionary list as a text file using permutations of terms
    stored in JSON file. Terms are intended to be accumulated during
    information gathering phase of a penetration test. The more relevant the
    terms, the higher chance of success. See template 'config.json'
"""

import argparse
import itertools
import json
import Mangler


def term_types(collection):
    """
        Take list and split into categorized lists inside of a dictionary

        :param collection: list of strings
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
    return {
        'numeric': numeric,
        'special': special,
        'alpha_lower': alpha_lower,
        'alpha_mixed': alpha_mixed,
        'alnum_lower': alnum_lower,
        'alnum_mixed': alnum_mixed
    }


def main():
    """
        ** Code below is temporary & for testing Mangler / proof of concept **

        Generate personalized dictionary list of passwords, tailored towards a
        target with information gathered during initial phase of pen test.
    """
    print("\n*X* Personalized Dictionary Generator *X* \n")

    # list to hold all passwords after processing
    results = []

    # user sets pw and list length parameters
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
        '-o', '--out', help='Generated password file')

    args = parser.parse_args()
    min_length = args.min or 6
    max_length = args.max or 12
    password_count = args.num or 20000
    output_file = args.out or "dictionary.txt"

    try:
        criteria = json.loads("".join(open(args.file, "r").readlines()))
    except FileNotFoundError as e:
        print("Could not open criteria file: %s" % e)
        exit(1)
    except ValueError as e:
        print("Invalid formatting in JSON file: %s" % e)
        exit(1)
    else:
        print("\nPlease wait while your dictionary is generated... This may " +
              "take a while depending on the amount of data.\n")

        # use function 'mangle' for most common permutation
        pets = Mangler.mangle(
            criteria["pets"]) if criteria["pets"] else []
        sports = Mangler.mangle(
            criteria["sports"]) if criteria["sports"] else []
        family = Mangler.mangle(
            criteria["family"]) if criteria["family"] else []
        music = Mangler.mangle(
            criteria["music"]) if criteria["music"] else []
        states = Mangler.mangle(
            criteria["states"]) if criteria["states"] else []
        cities = Mangler.mangle(
            criteria["cities"]) if criteria["cities"] else []
        schools = Mangler.mangle(
            criteria["schools"]) if criteria["schools"] else []
        colors = Mangler.mangle(
            criteria["colors"]) if criteria["colors"] else []
        streets = Mangler.mangle(
            criteria["street_numbers"]) if criteria["streets"] else []
        other = Mangler.mangle(
            criteria["other"]) if criteria["other"] else []
        jobs = Mangler.mangle(
            criteria["employment"]) if criteria["employment"] else []

        # lists to permute for base passwords
        collections = [
            pets, family, sports, schools, cities, music, states, jobs,
            streets, colors, other
        ]

        zip_codes = criteria["zip_codes"] if criteria["zip_codes"] else []
        phone_numbers = criteria["phone"] if criteria["phone"] else []

        # populate lists that don't use function 'mangle'
        phones = []
        for phone in criteria["phone"]:
            phones.extend(Mangler.permute_phone(phone))

        years = []
        for year in criteria["years"]:
            years.extend(Mangler.permute_year(year))

        zips = []
        for zip_code in criteria["zip_codes"]:
            zips.extend(Mangler.permute_zip_code(zip_code))

        street_nums = []
        for street_number in criteria["street_numbers"]:
            street_nums.extend(Mangler.perm_st_num(street_number))

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
                    combinations[len(combinations):] = \
                        [term_one + term_two, term_two + term_one]
            marker += 1

        # permute category 'other' against itself
        length = len(other)
        marker = 0
        while marker < length:
            for item in other[marker:]:
                combinations[len(combinations):] = \
                    [other[marker] + item, item + other[marker]]
            marker += 1

        # add suffix of additional common variations to existing combinations
        with_suffix = []
        for word in combinations:

            # add generic numeric and special chars
            with_suffix[
                len(with_suffix):] = [word + "!", word + "1", word + "123"]

            for year in years:
                with_suffix.append(word + year)

            for zip_code in zip_codes:
                with_suffix.append(word + zip_code)

            for street_number in street_nums:
                with_suffix.append(word + street_number)

            # append area code from phone numbers to base words
            for phone in phone_numbers:
                with_suffix.append(word + phone[0:3])

        # remove dupes and combine various lists meeting length requisites
        results.extend(phones + combinations + with_suffix)
        collection = list(set(results))
        collection = [word for word in collection if
                      max_length >= len(word) >= min_length]

        # push probable passwords higher
        word_groups = term_types(collection)
        for word in word_groups:
            Mangler.ord_sort(word_groups[word])

        # combine password types for results
        results = word_groups['numeric'] + word_groups['alpha_lower']
        results.extend(list(
            itertools.chain.from_iterable(
                zip(word_groups['alnum_lower'], word_groups['alpha_mixed']))))
        results.extend(list(
            itertools.chain.from_iterable(
                zip(word_groups['alnum_mixed'], word_groups['special']))))

        # save list with name & length specified by user
        count = 0
        with open(output_file, 'w+') as my_file:
            for word in results:
                if count == password_count:
                    break
                my_file.write(word + '\n')
                count += 1

        print("Dictionary list generated: " + output_file)


if __name__ == "__main__":
    main()
