#!/usr/bin/env python3

"""
    Author: MC_GitFlow
    Last Modified: 2016-12-05 11:18:02 CDT
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
    category_name = new_category.strip().replace(" ", "_").lower()
    if word_list.add_category(category_name):
        print("Added category " + new_category)
        return True
    return False


def select_category():
    """
        Choose active category.
        :return: bool|string
    """
    show_categories()
    category_selection = input("Please enter a category name: ")
    try:
        selection = str(category_selection.strip().replace(" ", "_").lower())
        if selection not in word_list.get_category_names():
            print("Category not in database.")
            return False
        else:
            print("Selected category: " + category_selection)
            return selection
    except ValueError:
        print("Please enter the name of a category.")


def add_word(active_category):
    """
        Add word to specified category.
        :param active_category: category to add new word to.
    """
    if active_category:
        new_word = input(
            "Add word to category " + str(active_category) + ": ")
        word_list.add_word(str(active_category), new_word)
    else:
        print("Please select a category.")


def main():
    """
        Begin interactive menu for Manifest Dictionary
    """
    for item in categories:
        word_list.add_category(item)

    for category in categories:
        for term in criteria[category]:
            word_list.add_word(category, term)

    active_category = False
    main_menu = "\n[+] Main Menu - *X* Manifest Dictionary *X* " \
                "[Personalized Generator]\n\n" \
                "1) Show Categories\n" \
                "2) Add Categories\n" \
                "3) Select Category\n" \
                "4) Add Word to Category\n" \
                "5) Show Words in Category\n" \
                "99) Quit\n" \
                "\nOption: "

    while True:
        try:
            selection = int(input(main_menu))

            if selection == 1:
                show_categories()
            elif selection == 2:
                if not add_category():
                    print("Category already exists.")
            elif selection == 3:
                active_category = select_category()
            elif selection == 4:
                add_word(active_category)
            elif selection == 5:
                print(word_list.get_words_in_category(active_category))
            elif selection == 99:
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
