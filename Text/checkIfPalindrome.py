# Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as
# backwards like racecar

import sys

def main():
    string = " ".join(sys.argv[1:])
    if string == string[::-1]:
        print "Palindrome!"
    else:
        print "Nope!"

if __name__ == "__main__": 
    main()