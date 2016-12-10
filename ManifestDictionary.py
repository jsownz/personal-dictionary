#!/usr/bin/env python3

"""
    Author: MC_GitFlow
    Last Modified: 2016-12-10
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
    full_count = 0
    for item in word_list.get_category_names():
        temp_count = len(word_list.get_words_in_category(item))
        full_count += temp_count
        print(item.replace("_", " ").title() + " (" + str(temp_count) + ")")
    print("\n" + str(full_count) + " total entries.")


def show_words(active_category):
    """
        Show currently stored words in specified category
        :param active_category: Category to display words from
    """
    for item in word_list.get_words_in_category(active_category):
        print(item)


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
        print("\033[1;31mError: please enter the name of a category.\033[0m")


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
        for item in word_list.get_words_in_category(active_category):
            print(item)
    else:
        print("\033[1;31mError: no category has been selected.\033[0m")


def add_list():
    """
        Prompt for path to 3rd party word list for import
    """
    file_name = input("\033[94mEnter path to word list: \033[0m").strip()
    if os.path.isfile(file_name):
        print("The final word list can now be combined with: " + file_name)
        return file_name
    else:
        print("\033[1;31mError: specified file not found.\033[0m")
        return False


def run_script(additional_list):
    """
        run the ManifestDictionary script with the interactive modifications
        :param additional_list: third party list to combine if specified
    """
    # todo: add type checking / validation
    cfg_file = "config.json"
    with open(cfg_file, 'w') as outfile:
        json.dump(word_list.export_database(), outfile)
    use_list = False
    print("Leave values blank for defaults.")
    min_length = input("Enter minimum password length: ")
    max_length = input("Enter maximum password length: ")
    num_passwd = input("Enter max number of passwords: ")
    out_name = input("Enter name for output file (include extension): ")
    if additional_list:
        if input("Combine 3rd party list? [y/n]: ").strip().lower() == "y":
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
    if out_name:
        execution_string += " --out " + out_name.strip()
    os.system(execution_string)


def clear_categories():
    """
        Remove all words from all categories for the config file
    """
    if input("Are you sure you want to remove *all* words "
             "from the config file? [y/n]: ").strip().lower() == "y":
        word_list.clear_all_categories()
        add_blank_lines()
        print("All words have been removed from the configuration file.")


def add_blank_lines():
    """
        Print 100 blank lines to reduce clutter
    """
    print("\n" * 100)


def main():
    """
        Begin interactive menu for Manifest Dictionary
    """
    add_blank_lines()

    for item in categories:
        word_list.add_category(item)

    for category in categories:
        for term in criteria[category]:
            word_list.add_word(category, term)

    active_category = False
    additional_list = False
    first_run = True

    while True:
        try:
            main_menu = "\n\033[93m[+] *X* Manifest Dictionary *X* " \
                        "[Personalized Generator]\n\n" \
                        "\033[94mFormats - Years: #### Zip Codes: " \
                        "##### Phone Numbers: ##########\033[95m"
            if first_run:
                main_menu += "\033[95m\n\nUse the options below to " \
                             "generate a personalized dictionary list." \
                             "\n \033[91m-> Interactive mode is " \
                             "still in beta <-\033[95m\n\nTerms are " \
                             "loaded into categories stored inside the " \
                             "\"config.json\"\nfile in the script directory."
            main_menu += "\033[92m\n\nSelected Category: "
            if active_category:
                main_menu += "\033[94m" + active_category + "\033[92m"
            else:
                main_menu += "\033[1;31mNot Selected\033[92m"
            main_menu += "\n\n1) Show Categories & Word Count\n" \
                         "2) Select Category\n" \
                         "3) Add Word to Category\n" \
                         "4) Remove Word from Category\n" \
                         "5) Show Terms in Category\n" \
                         "6) Import Existing List\n" \
                         "7) Remove All Words\n" \
                         "8) Display Help From Core Script\n" \
                         "9) Generate Final Word List\n" \
                         "99) Quit\n" \
                         "\nOption:\033[0m "
            selection = int(input(main_menu).strip())
        except ValueError:
            add_blank_lines()
            print("\033[1;31mError: please enter a numeric value.\033[0m")
        else:
            first_run = False
            add_blank_lines()
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
                clear_categories()
            elif selection == 8:
                os.system("python3 manifest_core.py -h")
            elif selection == 9:
                run_script(additional_list)
                break
            elif selection == 99:
                break
            else:
                print(
                    "\033[1;31mError: please enter a valid menu number.\033[0m"
                )

    print("Exiting...")


if __name__ == '__main__':
    main()
