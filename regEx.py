import re

def textMatch1(text):
    pattern1 = 'ab+'
    if re.search(pattern1, text):
        return print(text, "is valid")
    else:
        return print(text, "is not valid")
def textMatch2(text):
    pattern2 = 'ab?'
    if re.search(pattern2, text):
        return print(text, "is valid")
    else:
        return print(text, "is not valid")
def textMatch3(text):
    pattern3 = 'abbb'
    if re.search(pattern3, text):
        return print(text, "is valid")
    else:
        return print(text, "is not valid")
def textMatch4(text):
    pattern4 = 'abbb?'
    if re.search(pattern4, text):
        return print(text, "is valid")
    else:
        return print(text, "is not valid")

print("expression ab+")
textMatch1("ab")
textMatch1("a")
textMatch1("abc")
print("expression ab?")
textMatch2("ab")
textMatch2("a")
textMatch2("abb")
print("expression abbb")
textMatch3("abbb")
textMatch3("abb")
textMatch3("abbbb")
print("expression abbb?")
textMatch4("abbb")
textMatch4("abb")
textMatch4("ab")
