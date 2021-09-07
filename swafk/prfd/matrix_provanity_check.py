from .checker import *
from .text_utils import *


def matrix_profanity_check_rating(raw_rating):
    rating_ = raw_rating.lower()
    forbidden_rating = ["mature", "adult", "restricted", "RTA-5042-1996-1400-1577-RTA"]
    forbidden_rating = [fr.lower() for fr in forbidden_rating]
    for fr in forbidden_rating:
        if fr in rating_:
            return {"rating": 1}

    return {"rating": 0}


def matrix_profanity_check_url(raw_url):
    url_clean = cleaning_url(raw_url)
    text_ = cleaning_text(url_clean)

    v_check_forbidden_word = check_forbidden_word(url_clean)
    v_check_profanity_check_lib = check_profanity_check_lib(text_)
    v_check_ip_domain = check_ip_domain(raw_url)

    return {"fword": v_check_forbidden_word, "proflib": v_check_profanity_check_lib, "ipdomain": v_check_ip_domain}


def matrix_profanity_check_text(raw_text):
    text_ = cleaning_text(raw_text)

    v_check_forbidden_word = check_forbidden_word(raw_text)
    v_check_profanity_check_lib = check_profanity_check_lib(text_)

    return {"fword": v_check_forbidden_word, "proflib": v_check_profanity_check_lib}
