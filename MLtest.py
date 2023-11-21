import requests
import json

def Get_textlist():
    webpage = requests.get('https://www.gutenberg.org/cache/epub/72142/pg72142.txt')
    webpage_words = webpage.text.split()
    #print(webpage_words)
    #print(len(webpage_words))
    amount_of_words_in_dok = len(webpage_words)
    definitiv_list = []
    for i in range(amount_of_words_in_dok):
        if webpage_words[i] not in definitiv_list:
            definitiv_list.append(webpage_words)
    print(len(definitiv_list))

if __name__ == "__main__":
    Get_textlist()