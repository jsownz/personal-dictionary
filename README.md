# Personal Dictionary Generator

Generate a dictionary list as a text file using permutations of terms that are entered by the user into a JSON file. Terms are intended to be accumulated during information gathering phase of a penetration test. The more relevant the terms, the higher chance of success. Terms are in categories that are similar to those of security questions or personal terms one would be prone to remember.

## Usage

For authorized testing only. The biggest takeaway is perhaps what to not choose as a password.

Generate a dictionary list as a text file using permutations of terms. Data imported from populated JSON template 'config.json'.

PersonalDictionary.py [-h] --min MIN --max MAX -n NUM -f FILE

python3 PersonalDictionary.py --min 8 --max 12 -n 10000 -f config.json

![alt tag](https://raw.githubusercontent.com/MC-GitFlow/personal-dictionary/master/example/Usage.png)

![alt tag](https://raw.githubusercontent.com/MC-GitFlow/personal-dictionary/master/example/Screenshot.png)

## Future Features

Weighting of category significance.

Sub categories with common phrases.

Additional permutations from importing existing dictionaries.

Social Media Integration.

Possible integration of Flask or other UI.

Formatting for locales outside of U.S.

## History

Project started on June 18th of 2016 by John Vardanian

## Contributors

Development:
- John Vardanian
- ASC3ND

Testing and Feature Suggestions
- Jacob Wilkin
- leeJenks
