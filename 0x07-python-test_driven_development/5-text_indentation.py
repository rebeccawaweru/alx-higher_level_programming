#!/usr/bin/python3

""" text_indentation
Print text with two lines after punctuations
"""


def text_indentation(text):
    """ print text with 2 new lines after : . ,? :
    Args:
    text - must be a string
    """
    if text is None:
        raise TypeError("missing argument")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    j = 0
    while j < len(text) and text[j] == ' ':
        j += 1
    while j < len(text):
        print(text[j], end="")
        if text[j] == "\n" or text[j] in ".?:":
            if text[j] in ".?:":
                print("\n")
            j += 1
            while j < len(text) and text[j] == ' ':
                j += 1
            continue
        j += 1
