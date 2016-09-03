class DictionaryDatabase(object):
    """ store terms by category, use mangler to permute and return """

    def __init__(self):
        """ Create dictionary of terms with mapping by category """
        self._categories = {}

    def add_category(self, category_name):
        """
            Add key to categories dictionary and assign empty dictionary
            :param category_name: key to reference category by
        """
        self._categories[category_name] = []

    def add_word(self, category_name, term):
        """
            Add term to specified category in categories dictionary
            :param category_name: name of category to append term to
            :param term: new term to add to specified category
        """
        self._categories[category_name].append(term)

    def get_words_in_category(self, category_name):
        """
            Display all words in specified category
            :param category_name: specified category to search for terms
            :return: all words assigned to specified category
        """
        return self._categories[category_name]
