# Implement a Caesar cipher, both encoding and decoding. The key is an integer from 1 to 25. This cipher rotates
# the letters of the alphabet (A to Z). The encoding replaces each letter with the 1st to 25th next letter
# in the alphabet (wrapping Z to A). So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to
# "BC". This simple "monoalphabetic substitution cipher" provides almost no security, because an attacker who has the encoded message can either
# use frequency analysis to guess the key, or just try all 25 keys.

import sys

def encode(content,key):
    res = ""
    alpha = [chr(i + 97) for i in xrange(26)]
    letters = "".join(content).split()[0]
    for letter in letters:
        if letter in alpha:
            print letter,chr(ord(letter) + int(key))

# def decode(content,key):
    # return

def main():
    # Usage [encode|decode] [key] [content]
    key = sys.argv[2]
    content = sys.argv[3:]
    if sys.argv[1] == "encode": encode(content,key)
    else: decode(content,key)

if __name__ == "__main__": 
    main()