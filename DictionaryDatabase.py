"""
    DictionaryDatabase.py
    Author: MC_GitFlow
    Python3
    Last Modified: 2016-09-07 09:42:04 AM CDT

    Class methods:
        > add_category(self, category_name)
        > add_word(self, category_name, term)
        > get_words_in_category(self, category_name)
        > get_all_words(self)
        > get_category_names(self)
        > clear_category(self, category_name)
        > remove_term(self, category_name, term)
        > clear_all_categories(self)
        > reset_database(self)
"""


class DictionaryDatabase(object):

    """ Manage dictionary of terms mapped by categories """

    def __init__(self):
        """ Create dictionary of terms with mapping by category """
        self._categories = {}

    def add_category(self, category_name):
        """
            Add key to categories dictionary and assign empty dictionary
            :param category_name: key to reference category by
        """
        if category_name not in self._categories:
            self._categories[category_name] = []
            return True
        else:
            return False

    def add_word(self, category_name, term):
        """
            Add term to specified category in categories dictionary
            :param category_name: name of category to append term to
            :param term: new term to add to specified category
        """
        if category_name not in self._categories:
            self._categories[category_name] = [term]
            return True
        elif term not in self._categories[category_name]:
            self._categories[category_name].append(term)
            return True
        else:
            return False

    def get_words_in_category(self, category_name):
        """
            Display all words in specified category
            :param category_name: specified category to search for terms
            :return: all words assigned to specified category; False if nothing
        """
        if category_name in self._categories:
            return self._categories[category_name]
        else:
            return False

    def get_all_words(self):
        """
            Return a list of all words currently in instance
            :return: all words in words in instance or False if none present
        """
        word_list = []
        for category in self._categories:
            for item in self._categories[category]:
                word_list.append(item)
        if word_list:
            return word_list
        else:
            return False

    def get_category_names(self):
        """
            Return the name of all categories of present
            :return: list of category names or False if none
        """
        if self._categories:
            return [item for item in self._categories]
        else:
            return False

    def clear_category(self, category_name):
        """
            Remove all words from specified category if exists.
            :param category_name: category to remove words from
            :return: true if category found
        """
        if category_name in self._categories:
            self._categories[category_name] = []
            return True
        return False

    def remove_term(self, category_name, term):
        """
            Remove a term from specified category
            :param category_name: name of category to prune
            :param term: term to prune
            :return: true on success false if not found
        """
        if self._categories[category_name]:
            self._categories[category_name].remove(term)
            return True
        return False

    def clear_all_categories(self):
        """
            Remove all words present in each category
            :return: True on success; false if no categories present
        """
        if self._categories:
            for item in self._categories:
                self._categories[item] = []
            return True
        else:
            return False

    def reset_database(self):
        """
            Remove all categories and words
        """
        self._categories.clear()
