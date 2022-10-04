def alphanumeric(password):
    return password.isalnum()

some_string = input("Prosze wprowadzić ciąg znaków: ")

print(alphanumeric(some_string))

#Wykonanie zawierające regular expression
# import re
#
# pattern = re.compile('^[0-9a-zA-Z]+$')
#
# def alphanumeric(string):
#   return pattern.match(string) is not None