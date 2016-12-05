#!/usr/bin/env python3

"""
    Author: MC_GitFlow
    Last Modified: 2016-12-04
    Python 3
"""

import DictionaryDatabase
import mangler

criteria = mangler.parse_json("config.json")
categories = [item for item in criteria if item[0] != '_']
categories.sort()
word_list = DictionaryDatabase.DictionaryDatabase()


def main():
    for item in categories:
        word_list.add_category(item)

    for category in categories:
        for term in criteria[category]:
            word_list.add_word(category, term)

    main_menu = "[+] Select an option\n\n" \
                "1) Show Categories\n" \
                "2) Add Categories\n" \
                "3) Select Category\n" \
                "4) Add Dictionary\n" \
                "5) Quit\n" \
                "\nSelection: "

    while True:
        try:
            selection = int(input(main_menu))

            if selection == 1:
                print(word_list.get_category_names())
            elif selection == 2:
                print("Pass")
            elif selection == 3:
                print("Pass")
            elif selection == 4:
                print("Pass")
            elif selection == 5:
                break
            else:
                print("Please enter a valid menu number.")

        except ValueError:
            print("Please enter a numeric value.")


if __name__ == '__main__':
    main()
