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

import mangler


def finalize_collection(max_length, min_length, results):
    """
        Consolidate all lists of data from JSON file, sort for more probable
        passwords to be towards start of list, remove duplicates and enforce
        length limitations

        :param max_length: upper bound char length on passwords
        :param min_length: lower bound length on pws
        :param results: permutations of criteria
        :return: list
    """
    results = mangler.consolidate_final(
        mangler.sort_words(
            mangler.clean_list(
                max_length,
                min_length,
                results)))
    return results


def save_dictionary(args, max_length, min_length, output, pw_count, results):
    """
        Combine with 3rd party list if present and save results to file

        :param args: parameters from CLI
        :param max_length: upper bound length on passwords
        :param min_length: lower bound length on pws
        :param output: name of file to save list as
        :param pw_count: maximum number of passwords to choose
        :param results: finalized collection of permuted criteria
    """
    mangler.generate_dictionary(
        mangler.read_input_list(
            args,
            max_length,
            min_length),
        output,
        pw_count,
        results)


def main():
    """
        Generate a dictionary list as a text file using permutations of terms
        imported from a JSON file. Terms are intended to be accumulated during
        information gathering phase of a penetration test.
    """

    print("\n*X* Dictionary Manifest *X* [Personalized Generator]\n")

    args, criteria, max_length, min_length, output, pw_count = \
        mangler.parse_args()

    try:
        criteria = mangler.parse_json(args.file)
    except FileNotFoundError as fnf_e:
        exit(u"Could not open criteria file: {0:s}".format(fnf_e.strerror))
    else:
        print("\nPlease wait while your dictionary is generated... This may " +
              "take a while depending on the amount of data.\n")

        # create permutations of individual categories
        collections, other, phone_numbers, phones, street_nums, years, zips = \
            mangler.permute_criteria(criteria)

        # combine permutations of multiple categories
        combinations = mangler.permute_collections(collections)

        # combine permutations of category "other" with itself
        mangler.permute_other(combinations, other)

        # combine current lists and add common suffixes
        results = phones + combinations + mangler.add_suffixes(
            combinations,
            phone_numbers,
            street_nums,
            years,
            zips)

        # enforce lengths, sort to push probable passwords to top, remove dupes
        results = finalize_collection(
            max_length, min_length, results)

        # generate txt file of wordlist, combine with any third party lists
        save_dictionary(
            args, max_length, min_length, output, pw_count, results)

        print("Dictionary list generated: " + output)


if __name__ == "__main__":
    main()
