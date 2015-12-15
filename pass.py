#!/usr/bin/env python3

from subprocess import Popen, PIPE
from random import randint

print()
number_of_words = int(input('How many words? '))
passphrase = ''
n = 0

while n < number_of_words:
    repeat = False

    # Grab a random word. Decode from binary to ascii.
    word = Popen(['shuf', '-n1', '/usr/share/dict/words'], stdout=PIPE, shell=False).communicate()[0].decode('ascii')

    # Check word for apostrophe; discard if true.
    for c in word:
        if c == "'":
            repeat = True
            break
        else:
            repeat = False

    # Add word to list
    if repeat == False:
        passphrase += (word.strip('\n').capitalize() + str(randint(1,9)))
        n += 1

print()
print(passphrase)
print()
