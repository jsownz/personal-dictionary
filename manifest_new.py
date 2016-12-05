#!/usr/bin/env python3

"""
    Author: MC_GitFlow
    Last Modified: 2016-12-05
    Python 3
"""

import DictionaryDatabase
import mangler

criteria = mangler.parse_json("config.json")
categories = [item for item in criteria if item[0] != "_"]
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
        :return: bool
    """
    new_category = input("Enter category name: ").strip()
    category_name = new_category.strip().replace(" ", "_").lower()
    if word_list.add_category(category_name):
        print("Added category " + new_category)
        return True
    print("Category already exists.")
    return False


def select_category():
    """
        Choose active category.
        :return: false if category not in database, otherwise key for category
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


def remove_word(active_category):
    """
        Remove word from specified category
        :param active_category: category to remove term from
    """
    if active_category:
        new_word = input("Enter word to remove: ")
        if word_list.remove_term(active_category, new_word):
            print(new_word + " removed from category \""
                  + active_category + "\"")
        else:
            print("Word \"" + new_word + "\" not found in category "
                  + active_category)
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
    main_menu = "\n[+] Menu - *X* Manifest Dictionary *X* " \
                "[Personalized Generator]\n\n" \
                "1) Show Categories\n" \
                "2) Add Categories\n" \
                "3) Select Category\n" \
                "4) Add Word to Category\n" \
                "5) Remove Word from Category\n" \
                "6) Show Words in Category\n" \
                "7) Create Personalized Word List\n" \
                "99) Quit\n" \
                "\nOption: "

    while True:
        try:
            selection = int(input(main_menu).strip())
        except ValueError:
            print("Please enter a numeric value.")
        else:
            if selection == 1:
                show_categories()
            elif selection == 2:
                add_category()
            elif selection == 3:
                active_category = select_category()
            elif selection == 4:
                add_word(active_category)
            elif selection == 5:
                remove_word(active_category)
            elif selection == 6:
                print(word_list.get_words_in_category(active_category))
            elif selection == 7:
                print("Coming soon.")
            elif selection == 99:
                print("Exiting...")
                break
            else:
                print("Please enter a valid menu number.")
        finally:
            pass


if __name__ == '__main__':
    main()
