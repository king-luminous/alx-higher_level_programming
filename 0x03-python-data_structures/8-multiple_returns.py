#!/usr/bin/python3
def multiple_returns(sentence):
    my_sentence = ()
    if len(sentence) == 0:
        my_sentence = 0, "none"
    else:
        my_sentence = len(sentence), sentence[0]
    return my_sentence

