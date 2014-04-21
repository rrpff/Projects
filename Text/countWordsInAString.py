# Counts the number of individual words in a string. For added complexity read these strings in from a text file
# and generate a summary.

import sys

def main():
    count = 0
    words = sys.argv[1:]
    for word in words:
        count += 1
    print count

if __name__ == "__main__": 
    main()