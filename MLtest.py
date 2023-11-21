import requests
import PyPDF2


def get_textlist():
    webpage = requests.get('https://www.gutenberg.org/cache/epub/72142/pg72142.txt')
    webpage_words = webpage.text.split()
    webpage_words.sort()
    #print(webpage_words)
    #print(len(webpage_words))
    amount_of_words_in_dok = len(webpage_words)
    definitiv_list = []

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
            definitiv_list.append(webpage_words[i])
            actual_word = webpage_words[i]"""

        
    print(definitiv_list)

def read_pdf_list(pdf):
    pdfFileObj = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    ant_sidor = len(pdfReader.pages)
    pg_lista = []
    for i in range(ant_sidor):
        page_obj = pdfReader.pages[i]
        text = page_obj.extract_text()
        pg_lista.append(text.split())
    text_lista = []
    [text_lista.extend(el) for el in pg_lista]
    print(text_lista)

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

if __name__ == "__main__":
    #get_textlist()
    read_pdf_list("text_data.pdf")