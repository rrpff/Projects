# Enter a string and the program counts the number of vowels in the text. For added complexity have it report
# a sum of each vowel found.

import sys 

def main():
    words = "".join(sys.argv[1:])
    vowels = {"a":0,"e":0,"i":0,"o":0,"u":0}
    for letter in words:
        if letter in vowels:
            for vowel in vowels:
                if letter == vowel: vowels[vowel] += 1 
    print vowels

if __name__ == "__main__": 
    main()