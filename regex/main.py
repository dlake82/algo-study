import practice1
import practice2

# .^$*+?{}[]\|()
# . - Any character except new line
# ^ - Start of a string
# $ - End of a string
# * - 0 or more occurrences
# + - 1 or more occurrences
# ? - 0 or 1 occurrences
# {} - Exactly the specified number of occurrences
# [] - A set of characters
# \ - Special sequence
# | - Either or
# () - Capture and group
# \A - Beginning of a string
# \b - Beginning of a word
# \B - Not at the beginning of a word
# \d - Any digit
# \D - Any non-digit
# \s - Any whitespace
# \S - Any non-whitespace
# \w - Any word character
# \W - Any non-word character
# \Z - End of a string

if __name__ == "__main__":
    practice1()
    practice2()
