#!/usr/bin/env python3

"""
    Author: MC_GitFlow
    Last Modified: 2016-07-24
    Python3.5 using PyCharm
    r0.3-2016.07.24(b)

    -----
    Usage
    -----
    optional arguments:
      -h, --help            show this help message and exit
      --min MIN             Minimum password length
      --max MAX             Maximum password length
      -n NUM, --num NUM     Number of passwords to be generated
      -f FILE, --file FILE  Criteria file (JSON)
      -i INPUT, --input INPUT
                            Wordlist to mix with results generated from
                            criteria
      -o OUT, --out OUT     Generated password file
"""

import Mangler


def main():
    """
        Generate a dictionary list as a text file using permutations of terms
        imported from a JSON file. Terms are intended to be accumulated during
        information gathering phase of a penetration test.
    """

    print("\n*X* Dictionary Manifest *X* [Personalized Generator]\n")

    args, criteria, max_length, min_length, output, pw_count = \
        Mangler.parse_args()

    try:
        criteria = Mangler.parse_json(args.file)
    except FileNotFoundError as fnf_e:
        exit(u"Could not open criteria file: {0:s}".format(fnf_e.strerror))
    else:
        print("\nPlease wait while your dictionary is generated... This may " +
              "take a while depending on the amount of data.\n")

        # create permutations of individual categories
        collections, other, phone_numbers, phones, street_nums, years, zips = \
            Mangler.permute_criteria(criteria)

        # combine permutations of multiple categories
        combinations = Mangler.permute_collections(collections)

        # combine permutations of category "other" with itself
        Mangler.permute_other(combinations, other)

        # combine current lists and add common suffixes
        results = phones + combinations + Mangler.add_suffixes(
            combinations,
            phone_numbers,
            street_nums,
            years,
            zips)

        # consolidate all lists of data from JSON file
        results = Mangler.consolidate_final(
            # sort for more probable passwords to be towards start of list
            Mangler.sort_words(
                # remove duplicates and enforce length limitations
                Mangler.clean_list(
                    max_length,
                    min_length,
                    results)))

        # combine with 3rd party list if present and save results to file
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
