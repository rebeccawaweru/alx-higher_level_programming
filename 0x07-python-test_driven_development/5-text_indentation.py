#!/usr/bin/python3

def text_indentation(text):
    """ print text with 2 new lines after : . ,? :
    Args:
    text - must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    punctuation_marks = [".", "?", ":"]
    line = ""
    j = 0
    length = len(text)
    while j < length:
        line += text[j]
        if text[j] in punctuation_marks:
            line = line.strip()
            print(line + '\n')
            try:
                if text[j + 1] == ' ':
                    j += 1
            except IndexError:
                pass
            line = ''
        j += 1
    if length > 0:
        print(line, end="")
