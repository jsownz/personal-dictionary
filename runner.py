#!/usr/bin/env python3

"""
    Author: MC_GitFlow
    Last Modified: 2016-12-05 10:48:57 CDT
    Python 3
"""

import DictionaryDatabase
import mangler

criteria = mangler.parse_json("config.json")
categories = [item for item in criteria if item[0] != '_']
categories.sort()
word_list = DictionaryDatabase.DictionaryDatabase()


def show_categories():
    """
        Display current categories in database.
        :return: void
    """
    for item in word_list.get_category_names():
        print(item.replace("_", " ").title())


def add_category():
    """
        Add category to database of words.
        :return: void
    """
    new_category = input("Enter category name: ").strip()
    if word_list.add_category(new_category):
        print("Added category " + new_category)
    else:
        print("Category " + new_category + " already present.")


def select_category():
    """
        Choose active category.
        :return: void
    """
    show_categories()
    category_selection = input("Please enter a category name: ")
    try:
        selection = str(category_selection.strip().replace(" ", "_").lower())
        if not word_list.get_words_in_category(selection):
            print("Category not in database.")
        else:
            print("Selected category: " + category_selection)
    except ValueError:
        print("Please enter the name of a category.")


def main():
    """
        Begin interactive menu for Manifest Dictionary
    """
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
                show_categories()
            elif selection == 2:
                add_category()
            elif selection == 3:
                select_category()
            elif selection == 4:
                pass
            elif selection == 5:
                print("Exiting...")
                break
            else:
                print("Please enter a valid menu number.")

        except ValueError:
            print("Please enter a numeric value.")

        else:
            pass
        finally:
            pass


if __name__ == '__main__':
    main()
