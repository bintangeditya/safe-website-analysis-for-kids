from .provanity_check import *
from .matrix_provanity_check import *


def profanity_check_overall(url, title, description, keyword, rating):
    v_profanity_check_url = profanity_check_url(url)
    if v_profanity_check_url == 1: return 1

    v_profanity_check_title = profanity_check_text(title)
    if v_profanity_check_title == 1: return 1

    v_profanity_check_description = profanity_check_text(description)
    if v_profanity_check_description == 1: return 1

    v_profanity_check_keyword = profanity_check_text(keyword)
    if v_profanity_check_keyword == 1: return 1

    v_profanity_check_rating = profanity_check_rating(rating)
    if v_profanity_check_rating == 1: return 1

    return 0


def matrix_profanity_check_overall(url, title, description, keyword, rating):
    v_profanity_check_url = matrix_profanity_check_url(url)
    v_profanity_check_title = matrix_profanity_check_text(title)
    v_profanity_check_description = matrix_profanity_check_text(description)
    v_profanity_check_keyword = matrix_profanity_check_text(keyword)
    v_profanity_check_rating = matrix_profanity_check_rating(rating)

    return {"url": v_profanity_check_url, "title": v_profanity_check_title,
            "description": v_profanity_check_description, "keyword": v_profanity_check_keyword,
            "rating": v_profanity_check_rating}
