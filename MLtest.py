import requests
import PyPDF2


def ge_unik_text_lista():
    '''
    Reads all pages of a pdf-file and prints a list with all words that occur, without repetition.
    
    Parameters: none.

    Return values: none.
    '''

    webpage = requests.get('https://www.gutenberg.org/cache/epub/72142/pg72142.txt')
    webpage_words = webpage.text.split()
    webpage_words.sort()
    #print(webpage_words)
    #print(len(webpage_words))
    amount_of_words_in_dok = len(webpage_words)
    unique_list = []

    test_list = ['a', 'a', 'a', 'a', '123453', 'g', 'g', 'asdfg', 'dfghjk', 't', 't', 't', 'o']
    test_list.sort()

    pdfFileObj = open('text_data.pdf', 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    pageObj = pdfReader.pages[34]
    print(pageObj.extract_text())
    pdfFileObj.close()

    test_list_words = len(test_list)

    actual_word = ''

    """for i in range(amount_of_words_in_dok):
        if webpage_words[i] != actual_word:
            unique_list.append(webpage_words[i])
            actual_word = webpage_words[i]"""

        
    print(unique_list)

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
    
    print(word_list)

    return word_list

def binsok(lista, element):
    '''Kollar om ett element finns i en lista mha binärsökning.

    Parametrar:
    lista (list): listan som undersöks
    elem (str): vi vill se om detta element finns i listan.

    Returvärden: ett booleskt värde beroende på om elementet finns i listan eller ej.'''
    lista.sort()
    
    lo = 0
    hi = len(lista)-1
    while lo <= hi:
        mid = (lo+hi)//2
        #print(f'\n{lista[mid]}\n')
        if element < lista[mid]:
            hi = mid - 1
        elif element > lista[mid]:
            lo = mid + 1
        else:
            return True
    return False

if __name__ == '__main__':
    #get_textlist()
    get_word_list('text_data.pdf')
