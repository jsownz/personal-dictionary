# Personal Dictionary Generator

Generate a dictionary list as a text file using permutations of terms that are entered by the user into a JSON file. Terms are intended to be accumulated during information gathering phase of a penetration test. The more relevant the terms, the higher chance of success. Terms are in categories that are similar to those of security questions or personal terms one would be prone to remember.

## Technical Notes

Current list generation code is for proof of concept of permutation algorithms and is to be replaced.

All interactions are through CLI.

Written using Python 3.5 with PyCharm, Atom, and Sublime Text 3.


## Usage

Generate a dictionary list as a text file using permutations of terms. Data imported from populated JSON template 'config.json'.

PersonalDictionary.py [-h] --min MIN --max MAX -n NUM -f FILE

python3 PersonalDictionary.py --min 8 --max 12 -n 10000 -f config.json

## Future Features

Weighting of category significance.

Social Media Integration.

Integration of flask or other UI.

## History

This is an alpha release for a project that began on June 18th of 2016

## Contributors

Development:
- John Vardanian
- ASC3ND

Testing and Feature Suggestions
- Jacob Wilkin
- leeJenks
