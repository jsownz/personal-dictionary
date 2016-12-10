#!/usr/bin/env python3

"""
    Author: MC_GitFlow
    Last Modified: 2016-12-09
    Python 3

    Interactive menu to make use of manifest_core application
    Uses DictionaryDatabase module for book keeping.
"""

import json
import os
import DictionaryDatabase
import mangler

criteria = mangler.parse_json("config.json")
categories = [item for item in criteria if item[0] != "_"]
categories.sort()
word_list = DictionaryDatabase.DictionaryDatabase()


def show_categories():
    """
        Display current categories in database.
    """
    for item in word_list.get_category_names():
        print(item.replace("_", " ").title())


def show_words(active_category):
    """
        Show currently stored words in specified category
        :param active_category: Category to display words from
    """
    for item in word_list.get_words_in_category(active_category):
        print(item)


def add_category():
    """
        Add category to database of words.
        :return: true on success; false if category already exists
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
            print("\033[1;31mError: category not in database.\033[0m")
            return False
        else:
            print("\033[94mSelected category: " + category_selection +
                  "\033[0m")
            return selection
    except ValueError:
        print("\033[1;31mError: lease enter the name of a category.\033[0m")


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
        print("\033[1;31mError: please select a category.\033[0m")


def remove_word(active_category):
    """
        Remove word from specified category
        :param active_category: category to remove term from
    """
    if active_category:
        show_words(active_category)
        new_word = input("Enter word to remove: ")
        if word_list.remove_term(active_category, new_word):
            print("\033[94m" + new_word + " removed from category \""
                  + active_category + "\"\033[0m")
        else:
            print("\033[1;31mError: word \"" + new_word +
                  "\" not found in category \"" + active_category +
                  "\"\033[0m")
    else:
        print("\033[1;31mError: please select a category.\033[0m")


def show_category_words(active_category):
    """
        Display words within selected category.
        :param active_category: category to display words from
    """
    if active_category:
        print(word_list.get_words_in_category(active_category))
    else:
        print("\033[1;31mError: no category has been selected.\033[0m")


def add_list():
    """
        Prompt for path to 3rd party word list for import
    """
    return input("\033[94mEnter path to word list: ").strip()


def run_script(additional_list):
    """
        run the ManifestDictionary script with the interactive modifications
        :param additional_list: third party list to combine if specified
    """
    cfg_file = "config.json"
    with open(cfg_file, 'w') as outfile:
        json.dump(word_list.export_database(), outfile)
    use_list = False
    min_length = input("Enter minimum password length: ")
    max_length = input("Enter maximum password length: ")
    num_passwd = input("Enter max number of passwords: ")
    if additional_list:
        if input("Combine 3rd party list? [y/n]").strip() == "y":
            use_list = True
    execution_string = "python3 manifest_core.py"
    execution_string += " -f " + cfg_file
    if min_length:
        execution_string += " --min " + min_length
    if max_length:
        execution_string += " --max " + max_length
    if num_passwd:
        execution_string += " --num " + num_passwd
    if use_list:
        execution_string += " --input " + additional_list
    os.system(execution_string)


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
    additional_list = False
    main_menu = "\n\033[93m[+] *X* Manifest Dictionary *X* " \
                "[Personalized Generator]\033[92m\n\n" \
                "1) Show Categories\n" \
                "2) Select Category\n" \
                "3) Add Word to Category\n" \
                "4) Remove Word from Category\n" \
                "5) Show Words in Category\n" \
                "6) Import Existing List\n" \
                "7) Create Personalized Word List\n" \
                "99) Quit\n" \
                "\nOption:\033[0m "

    while True:
        try:
            selection = int(input(main_menu).strip())
        except ValueError:
            print("\n" * 100)
            print("\033[1;31mError: please enter a numeric value.\033[0m")
        else:
            print("\n" * 100)
            if selection == 1:
                show_categories()
            elif selection == 2:
                active_category = select_category()
            elif selection == 3:
                add_word(active_category)
            elif selection == 4:
                remove_word(active_category)
            elif selection == 5:
                show_category_words(active_category)
            elif selection == 6:
                additional_list = add_list()
            elif selection == 7:
                run_script(additional_list)
            elif selection == 99:
                break
            else:
                print(
                    "\033[1;31mError: please enter a valid menu number.\033[0m"
                )

    print("Exiting...")


if __name__ == '__main__':
    main()
