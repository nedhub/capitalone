import re
def reverseInParentheses(s):
    while "(" in s:
        match = re.search("\([^()]*\)", s)
        match_string = match.group(0)[1: len(match.group(0)) - 1]
        reversed_match_string = match_string[::-1]
        s = s[:match.start()] + reversed_match_string + s[match.end():]
    return s



# Write a function that reverses characters in (possibly nested) parentheses in the input string.

# Input strings will always be well-formed with matching ()s.