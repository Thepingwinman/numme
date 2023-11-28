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

    print(word_list, unique_word_list)

    print(f'längd word_list: {len(word_list)}; längd unique_word_list: {len(unique_word_list)}')

    return word_list, unique_word_list

get_word_lists()
