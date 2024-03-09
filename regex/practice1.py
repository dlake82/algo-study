import re


def practice1():
    p = re.compile("[a-z]+")

    # match() returns a match object if the string starts with the pattern
    m = p.match("python")
    if m:
        print("Match found:", m.group())
    else:
        print("No match")

    # search() returns a match object if there is a match anywhere in the string
    m = p.search("python")
    print(m)  # <re.Match object; span=(0, 6), match='python'>
    m = p.search("3 python")
    print(m)  # <re.Match object; span=(2, 8), match='python'>

    # findall() returns a list of all matches
    m = p.findall("life is too short")
    print(m)  # ['life', 'is', 'too', 'short']

    # finditer() returns an iterator of all matches
    m = p.finditer("life is too short")
    for r in m:
        print(r)  # <re.Match object; span=(0, 4), match='life'>

    # m.group() returns the matched string
    m.group()  # 'python'
    # m.start() returns the starting position of the match
    m.start()  # 0
    # m.end() returns the ending position of the match
    m.end()  # 6
    # m.span() returns a tuple containing the (start, end) positions of the match
    m.span()  # (0, 6)

    m = re.match("[a-z]+", "python")

    # DOTALL matches any character including new line
    p = re.compile("a.b", re.DOTALL or re.S)
    m = p.match("a\nb")
    print(m)  # <re.Match object; span=(0, 3), match='a\nb'>

    p = re.compile("[a-z]", re.IGNORECASE or re.I)
    m = p.match("Python")
    print(m)  # <re.Match object; span=(0, 1), match='P'>
    m = p.match("PYTHON")
    print(m)  # None

    p = re.compile("^python\s\w+", re.MULTILINE or re.M)
    data = """python one
    life is too short
    python two
    you need python
    python three"""

    m = p.findall(data)
    print(m)  # ['python one', 'python two', 'python three']

    # VERBOSE allows you to write multi-line regular expressions
    charref = re.compile(r"&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);")
    charref = re.compile(
        r"""
    &[#]                # Start of a numeric entity reference
    (
        0[0-7]+         # Octal form
    | [0-9]+          # Decimal form
    | x[0-9a-fA-F]+   # Hexadecimal form
    )
    ;                   # Trailing semicolon
    """,
        re.VERBOSE,
    )

    # r"" is used to create a raw string
    p = re.compile(r"\\secsion")
