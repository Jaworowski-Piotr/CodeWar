# The goal of this exercise is to convert a string to a new string where
# each character in the new string is "(" if that character appears only
# once in the original string, or ")" if that character appears more than
# once in the original string. Ignore capitalization when determining if
# a character is a duplicate.

def duplicate_encode(word):
    lower_case_string = word.lower()
    print(lower_case_string)
    temp = []
    next_word = ""
    for letters in lower_case_string:
        if(lower_case_string.count(letters)>1):
            temp.append(")")
        else:
            temp.append("(")
    return next_word.join(temp)

print(duplicate_encode(word="recede"))

####Najciekawsze rozwiązanie####
# from collections import Counter
#
# def duplicate_encode(word):
#     word = word.lower()
#     counter = Counter(word)
#     return ''.join(('(' if counter[c] == 1 else ')') for c in word)