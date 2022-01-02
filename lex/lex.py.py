import re

# f = open("input.txt", "x")
word_input = ""


def getchar():
    # gets a character from a file named input.txt - done
    # and classifies it as LETTER, DIGIT, or UNKNOWN.
    # and classifies it as LETTER, DIGIT, or UNKNOWN.
    # Implement a way for it to ignore white spaces.
    classifier = []
    f = open("input.txt", "r")
    word = f.read()
    f.close()

    global word_input
    word_input = word
    for x in word:
        if bool(x.isalpha()) == bool(True):
            classifier.append(0)

        elif bool(x.isnumeric()) == bool(True):
            classifier.append(1)
        else:
            if x == " " or x == "\n":
                classifier.append(x)
                # continue
            else:
                classifier.append(2)
    return classifier


def add_char(word):
    # adds the character to a lexeme array of size 10 (therefore, maximum lexeme length is 9 to accommodate for
    # string terminator '\0'). If longer than max length, simply disregard the extra characters (do not insert in
    # array)
    temp_next = ""
    temp_lexeme = ""
    numeric = 0

    lexeme = []
    max_iter = len(word)

    for x in range(0, len(word)):

        if len(lexeme) > 8:
            break

        temp = word[x]
        if x < max_iter - 1:
            temp_next = word[x + 1]

        # if space or newline ang first
        if temp == " " or temp == "\n":
            continue

        elif bool(temp.isalpha()) == bool(True) or numeric == 1:
            if bool(temp_next.isalpha()) == bool(True) or bool(temp_next.isnumeric()) == bool(True):
                temp_lexeme = temp_lexeme + temp
                numeric = 1

            else:
                temp_lexeme = temp_lexeme + temp
                lexeme.append(temp_lexeme)
                numeric = 0
                temp_lexeme = ""

        elif bool(temp.isnumeric()) == bool(True):
            if bool(temp_next.isnumeric()) == bool(True):
                temp_lexeme = temp_lexeme + temp

            else:
                temp_lexeme = temp_lexeme + temp
                lexeme.append(temp_lexeme)
                temp_lexeme = ""

        else:
            lexeme.append(temp)

    return lexeme


def word_lookup(lexemes):
    # returns a token for unknown symbols;
    # the valid unknown symbols are +, –, *, /, (, ), and =.
    # Give them unique tokens each.
    # Invalid symbols all have the EOF token.
    # As for the token lookup for strings, you may implement it on a separate function (e.g. lookup2) or
    # within the lex function
    special_char = {
        "+": "PLUS_OP",
        "-": "MINUS_OP",
        "*": "DIVISION_OP",
        ",": "COMMA",
        "!": "LOGICAL_NOT"
    }
    max_iter = len(lexemes)
    token = []
    for x in range(0, max_iter):

        temp_lexemes = lexemes[x]
        if re.findall("^[a-zA-Z]", temp_lexemes):
            token.append("IDENTIFIER")

        elif re.findall("^[0-9]", temp_lexemes):
            token.append("INT_LITERAL")

        elif re.findall("^[+*,!]", temp_lexemes):
            for y in special_char:
                if temp_lexemes == y:
                    token.append(special_char[temp_lexemes])

        else:
            token.append("INVALID")
    return token


word_classifier = getchar()
word_lexeme = add_char(word_input)
word_token = word_lookup(word_lexeme)

res_lexemeAndToken = dict(zip(word_lexeme, word_token))

print(f"{'Lexeme':<8}  {'Token':<10}")
for k, v in res_lexemeAndToken.items():
    print("{:<8}  {:<10}".format(k, v))
