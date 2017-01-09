# Manifest Dictionary

**For authorized testing only. The biggest takeaway is perhaps what to not choose as a password.**

A brute force attack attempts to determine a secret by trying every possible combination. A dictionary attack is typically a guessing attack which uses a pre-compiled list of information. Rather than trying every option, it only tries combinations which are likely to work.

In current times most brute force attacks against sufficiently chaotic passwords are unlikely to be successful within a reasonable time frame. A dictionary attack on the other hand retains its relevance in the insistence of so many users creating passwords that are based off of predictable information easily found through OSINT (information such as pet names, sports, family members, etc).

Manifest Dictionary quickly generates an intelligent wordlist using permutations of terms stored within a JSON file. The file can be manually edited via a text editor, or populated dynamically when ManifestDictionary.py is ran. View the contents of 'config.json' for further clarity. Terms are accumulated during the information gathering stage of a penetration test. The more relevant the terms in respect to the target: the higher chance of success.

Existing wordlists can be imported and combined during generation of personalized lists.

Included lists are from: https://github.com/MC-GitFlow/SecLists

Development is ongoing and relative to the scope of desired functionality the current release is in alpha. Hopefully this project will be deprecated through the education and awareness of encrypted password management applications, or by altogether replacing the insecure concept of a password.

## Usage

Directions below are for manual usage of manifest_core.py
Image is of interactive primary script.

Note: Requires Python 3

```
*X* Manifest Dictionary *X* [Personalized Generator]

usage: ManifestDictionary.py [-h] [--min MIN] [--max MAX] [-n NUM] -f FILE
                             [-i INPUT] [-o OUT]

Generate a dictionary list as a text file using permutations of terms. Data
imported from populated JSON template.

optional arguments:
  -h, --help            show this help message and exit
  --min MIN             Minimum password length
  --max MAX             Maximum password length
  -n NUM, --num NUM     Number of passwords to be generated
  -f FILE, --file FILE  Criteria file (JSON)
  -i INPUT, --input INPUT
                        Wordlist to mix with results generated from criteria
  -o OUT, --out OUT     Generated password file
```


![alt tag](https://raw.githubusercontent.com/MC-GitFlow/personal-dictionary/master/example/Usage.png)

## Future Features

Weighting of category significance.

Social Media Integration.

Possible integration of Flask or other UI.

Formatting for locales outside of U.S.

## History

Project started on June 18th of 2016 by MC_GitFlow

## Contributors

Development:
- MC_GitFlow
- ASC3ND
- jsownz

Testing and Feature Suggestions
- Jacob Wilkin
- leeJenks
