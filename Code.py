'''
#Uncomment this to download nltk database
import nltk
nltk.download()
'''
from __future__ import print_function #allows use of python 3.x print funtion in place of python 2.x print statement
from nltk.corpus import wordnet as wn
import pyttsx
import webbrowser
import random
import string



def black(n, inputt_array_copy, word_array_copy, whites):
    """
    The module compares user input word with the word chosen by computer and prints
    the no. of letters in the user's word which are present in the computer's word,
    but not present in the right position
    :param n: length of word
    :param inputt_array_copy: an array of characters of user's input word
    :param word_array_copy: an array of characters of computer's chosen word
    :param whites: no. of letters in user's word which are in the right position in computers word
    :return: void
    """
    blacks = 0
    #print(word_array_copy)
    #print("hi")
    for i in range (0,n):
        for j in range(0,n):
            if(word_array_copy[i]!='*'):
             if(word_array_copy[i]==inputt_array_copy[j]):
                inputt_array_copy[j]='$'
                #print("hi")
                #print(word_array_copy)
               # print(inputt_array_copy)
                break
    for i in range(0,n):
        if(inputt_array_copy[i]=='$'):
            blacks+=1
    print (blacks, "Bulls ",whites,"Cows")

def whites(n, word_array_copy, inputt_array_copy):
    """
    This module compares the user's input word with computer's chosen word and calculates
    the no. of letters in user's word which are in the right position in the computer's word
    :param n: length of words
    :param word_array_copy:an array of characters of computer's chosen word
    :param inputt_array_copy:an array of characters of user's input word
    :return: void
    """
    whites = 0
    #print(inputt_array_copy)
    #print(word_array_copy)
    for i in range(0, n):
        if word_array_copy[i] == inputt_array_copy[i]:
            inputt_array_copy[i] = '*'
            word_array_copy[i]='*'
            whites+=1
    #print(inputt_array_copy)
    blacks = black(n,inputt_array_copy,word_array_copy,whites)


WORDLIST_FILENAME = "wordlist.txt"
#importing wordlist text file

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split(',')
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def definition(syns):
    """
    The function to print definition of the word
    :param syns: it is a synset of the word selected by the computer
    :return:void
    """
    print ("DEFINITION")
    print(syns[0].definition())

def TextToSpeech(syns,inputt):
    """
    text to speech module which is used to read out the word and definition aloud to the user
    :param syns:
    :param inputt:word chosen by computer
    :return: void
    """
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-85)
    engine.say(inputt)
    engine.say(syns[0].definition())
    engine.runAndWait()

def synonyms(inputt, syns):
    """
    This module displays all the synonyms of the word selected by the computer
    :param inputt:the word to be guessed
    :param syns: synset of the word selected by the computer
    :return: void
    """
    synonyms = syns[0].lemmas()[0].name()
    #syn =[str(lemma.name()) for lemma in wn.synset('dog.n.01').lemmas()]
    #print(syn)
    if synonyms == inputt:
        pass
    else:
        print ("SYNONYMS")
        print (synonyms)

def examples(syns):
    """
    used to display example sentences for the word
    :param syns: synset of the word selected by the computer
    :return: void
    """
    examples = syns[0].examples()
    n = len(examples)
    if examples == []:
        pass
    else:
        print("EXAMPLES")
        if n==1:
            print (examples[0])
        else:
            for i in range(0,n):
                print(i+1,". ",examples[i])

def ConnectToWeb(inputt):
    """
    This module is used to show a picture for thw word and the words prnounciation
    by connecting to an online dictionary "ipicthat"
    :param inputt: the word selected by the computer
    :return:void
    """
    new = 2 #for a new tab
    url = "http://www.ipicthat.com/index.php?m=dictionary&t=az&w="+inputt
    print(url)
    webbrowser.open(url,new=new)

def vocab(inputt):
    """
    Vocabulary module is used for displaying the meanings,synonyms,read out definition
    and show a picture related to the word
    :param inputt: word selected by the computer
    :return:void
    """
    syns = wn.synsets(inputt)
    '''
    A synset is a group of words expressing a similar theme(synonyms)
    this is how the words are stored in wordnet database.
    each synonym can be accessed through lemmas.
    syns[0] stores the word for which we are searching
    '''
    definition(syns)
    TextToSpeech(syns,inputt)
    synonyms(inputt, syns)
    examples(syns)
    ConnectToWeb(inputt)

def CnB(word):
    n = len(word)
    word_array = list(word)
    count = 0
    var = 1
    while var:
        count+=1
        inputt = raw_input("Guess " + str(n)+ " letter word?")
        if len(inputt)!=n:
            print ("OOPS! Enter only ",n, " digit word")
            continue
        inputt_array = list(inputt)
        if inputt == word:
            print ("You made it in ",count," attempts")
            var = 0
        else:
            #print(word_array)
            word_array_copy=list(word_array)
            inputt_array_copy=list(inputt_array)
            whites(n,word_array_copy,inputt_array_copy)





def is_word_guessed(guesslist,guessedlist):
    count=0
    for char in guesslist:
        if char in guessedlist:
            count+=1
    if count==len(guesslist):
        return 1
    else:
        return 0

def get_guessed_word(sword,guessedlist):
    word=[]
    print("Word:" ,end=" ")
    for i in range(0,len(sword)):
        if sword[i] in guessedlist:
            word.append(sword[i])
        else:
            word.append(' _')
        print(word[i],end=" ")
    print()

def inputt(letter,guesslist,guesses,warnings,guessedlist):
    if letter in guessedlist:
        print("Ooops!You hae already guessed that!")
        if warnings>0:
            warnings-=1
        elif warnings==0:
            guesses-=1
    else:
        if letter in guesslist:
            print("Good Guess!!")
        else:
            print("Ooops! That's not in my word!")
            guesses-=1
    if letter not in guessedlist:
        guessedlist.append(letter)

    return guesses,warnings,guessedlist

def available(guessedlist):
    avail=[]
    alphabets='abcdefghijklmnopqrstuvwxyz'
    print("Available letters:",)
    for char in alphabets:
        if char not in guessedlist:
            avail.append(char)
            print(char,end=" ")
    print()

def score(guesses,n):
    return guesses*n

def Hangman(sword):
    guesslist=[]
    print("I am thinking of a ",len(sword)," letter word")
    for char in sword:
        if char not in guesslist:
            guesslist.append(char)
    guessedlist=[]
    warnings=3
    guesses=int(1.5*len(sword))
    while guesses!=0:
        print("you have ",guesses,"guesses and ",warnings,"warnings remaining")
        letter=raw_input("enter a letter")
        if letter not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            print("Ooops thats not a letter guess again")
            letter=raw_input("enter a letter")
        guesses,warnings,guessedlist=inputt(letter,guesslist,guesses,warnings,guessedlist)
        j=is_word_guessed(guesslist,guessedlist)
        get_guessed_word(sword,guessedlist)
        if j==1:
            print("you won")
            print("Score:",score(guesses,len(guesslist)))
            vocab(sword)
            exit(0)
        available(guessedlist)
    print("you lost")
    print(sword)



"""
The main module where the computer selects a random word from the wordlist and asks the user to select a game to learn the word
"""
wordlist=load_words()
word = choose_word(wordlist)
#print(word)
choice=raw_input("Do you want to play 1.Cows or Bulls or 2.Hangman select 1 or 2")
if(choice == '1'):
    CnB(word)
elif(choice == '2'):
    Hangman(word)
else:
    print("invalid choice try again")
    choice=raw_input("Do you want to play 1.Cows or Bulls or 2.Hangman select 1 or 2")
vocab(word)

