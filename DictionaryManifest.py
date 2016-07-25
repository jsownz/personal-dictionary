#!/usr/bin/env python3

"""
    Author: MC_GitFlow
    Last Modified: 2016-07-24
    Python3.5 using PyCharm

    r0.3-2016.07.24(b)

    Generate a dictionary list as a text file using permutations of terms
    stored in JSON file. Terms are intended to be accumulated during
    information gathering phase of a penetration test. The more relevant the
    terms, the higher chance of success. See template 'config.json'
"""

import Mangler


def main():
    """
        Receive arguments from call to CLI. Permute using code testing
        functions above.

        Generate personalized dictionary list of passwords, tailored towards a
        target with information gathered during initial phase of pen test.
    """
    print("\n*X* Dictionary Manifest *X* [Personalized  Generator]\n")

    args, criteria, max_length, min_length, output, pw_count = \
        Mangler.parse_args()

    try:
        criteria = Mangler.parse_json(args.file)
    except FileNotFoundError as fnf_e:
        exit(u"Could not open criteria file: {0:s}".format(fnf_e))
    else:
        print("\nPlease wait while your dictionary is generated... This may " +
              "take a while depending on the amount of data.\n")

        collections, other, phone_numbers, phones, street_nums, years, zips = \
            Mangler.permute_criteria(criteria)
        combinations = Mangler.permute_collections(collections)
        Mangler.permute_other(combinations, other)
        results = phones + combinations + Mangler.add_suffixes(
            combinations,
            phone_numbers,
            street_nums,
            years,
            zips)
        results = Mangler.consolidate_final(
            Mangler.sort_words(
                Mangler.clean_list(
                    max_length,
                    min_length,
                    results)))

        Mangler.generate_dictionary(
            Mangler.read_input_list(
                args,
                max_length,
                min_length),
            output,
            pw_count,
            results)
        print("Dictionary list generated: " + output)


if __name__ == "__main__":
    main()
