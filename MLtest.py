import PyPDF2

def get_unique_word_list(word_list):
    '''
    Given a list, this function creates a list with the same elements, but without repetition and writes it to a file. (That is, elements that occur multiple times in word_list will only
    occur one time in the unique_word_list that this function creates.)

    Parameters: word_list (list): list of words (strings) that may include repetitions.

    Return values: none.
    '''
    word_list.sort()

    unique_word_list = []

    actual_word = ''

    for i in range(len(word_list)): 

        word = word_list[i]

        word.strip('$%&+=0123456789*.?!-)(][_/|,"“”:}{;—<>@').strip("'").lower()

        #Create unique list
        if word != actual_word:
            unique_word_list.append(word)
            actual_word = word

    write2file(unique_word_list, 'unique_word_list.txt')

def get_word_list(pdf):
    '''Reads pdf-file and creates a list of all words that occure, that is then returned and printed to a file.
    
    Parameters: pdf (str): the name of the pdf-file.
    
    Return values: word_list (list): list of strings that contains all words in the infile.'''

    pdf_obj = open(pdf, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_obj)
    number_of_pages = len(pdf_reader.pages)
    
    word_matrix = []

    for i in range(number_of_pages):
        page_obj = pdf_reader.pages[i]
        text = page_obj.extract_text()
        word_matrix.append(text.split())
    
    word_list = []
    [word_list.extend(el) for el in word_matrix]

    word_list_edited = []

    for i in range(len(word_list)):
        if word_list[i].strip('$%&+=0123456789*.?!-)(][_/|,"“”:}{;—<>@').strip("'").lower() in ['', ' ', '\n']:
            continue

        word_list_edited.append(word_list[i].strip('$%&+=0123456789*.?!-)(][_/|,"“”:}{;—<>@').strip("'").lower())

    write2file(word_list_edited, 'word_list.txt')
    return word_list_edited

def write2file(word_list, file_name):
    ''''Writes all elements of a list to a file.
    
    Parameters: 
    word_list (list of strings)
    file_name (str): name of outfile.
    
    Return values: none.'''

    with open(file_name, 'w', encoding='utf-8') as outfile:
        for word in word_list:
            outfile.write(word + '\n')
        
if __name__ == '__main__':
    word_list = get_word_list('Andersen.pdf')
    get_unique_word_list(word_list)
