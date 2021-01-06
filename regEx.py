import re

def textMatch(text, pattern):
    if re.search(pattern, text):
        return print(text, "is valid")
    else:
        return print(text, "is not valid")

print("expression ab+")
pattern = "ab*"
textMatch("ab", pattern)
textMatch("a", pattern)
textMatch("abc", pattern)
print("expression ab?")
pattern = "ab?"
textMatch("ab", pattern)
textMatch("a", pattern)
textMatch("abb", pattern)
print("expression abbb")
pattern = "abbb"
textMatch("abbb", pattern)
textMatch("abb", pattern)
textMatch("abbbb", pattern)
print("expression abbb?")
pattern = "abbb?"
textMatch("abbb", pattern)
textMatch("abb", pattern)
textMatch("ab", pattern)
