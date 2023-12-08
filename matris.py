import numpy as np
import re

def read_from_file(infile):
    '''Reads words from file and returns list of all words in said file.
    
    Parameters: infile (file)
    
    Return values: words (list of strings).'''
    words = []

    with open(infile, 'r', encoding="utf-8") as infile:
        word = [re.sub(r'[^a-zA-Z0-9\s]', '', line.strip()) for line in infile] #strips word and removes encoding-related special chars
        words.append(word)

        while word != '':
            word = infile.readline().strip()
            words.append(word) 

    words.pop()
    
    return words

def get_word_lists():
    '''Creates lists from files with calls to read_from_file() and returns them.
    
    Parameters: none
    
    Return values: word_list, unique_word_list (lists of strings).'''
    
    word_list = read_from_file('word_list.txt')
    unique_word_list = read_from_file('unique_word_list.txt')

    return word_list, unique_word_list

def create_matrix(unique_word_list, word_list):
    '''Creates transition matrix that contains the possibilities for a given word to come after another
    given word in a text, based on a list of all words in the text with, repetition, and another word
    list that contains all these words, but without repetition.
    
    Parameters:
    unique_word_list (list of strings)
    word_list (list of strings)
    
    Return values:
    markov (np array): the transition matrix
    lentot (int): the length of the unique word list'''

    #Gets all the indices that every unique word has in word_list and creates a matrix of these indices
    indexlist = []
    worddict = dict()
    for word in unique_word_list:
        indexlist.append([i for i, x in enumerate(word_list) if x == word])

    for inde in range(len(indexlist)):
        listnext = [] #list of all words that follow a given a word
        smalldict = dict()
        for i in indexlist[inde]:
	        if i != len(word_list)-1:
                    listnext.append(word_list[i+1])
        listnextuni = list(dict.fromkeys(listnext))
        for i in listnextuni:
            smalldict[i] = listnext.count(i)

        worddict[unique_word_list[inde]] = smalldict #in worddict, let the value of a unique word be how many times it occurs after a given word 

    lentot = len(unique_word_list)
    markov = np.zeros((lentot, lentot))

    #fill markov, the transition matrix, with probabilities
    for word1 in worddict:
        tot = sum(worddict.get(word1).values())
        for word in worddict.get(word1).keys():
                markov[unique_word_list.index(word), unique_word_list.index(word1)] = worddict.get(word1)[word]/tot

    #to save time when the program is not ran for the first time
    np.save('markov_matrix.npy', markov) 
    np.save('lentot_value.npy', lentot)

    return markov, lentot

def user_word(markov, lentot, unique_word_list):
    '''Asks user for word and prints the three words that are most likely to 
    follow that word in a sentence based on a list of words and a transition matrix.
    
    Parameters: 
    markov (np array): the transition matrix
    lentot (int): the length of unique_word_list
    unique_word_list (list of strings)
    
    Return values: none.'''

    prevword = input('Write word: ')
    if prevword in unique_word_list:
        wordvector = np.zeros((lentot,1))
        wordvector[unique_word_list.index(prevword),0] = 1

        nextwords = []

        for n in range(3):
            wordvector = markov.dot(wordvector)
            maxpos = next(i for i, x in enumerate(wordvector) if x == wordvector.max())
            nextword = unique_word_list[maxpos]
            if nextword in nextwords:
                wordvector_copy = wordvector.copy()
                wordvector_copy[maxpos] = 0 
                maxpos = next(i for i, x in enumerate(wordvector_copy) if x == wordvector_copy.max())
                nextword = unique_word_list[maxpos]
            nextwords.append(nextword)
        
        for word in nextwords:
            print(word)

    else:
        print('No data available for this word.')

def main():
    textlist, allword = get_word_lists()

    textlist = textlist[0]
    allword = allword[0]

    try:
        Markov = np.load('markov_matrix.npy')
        lentot = np.load('lentot_value.npy')
    except FileNotFoundError:
        Markov, lentot = create_matrix(allword, textlist)

    user_word(Markov, lentot, allword)

if __name__ == '__main__':
    main()
