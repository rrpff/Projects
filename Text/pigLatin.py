# Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of
# an English word the initial consonant sound is transposed to the end of the word and an ay is affixed
# (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.

import sys

def main():
    words = sys.argv[1:]
    latin = []
    vowels = ["a","e","i","o","u"]
    for word in words:
        if word.lower() == "a": latin.append("ay")
        elif word[0].lower() in vowels: latin.append(word+"-ay")
        else: latin.append(word[1:]+"-"+word[0].lower()+"ay")
    print " ".join(latin)

if __name__ == "__main__": 
    main()