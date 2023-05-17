#!/usr/bin/python3
def best_score(a_dictionary):
    top_score = 0
    for key, score in a_dictionary:
        if score > top_score:
            top_score = score
            alias = key
    if top_score == 0:
        return None
    return alias
