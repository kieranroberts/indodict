import re

global vo, co, vowels, consonants 
vo = '[aeiou]'
co = '[bcdfghjklmnpqrstvwxyz]'
vowels = list(vo[1:-1])
consonants = list(co[1:-1])



# A function that creates a dictionary whose keys are the vowels of the word 
# s and values are the frequencies of each vowel.
def getVowels(s):
    svowels = dict()
    for a in s:
        if a in vowels:
            if a in svowels.keys():
                svowels[a] += 1
            else:
                svowels[a] = 1
    return svowels

# A function that creates a dictionary whose keys are the consonants of the word 
# s and values are the frequencies of each consonant.

def getConsonants(s):
    sconsonants = dict()
    for a in s:
        if a in consonants:
            if a in sconsonants.keys():
                sconsonants[a] += 1
            else:
                sconsonants[a] = 1
    return sconsonants
   

# Length of a word. It excludes non-alphabetic symbols such as the '-'.
def wordLength(word):
    return len([x for x in word if x.isalpha()])
    
# Remove the vowels of a word to form a sequence of consonants
def getConsonantSeq(s):
    return ''.join([x for x in s if x in consonants])




################################################################################
# Define two common patterns we are interested in and functions that detect him.
#

def altPattern(s,t,n):
    r = n % 2
    return (s+'{1}'+t+'{1}')*(n/2)+(s+'{1}')*r

def vowelSepPattern(s,t,nv):
    # n is the number of vowels in your pattern
    if s == vo:
        return (s + '{1}') + (t +'{1,}'+ s +'{1}')*(nv-1) + (t+'{0,}')
    else:
        return (s+'{1,}'+t+'{1}')*nv + (s + '{0,}')

def hasAltPattern(s):
    n = wordLength(s)
    patternOne = altPattern(vo,co,n)
    patternTwo = altPattern(co,vo,n)
    if bool(re.search('^'+patternOne+'$',s)) or \
        bool(re.search('^'+patternTwo+'$',s)):
        return True
    else:
        return False

def hasVowelSepPattern(s):
    nv = sum(getVowels(s).values())
    patternOne = vowelSepPattern(vo,co,nv)
    patternTwo = vowelSepPattern(co,vo,nv)    
    if bool(re.search('^'+patternOne+'$',s)) or \
        bool(re.search('^'+patternTwo+'$',s)):
        return True
    else:
        return False
#
################################################################################
