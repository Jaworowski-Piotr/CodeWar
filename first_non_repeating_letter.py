def first_non_repeating_letter(string):
    temp = string.lower()
    all_repeat = False
    if len(string) == 0:
        return ""
    for i, char in enumerate(temp):
        if temp.count(char) <= 1:
            return string[i]
        elif temp.count(char) > 1:
            all_repeat = True
        else:
            all_repeat = False
    if all_repeat:
        return None


print(first_non_repeating_letter('sttreess'))