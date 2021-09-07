from .prfd.profanity_detection import profanity_check_overall, matrix_profanity_check_overall


def check(url, title, description, keyword, rating):
    if profanity_check_overall(url, title, description, keyword, rating) == 1:
        return "bad"
    else:
        return "good"


def matrix(url, title, description, keyword, rating):
    for key, dict2 in matrix_profanity_check_overall(url, title, description, keyword, rating).items():
        print("["+key + "]")
        for key2, value in dict2.items():
            rate = "bad"
            if value == 0 : rate = "good"
            print(key2 + "\t : " + rate)
        print("")
