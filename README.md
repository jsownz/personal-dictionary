# Personal Dictionary Generator

Generate a dictionary list as a text file using permutations of terms that are entered by the user into a JSON file. Terms are intended to be accumulated during information gathering phase of a penetration test. The more relevant the terms, the higher chance of success. Terms are in categories that are similar to those of security questions or personal terms one would be prone to remember.

This is an open project and all developers are welcome to join.

## Usage

For authorized testing only. The biggest takeaway is perhaps what to not choose as a password.

usage: PersonalDictionary.py [-h] --min MIN --max MAX -n NUM -f FILE [-o OUT]

Generate a dictionary list as a text file using permutations of terms. Data
imported from populated JSON template.

optional arguments:

  -h, --help            show this help message and exit
  
  --min MIN             Minimum password length
  
  --max MAX             Maximum password length
  
  -n NUM, --num NUM     Number of passwords to be generated
  
  -f FILE, --file FILE  Criteria file
  
  -o OUT, --out OUT     Generated password file

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
