import re

def textMatch(text, pattern):
    if re.search(pattern, text):
        return print(text, "Found a match")
    else:
        return print(text, "No match")

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
#-----EXTENSION CHALLENGES-----
def textMatch2(text, pattern, rejectPattern):
    if re.search(pattern, text):
        if re.search(rejectPattern, text):
            return print(text, "No match")
        else:
            return print(text, "Found a match")
    else:
        return print(text, "No match")
print("Check string only contains a certain set of characters")
pattern = "\w+"
rejectPattern = "\W+"
textMatch2("hello", pattern, rejectPattern)
textMatch2("Hello", pattern, rejectPattern)
textMatch2("Hello1", pattern, rejectPattern)
textMatch2("Hello!", pattern, rejectPattern)
print("One upper case letter followed by lower case letters")
pattern = "[A-Z][a-z]+"
rejectPattern = "[A-Z][a-z]*([A-Z]+|[0-9]+|\W+)+"
textMatch2("Hello", pattern, rejectPattern)
textMatch2("Hello!", pattern, rejectPattern)
textMatch2("HellO", pattern, rejectPattern)
print("Anything between a and b")
pattern = "^a\w+b$"
textMatch("abcdcb", pattern)
textMatch("bcdcb", pattern)
textMatch("abcdcba", pattern)
print("Match a word at the beginning of a string")
textMatch("Hello world", "Hello")
textMatch("Hello world", "hello")
textMatch("hello world", "Hello")
