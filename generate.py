import random

n = '\n'
phadjective = "<adj>"
phnoun = "<noun>"
phverb = "<verb>"
phadverb = "<adverb>"
phpreposition = "<prep>"
phinterjection = "<interj>"
phinteger = "<integer>"

def gettext(filename):
    try:
        f = open(filename, 'r')
    except:
        f = open(filename, 'w').close()
        f = open(filename, 'r')
    output = f.read()
    f.close()
    return output

def converttxttoarray(text):
    text = text.split(n)
    return text

def digestgrammar(t):
    output = ""
    for noun in nouns:
        output = output + t.replace(phnoun, noun) + n
    return output

#set the text that we will be adding onto
text = gettext('origin.txt')

#get adjectives from adjectives.txt
adjectives = gettext('adjectives.txt')

#get nouns from nouns.txt
nouns = converttxttoarray(gettext('nouns.txt'))

#get verbs from verbs.txt
verbs = converttxttoarray(gettext('verbs.txt'))

#get adverbs from adverbs.txt
adverbs = converttxttoarray(gettext('adverbs.txt'))

#get prepositions from prepositions.txt
prepositions = converttxttoarray(gettext('prepositions.txt'))

#get conjunctions from conjunctions.txt
conjunctions = converttxttoarray(gettext('conjunctions.txt'))

#get interjections from interjections.txt
interjections = converttxttoarray(gettext('interjections.txt'))

#get integers from integers.txt
integers = converttxttoarray(gettext('integers.txt'))

#get the setups from setups.txt
setups = converttxttoarray(gettext('setups.txt'))

def digestsetup(t):
    output = ""
    output = digestgrammar(t)
    return output

#open up splashes.txt in write mode so we can
#continue our trolling
splashes = open('splashes.txt', 'w')

for setup in setups:
    text = text + digestsetup(setup)
    
#write the text to the file and close it
splashes.write(text)
splashes.close()