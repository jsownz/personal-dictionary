#!/usr/bin/env python3

"""
    Author: MC_GitFlow
    Last Modified: 2017-01-29
    Python 3

    Interactive menu to make use of manifest_core script
    Uses BookKeeper class to manage content used for generating wordlist.

    Functions:
      > show_categories()
      > show_words(active_category)
      > select_category()
      > add_word(active_category)
      > remove_word(active_category)
      > show_category_words(active_category)
      > add_list()
      > run_script(additional_list)
      > clear_categories()
      > format_category(active_category)
      > script_help_display()
      > add_blank_lines()
"""

import json
import os
import BookKeeper
import mangler

# prep for import of words from the configuration file to a BookKeeper object
CRITERA = mangler.parse_json("config.json")
CATEGORIES = [item for item in CRITERA if item[0] != "_"]
CATEGORIES.sort()
WORD_LIST = BookKeeper.BookKeeper()


def show_categories():
    """
        Display current categories in database.
    """
    full_count = 0
    for item in WORD_LIST.get_category_names():
        temp_count = len(WORD_LIST.get_words_in_category(item))
        full_count += temp_count
        print(item.replace("_", " ").title() + " (" + str(temp_count) +
              " items)")
    print("\n" + str(full_count) + " total entries.")


def show_words(active_category):
    """
        Show currently stored words in specified category
        :param active_category: Category to display words from
    """
    words = WORD_LIST.get_words_in_category(active_category)
    print(str(len(words)) + " term(s) in category \"" +
          active_category.title() + "\"\n")
    for item in words:
        print(item)
    print("\n")


def select_category():
    """
        Choose active category.
        :return: false if category not in database, otherwise key for category
    """
    show_categories()
    cat_select = input("Please enter a category name (empty to cancel): ")
    try:
        if cat_select.strip() == "":
            print("\033[94mSelect category canceled.\033[0m")
        else:
            selection = str(cat_select.strip().replace(" ", "_").lower())
            if selection not in WORD_LIST.get_category_names():
                print("\033[1;31mError: category not in database.\033[0m")
                return False
            else:
                add_blank_lines()
                cat_select = cat_select.replace("_", " ").title()
                print("\033[94mSelected category: " + cat_select + "\033[0m")
                return selection
    except ValueError:
        print("\033[1;31mError: please enter the name of a category.\033[0m")


def add_word(active_category):
    """
        Add word to specified category.
        :param active_category: category to add new word to.
    """
    if active_category:
        show_words(active_category)
        new_word = input("Add word to category \"" + format_category(
            active_category) + "\" (empty to cancel): ")
        if new_word.strip() == "":
            print("\033[94mAdd Term Canceled.\033[0;34m")
        else:
            WORD_LIST.add_word(str(active_category), new_word)
    else:
        print("\033[1;31mError: please select a category.\033[0m")


def remove_word(active_category):
    """
        Remove word from specified category
        :param active_category: category to remove term from
    """
    if active_category:
        show_words(active_category)
        new_word = input("Enter term to remove (empty to cancel): ")
        if new_word.strip() == "":
            print("\033[94mRemoval Canceled.\033[0m")
        else:
            if WORD_LIST.remove_term(active_category, new_word):
                print("\033[94m" + new_word + " removed from category \"" +
                      active_category + "\"\033[0;34m")
            else:
                print("\033[1;31mError: word \"" + new_word +
                      "\" not found in category \"" +
                      format_category(active_category) +
                      "\"\033[0m")
    else:
        print("\033[1;31mError: please select a category.\033[0;34m")


def show_category_words(active_category):
    """
        Display words within selected category.
        :param active_category: category to display words from
    """
    if active_category:
        for item in WORD_LIST.get_words_in_category(active_category):
            print(item)
    else:
        print("\033[1;31mError: no category has been selected.\033[0;34m")


def add_list():
    """
        Prompt for path to 3rd party word list for import
    """
    file_name = input("\033[94mEnter path to word list: \033[0;34m").strip()
    if os.path.isfile(file_name):
        print("The final word list can now be combined with: " + file_name)
        return file_name
    else:
        print("\033[1;31mError: specified file not found.\033[0;34m")
        return False


def run_script(additional_list):
    """
        run the manifest_core script with the interactive modifications
        :param additional_list: third party list to combine if specified
    """
    # todo: add type checking / validation
    cfg_file = "config.json"
    with open(cfg_file, 'w') as outfile:
        json.dump(WORD_LIST.export_database(), outfile)
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
        WORD_LIST.clear_all_categories()
        add_blank_lines()
        print("All words have been removed from the configuration file.")


def format_category(active_category):
    """
        Print category formatted for readability
        :param active_category: specified category to print
    """
    return active_category.replace("_", " ").title()


def script_help_display():
    """
        Print the help section of manifest_core
    """
    os.system("python3 manifest_core.py -h")


def add_blank_lines():
    """
        Print 100 blank lines to reduce clutter
    """
    print("\n" * 100)


def main():
    """
        Begin interactive menu for Manifest Dictionary
        Menu selections use functions from above inside a loop
        to customize data used in wordlist generation.
    """

    # push other text in terminal window out of view
    add_blank_lines()

    # import categories from config data
    for item in CATEGORIES:
        WORD_LIST.add_category(item)

    # import category terms from config data
    for category in CATEGORIES:
        for term in CRITERA[category]:
            WORD_LIST.add_word(category, term)

    active_category = False  # category to be acted upon
    additional_list = False  # list to combine if specified
    first_run = True  # indicates to show directions on first run of loop

    # begin interactive menu loop
    while True:
        try:
            main_menu = "\n\033[93m[+] *X* Manifest Dictionary *X* " \
                        "[Personalized Generator]\n\n" \
                        "\033[94mFormats - Years: #### Zip Codes: " \
                        "##### Phone: ##########\033[95m"
            if first_run:
                main_menu += "\033[95m\n\nUse the options below to " \
                             "generate a personalized dictionary list." \
                             "\n \033[91m-> Interactive mode is " \
                             "still in beta <-\033[95m\n\nTerms are " \
                             "loaded into categories stored inside the " \
                             "\"config.json\"\nfile in the script directory."
            main_menu += "\033[92m\n\n    Selected Category: "
            if active_category:
                main_menu += "\033[94m" + \
                             format_category(active_category) + \
                             "\033[92m\n\n"
            else:
                main_menu += "\033[93mNot Selected\033[92m\n\n"
            main_menu += "    " \
                         "1) Show Categories & Word Count\n    " \
                         "2) Select Category\n    " \
                         "3) Add Word to Category\n    " \
                         "4) Remove Word from Category\n    " \
                         "5) Show Terms in Category\n    " \
                         "6) Import Existing List\n    " \
                         "7) Remove All Words\n    " \
                         "8) Display Help From Core Script\n    " \
                         "9) Generate Word List " \
                         "\033[91m(\033[93mOverwrites Config File" \
                         "\033[91m)\033[92m\n\n    " \
                         "99) Quit\n\n  " \
                         "Option:\033[0;34m "
            selection = int(input(main_menu).strip())
        except ValueError:
            add_blank_lines()
            print("\033[1;31mError: please enter a numeric value.\033[0;34m")
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
                script_help_display()
            elif selection == 9:
                run_script(additional_list)
                break
            elif selection == 99:
                break
            else:
                print(
                    "\033[1;31mError: please enter a valid option.\033[0;34m")

    print("Exiting...")


if __name__ == '__main__':
    main()
