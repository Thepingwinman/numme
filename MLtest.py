import PyPDF2

TEST = True

def get_unique_word_list(word_list):
    '''
    Given a list, this function returns a list with the same elements, but without repetition. (That is, elements that occur multiple times in word_list will only
    occur one time in the unique_word_list that this function returns.)

    Parameters: word_list (list): list of words (strings) that may include repetitions.

    Return values: unique_word_list (list): list of words (strings) that does not include repetitions.
    '''
    word_list.sort()

    unique_word_list = []

    actual_word = ''

    special_chars = ['.', '?', '!', '-', ')', '(', '[', ']', '_', '\\', '/', '|', ',', '"', "'", '“', '”', ':', '{', '}', '—', ';']

    for i in range(len(word_list)): 

        word = word_list[i]

        word = word_list[i]

        #Create unique list
        if word != actual_word:
            unique_word_list.append(word)
            actual_word = word

    if TEST:
        print(f'\n{unique_word_list}\n')
        print(f'\nLength of unique_word_list: {len(unique_word_list)}\n')

    return unique_word_list

def get_word_list(pdf):
    '''Reads pdf-file and returns list of all words that occure.
    
    Parameters: pdf (str): the name of the pdf-file.
    
    Return values: word_list (list): list of all words that occur in the pdf-file.'''

    pdf_obj = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfReader(pdf_obj)
    number_of_pages = len(pdfReader.pages)
    
    word_matrix = []

    for i in range(number_of_pages):
        page_obj = pdfReader.pages[i]
        text = page_obj.extract_text()
        word_matrix.append(text.split())
    
    word_list = []
    [word_list.extend(el) for el in word_matrix]

    for i in range(len(word_list)):
        word_list[i] = word_list[i].strip('.?!-)(][_/|,"“”:}{;—<>@').strip("'")
     
    if TEST:
        print(f'\n{word_list}\n')
        print(f'\nLength of word_list: {len(word_list)}\n')

    return word_list

if __name__ == '__main__':
    word_list = get_word_list('text_data.pdf')
    unique_word_list = get_unique_word_list(word_list)
