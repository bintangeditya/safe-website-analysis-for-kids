import re
import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.tokenize.toktok import ToktokTokenizer



def cleaning_url(raw_url)->str:
    url_ = re.sub(';|,| |-|/|:|\.',' ',raw_url)
    url_ = url_.lower()
    url_ = re.sub(r'https|com|net|co|us|fr|uk|id|care|http|www', ' ', url_)
    return url_


stopwords_english = stopwords.words('english')
stemmer = PorterStemmer()

mtokenize = ToktokTokenizer()

# stopword tambahan
more_stopword = set([])

# Happy Emoticons
emoticons_happy = set([
    ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3'
])

# Sad Emoticons
emoticons_sad = set([
    ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';('
])

# all emoticons (happy + sad)
emoticons = emoticons_happy.union(emoticons_sad)

def cleaning_text(raw_text)->str:
    '''
    :rtype: string
    :type text : string
    :param text: type string, text mentah
    :return: type string, text yang sudah dibersihkan
    '''
    text_ = re.sub(r'\n', ' ', raw_text)  # menghapus baris baru
    text_ = text_.strip(" ")  # menghapus karakter spasi pada awal dan akhir kalimat
    symbols_regrex_pattern = re.compile(pattern="["
                                                u"\U0001F600-\U0001F64F"  # emoticons
                                                u"\U0001F300-\U0001F5FF"  # simbol & piktograf
                                                u"\U0001F680-\U0001F6FF"  # simbol transport & map
                                                "]+", flags=re.UNICODE)    
    text_ = symbols_regrex_pattern.sub(r' ', text_)  
    text_ = text_.lower() 
    text_ = re.sub(r'^https?:\/\/.*[\r\n]*', ' ', text_, flags=re.MULTILINE)  # menghapus hyperlink
    text_ = re.sub('[0-9]+', ' ', text_)  # menghapus angka
    tokens = word_tokenize(text_)  # tokenize kata-kata
    tokens = mtokenize.tokenize(text_)  # tokenize kata-kata
    text_clean = []

    for word in tokens:
        if (word not in stopwords_english and  # menghilangkan stopwords. proses filtering
                word not in emoticons and  # menghilangkan emoticons. proses filtering
                word not in more_stopword and
                word not in string.punctuation):  # menghilangkan tanda baca. proses filtering
            stem_word = stemmer.stem(word)  # mengubah ke kata dasar. proses stemming
            text_clean.append(stem_word)

    text_clean = " ".join(text_clean)
    text_clean = re.sub(r'[?\|$\.!_:")(\+,\*&%#@`\'\"=\\/]', ' ', text_clean)  # menghapus beberapa karakter khusus
    text_clean = re.sub(' +', ' ', text_clean)  # lebih dari satu spasi yang berdekatan, menjadi satu spasi
    text_ = text_.strip(" ")  # menghapus karakter spasi pada awal dan akhir kalimat
    return text_clean
