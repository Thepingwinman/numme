import numpy as np
import matplotlib.pyplot as plt

def read_from_file(infil):
    '''Reads words from file and returns list of all words in said file.
    
    Parameters: infil (file)
    
    Return values: words (list of strings).'''
    words = []

    with open(infil, 'r') as infil:
        word = infil.readline().strip()
        words.append(word)

        while word != '':
            word = infil.readline().strip()
            words.append(word) 

    words.pop()
    
    return words

def get_word_lists():
    '''Creates lists from files with calls to read_from_file() and returns them.
    
    Parameters: none
    
    Return values: word_list, unique_word_list (lists of strings).'''
    
    word_list = read_from_file('word_list.txt')
    unique_word_list = read_from_file('unique_word_list.txt')

    #print(word_list, unique_word_list)

    #print(f'längd word_list: {len(word_list)}; längd unique_word_list: {len(unique_word_list)}')

    return word_list, unique_word_list

def write2file(matrix, file_name):
    ''''Writes a matrix to a file.
    
    Parameters: 
    matrix (numpy matrix)
    file_name (str): name of outfile.
    
    Return values: none.'''

    with open(file_name, 'w') as outfile:
            outfile.write(matrix)

textlist, allword = get_word_lists()

''' 
allword = []    # listan med alla unika ord
textlist = []    # listan med texten i listform
'''

indexlist = []
worddict = dict()
for word in allword:
    indexlist.append([i for i, x in enumerate(textlist) if x == word])

for inde in range(len(indexlist)):
    listnext = []
    smalldict = dict()
    for i in indexlist[inde]:
	    if i != len(textlist)-1:
		    listnext.append(textlist[i+1])
    listnextuni = list(dict.fromkeys(listnext))
    for i in listnextuni:
        smalldict[i] = listnext.count(i)
    worddict[allword[inde]] = smalldict

lentot = len(allword)
Markov = np.zeros((lentot, lentot))     # Skapar matris med enbart 0or

for word1 in worddict:
    tot = sum(worddict.get(word1).values())
    for word in worddict.get(word1).keys():
        Markov[allword.index(word), allword.index(word1)] = worddict.get(word1)[word]/tot

write2file(Markov, 'Markov_matris.txt')

''' 
prevword = input('Write word ')
if prevword in allword:     # Kollar efterföljande ord
    wordvector = np.zeros((lentot,1))
    wordvector[allword.index(prevword),0] = 1
    for n in range(3):
        wordvector = Markov.dot(wordvector)
        maxpos = next(i for i, x in enumerate(wordvector) if x == wordvector.max())
        nextword = allword[maxpos]
        print(nextword)
'''
