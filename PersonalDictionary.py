#!/usr/bin/env python

"""
    Author: John Vardanian
    Last Modified: 2016-06-30
    Python3.5 using PyCharm / Atom / Sublime Text 3

    r0.1.3.2-2016.06.30(a)

    Generate a dictionary list as a text file using permutations of terms
    stored in json file. Terms are intended to be accumulated during
    information gathering phase of a penetration test. The more relevant the
    terms, the higher chance of success.
"""

import argparse
import itertools
import json
import Mangler


def main():
    """
        ** All code below currently for testing and proof of concept **

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
                    "JSON template.\n\n"
    )
    parser.add_argument(
        '--min', type=int, required=False,
        help='Minimum password length'
    )
    parser.add_argument(
        '--max', type=int, required=False,
        help='Maximum password length'
    )
    parser.add_argument(
        '-n', '--num', type=int, required=False,
        help='Number of passwords to be generated'
    )
    parser.add_argument('-f', '--file', required=True,
                        help='Criteria file (JSON)')
    parser.add_argument('-o', '--out', help='Generated password file')
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
    else:
        print("\nPlease wait while your dictionary is generated... This may " +
              "take a while depending on the amount of data.\n")

        # use function 'mangle' for most common permutation
        pets = Mangler.mangle(criteria["pets"]) if criteria[
            "pets"] else []
        sports = Mangler.mangle(criteria["sports"]) if criteria[
            "sports"] else []
        family = Mangler.mangle(criteria["family"]) if criteria[
            "family"] else []
        music = Mangler.mangle(criteria["music"]) if criteria[
            "music"] else []
        states = Mangler.mangle(criteria["states"]) if criteria[
            "states"] else []
        cities = Mangler.mangle(criteria["cities"]) if criteria[
            "cities"] else []
        schools = Mangler.mangle(criteria["schools"]) if criteria[
            "schools"] else []
        colors = Mangler.mangle(criteria["colors"]) if criteria[
            "colors"] else []
        streets = Mangler.mangle(criteria["street_numbers"]) if criteria[
            "streets"] else []
        other = Mangler.mangle(criteria["other"]) if criteria[
            "other"] else []
        jobs = Mangler.mangle(criteria["employment"]) if criteria[
            "employment"] else []

        zip_codes = criteria["zip_codes"] if criteria["zip_codes"] else []
        phone_numbers = criteria["phone"] if criteria["phone"] else []

        # lists that don't make use of function 'mangle'
        phones = []
        years = []
        zips = []
        street_nums = []

        # populate lists that don't use function 'mangle'
        for phone in criteria["phone"]:
            phones.extend(Mangler.permute_phone(phone))

        for year in criteria["years"]:
            years.extend(Mangler.permute_year(year))

        for zip_code in criteria["zip_codes"]:
            zips.extend(Mangler.permute_zip_code(zip_code))

        for street_number in criteria["street_numbers"]:
            street_nums.extend(Mangler.perm_st_num(street_number))

        # add phone number to top of list
        final_collection[:0] = phones

        # lists to permute for base passwords
        collections = [
            pets, family, sports, schools, cities, music, states, jobs,
            streets, colors, other
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
