import requests

def Get_textlist():
    webpage = requests.get('https://www.gutenberg.org/cache/epub/72142/pg72142.txt')
    webpage_words = webpage.text.split()
    #print(webpage_words)
    #print(len(webpage_words))
    amount_of_words_in_dok = len(webpage_words)
    definitiv_list = []
    test_list = ["hello", "yeti", "hello", "pablo", "escobar", "is", "my", "name"]
    test_list_words = len(test_list)
    for i in range(test_list_words):
        if test_list[i] not in definitiv_list:
            definitiv_list.append(test_list[i])
        """value = binsok(definitiv_list, test_list[i])
        if value == False:
            definitiv_list.append(test_list[i])"""
    print(definitiv_list)

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
    Get_textlist()