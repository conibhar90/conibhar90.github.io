# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    
    scoreList = []
    
    for letter in word:
        scoreList.append(SCRABBLE_LETTER_VALUES[letter])
    
    score = sum(scoreList)*len(word)
    
    if len(word) == n:
        score += 50
    
    return score
        
        



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    
    handTemp = hand.copy()
    
    for letter in word:
        if handTemp[letter] > 0:
            handTemp[letter] -= 1
    
    return handTemp
            



#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    
    handTemp = hand.copy()
    handList = []
    
    for key in handTemp:
        handList.append(key)
    
    for letter in word:
        if letter in handList:
            if handTemp[letter] > 0:
                handTemp[letter] -= 1
            else:
                return False
        else:
            return False
   
    
    if word in wordList:
        return True
    else:
        return False
        
    


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
   
    handStringList = []
    
    for key in hand:
        handStringList.append(key*hand[key])
    
    handString = ''.join(handStringList)
    
    return len(handString)
    
        
        


def playHand(hand, wordList, n):
   
    totalScore = 0# Keep track of the total score
    
    while calculateHandlen(hand) != 0:# As long as there are still letters left in the hand:
    
        displayHand(hand)# Display the hand
        
        word = (str(input('Enter word, or a "." to indicate that you are finished: '))).lower()# Ask user for input
        
        if word == '.':# If the input is a single period:
        
            break# End the game (break out of the loop)

            
        else:# Otherwise (the input is not a single period):
        
            if isValidWord(word, hand, wordList) == False:# If the word is not valid:
            
                print("Invalid word, please try again.")
                print("")# Reject invalid word (print a message followed by a blank line)

            else:# Otherwise (the word is valid):
                
                totalScore += getWordScore(word, n)
                print(word + " earned "+ str(getWordScore(word, n)) + " points. Total: " + str(totalScore))# Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                print("")
                hand = updateHand(hand, word)# Update the hand 
                

    if word == '.':
        print("Goodbye! Total score: " + str(totalScore) + " points." )# Game is over (user entered a '.' or ran out of letters), so tell user the total score
    
    else:
        print("Run out of letters. Total score: " + str(totalScore) + " points.")

#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # TO DO ... <-- Remove this comment when you code this function
    print("playGame not yet implemented.") # <-- Remove this line when you code the function
   



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
