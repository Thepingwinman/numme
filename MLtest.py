import PyPDF2

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

    for i in range(len(word_list)): 

        word = word_list[i]

        word.strip('.?!-)(][_/|,"“”:}{;—<>@').strip("'").lower()

        #Create unique list
        if word != actual_word:
            unique_word_list.append(word)
            actual_word = word

    write2file(unique_word_list, 'unique_word_list.txt')
    #return unique_word_list

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

    word_list_edited = []

    for i in range(len(word_list)):
        if i in list(range(15)):
            print(f'\nordet: {word_list[i]}\n')
            
            print(f'\nangtal karaktärer i ordet: {len(word_list[i])}\n\n')

        if word_list[i].strip('.?!-)(][_/|,"“”:}{;—<>@').strip("'").lower() in ['', ' ', '\n']:
            continue
        
        word_list_edited.append(word_list[i].strip('.?!-)(][_/|,"“”:}{;—<>@').strip("'").lower())

    write2file(word_list_edited, 'word_list.txt')
    return word_list_edited

def write2file(word_list, file_name):
    ''''Writes all elements of a list to a file.
    
    Parameters: 
    word_list (list of strings)
    file_name (str): name of outfile.
    
    Return values: none.'''

    with open(file_name, 'w') as outfile:
        for word in word_list:
            outfile.write(word + '\n')
        
if __name__ == '__main__':
    word_list = get_word_list('text_data.pdf')
    unique_word_list = get_unique_word_list(word_list)

