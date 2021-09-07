from profanity_check import predict
import csv
from .text_utils import *



forbidden_word = []
with open('swafk/data/bad-bad-word-cleaned.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
for i in data:
    forbidden_word.append(i[0])


def check_forbidden_word(raw_text)->int:
    '''
    :rtype: integer
    :type text : string
    :param text: type string, text 
    :return: integer, 1 jika menemukan forbidden word, 0 jika tidak ditemukan forbidden word
    '''    
    text_ = raw_text.lower()
    for fword in forbidden_word:
        if fword in text_:
            return 1
    return 0

def check_ip_domain(raw_url)->int:
    url_ = re.sub(r'https|http|/|:', ' ', raw_url)
    url_ = re.sub(' +', ' ', url_)
    url_ = url_.strip(" ")
    url_ = url_.split(" ")
    if not url_[0].split('.')[-1].isalpha() :
        return 1
    else :
        return 0

def check_profanity_check_lib(text)->int:
    return predict([text])[0]