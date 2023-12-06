import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re

def read_from_file(infil):
    '''Reads words from file and returns list of all words in said file.
    
    Parameters: infil (file)
    
    Return values: words (list of strings).'''
    words = []

    with open(infil, 'r', encoding="utf-8") as infil:
        #word = infil.readline().strip()
        word = [re.sub(r'[^a-zA-Z0-9\s]', '', line.strip()) for line in infil]
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

    with open(file_name, 'w', encoding="utf-8") as outfile:
            outfile.write(matrix)

#allword, textlist = get_word_lists()

''' 
allword = []    # listan med alla unika ord
textlist = []    # listan med texten i listform
'''
def create_matrix(allword, textlist):
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

    np.save('markov_matrix.npy1', Markov)
    np.save('lentot_value.npy1', lentot)

    return Markov, lentot

def write_to_excel(markov):
    df = pd.DataFrame(markov)

    excel_writer = pd.ExcelWriter('markov.xlsx', engine='xlsxwriter')

    df.to_excel(excel_writer, sheet_name='BarGraphData', index=False)

    excel_writer.close()

def user_word(Markov, lentot, allword):
    prevword = input('Write word ')
    if prevword in allword:     # Kollar efterföljande ord
        wordvector = np.zeros((lentot,1))
        wordvector[allword.index(prevword),0] = 1
        for n in range(3):
            wordvector = Markov.dot(wordvector)
            maxpos = next(i for i, x in enumerate(wordvector) if x == wordvector.max())
            nextword = allword[maxpos]
            print(nextword)

def main():
    textlist, allword= get_word_lists()
    
    try:
        Markov = np.load('markov_matrix1.npy')
        lentot = np.load('lentot_value1.npy')
    except FileNotFoundError:
        Markov, lentot = create_matrix(allword, textlist)

    user_word(Markov, lentot, allword)

if __name__ == '__main__':
    main()
