#this file contains the original text
from contextlib import nullcontext


origin = open('origin.txt', 'r')

#set text to origin
text = origin.read()

#close the origin file
origin.close()

try:
    adjectivesfile = open('adjectives.txt', 'r')
except:
    adjectivesfile = open('adjectives.txt', 'w').close()
    adjectivesfile = open('adjectives.txt', 'r')

adjectives = adjectivesfile.read()

adjectivesfile.close()

try:
    nounsfile = open('nouns.txt', 'r')
except:
    nounsfile = open('nouns.txt', 'w').close()
    nounsfile = open('nouns.txt', 'r')

nouns = nounsfile.read()

nounsfile.close()

file = open('splashes.txt', 'w')

n = '\n'

for i in range(10):
    text = text + "poopy" + n
    
file.write(text)
    
file.close()
