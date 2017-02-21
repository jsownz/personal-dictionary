#!/usr/bin/env python3

"""
    Author: MC_GitFlow
    Last Modified: 2017-01-08
    Python 3

    Generate a dictionary list as a text file using permutations of terms
    imported from a JSON file. Specify maximum number of passwords, min and
    max length of passwords, and combine with existing 3rd party lists.
    Terms are intended to be accumulated during information gathering phase of
    a penetration test.
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
    return mangler.consolidate_final(
        mangler.sort_words(
            mangler.clean_list(
                max_length,
                min_length,
                results)))


def save_dictionary(user_params, results):
    """
        Combine with 3rd party list if present and save results to file

        :param user_params: parameters from CLI call
        :param results: finalized collection of permuted criteria
    """
    mangler.generate_dictionary(
        mangler.read_input_list(
            user_params["args"],
            user_params["max_length"],
            user_params["min_length"]),
        user_params["output_file"],
        user_params["pw_count"],
        results)


def main():
    """
        Generate a dictionary list as a text file using permutations of terms
        imported from a JSON file.
    """

    print("\n*X* Manifest Dictionary *X* [Personalized Generator]\n")

    user_params = mangler.store_cli_args()

    try:
        criteria = mangler.parse_json(user_params['args'].file)
    except FileNotFoundError as fnf_e:
        exit(u"Could not open criteria file: {0:s}".format(fnf_e.strerror))
    else:
        print("\nPlease wait while your dictionary is generated...\n")

        # create permutations of individual categories
        collections, other, phone_numbers, phones, \
            street_nums, years, zips, birthdays = mangler.permute_criteria(criteria)

        # combine permutations of multiple categories
        combinations = mangler.permute_collections(collections)

        # combine permutations of category "other" with itself
        mangler.permute_other(combinations, other)

        # combine current lists and add common suffixes
        results = phones + combinations + mangler.add_suffixes(
            combinations, phone_numbers, street_nums, years, zips, birthdays)

        # enforce lengths, sort to push probable passwords to top, remove dupes
        results = finalize_collection(
            user_params["max_length"], user_params["min_length"], results)

        # generate txt file of wordlist, combine with any third party lists
        save_dictionary(user_params, results)

        print("Dictionary list generated: generated/" + user_params["output_file"])


if __name__ == "__main__":
    main()
