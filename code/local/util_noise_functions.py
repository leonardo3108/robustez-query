"""
    Utility functions that add noise to text
    
    Original font (adapted): https://github.com/valentinmace/noisy-text
    * Understanding Back-Translation at Scale. https://arxiv.org/abs/1808.09381

"""

import random
import re
import pandas as pd

# Utility function 
def random_bool(probability=0.5):
    """Returns True with given probability

    Args:
        probability: probability to return True

    """
    assert (0 <= probability <= 1), "probability needs to be >= 0 and <= 1"
    return random.random() < probability

def delete_random_token(sentence, probability):
    """Delete random tokens in a given String with given probability
        If no word is deleted, the central one is deleted
    Args:
        sentence: a String
        probability: probability to delete each token

    """
    sentence_split = return_tokens(sentence)
    res = [token for token in sentence_split if not random_bool(probability)]

    if len(sentence_split) == len(res): # If no word is deleted, the central one is deleted
        # print(f"Excluindo palavra na posição {len(res)//2} de lista com {len(res)} elementos")
        del res[len(res)//2]
    
    new_sentence = " ".join(res)
    # print(f"Sentença antes: {sentence}; após ruído: {new_sentence}")
    if new_sentence == sentence:
        print(f"Não houve mudança em sentença antes: {sentence}; após ruído: {new_sentence}")   
    return new_sentence


def random_token_permutation(sentence, _range:int = 3):
    """Random permutation over the tokens of a String, restricted to a range, drawn from the uniform distribution

    Args:
        sentence: a String
        _range: Max range for token permutation
    """
    sentence_split = return_tokens(sentence)
    new_indices = [i+random.uniform(0, _range+1) for i in range(len(sentence_split))]
    res = [x for _, x in sorted(zip(new_indices, sentence_split), key=lambda pair: pair[0])]
    return " ".join(res)

def delete_token_set_index(sentence,  set_index_deletion:set):
    """Delete tokens in a given String by position informed in set_index_deletion

    Args:
        sentence (str): sentence to be changed
        set_index_deletion (set): list of unique indices (set) to be deleted
    """
    sentence_split = return_tokens(sentence)
    res = [x for num, x in enumerate(sentence_split) if num not in set_index_deletion]
    new_sentence = " ".join(res)
    # print(f"Sentença antes: {sentence}; após ruído: {new_sentence}")
    if new_sentence == sentence:
        print(f"Não houve mudança em sentença antes: {sentence}; após ruído: {new_sentence}")   
    return new_sentence

def token_permutation_list_index_pair(sentence, list_change_index_pair:list):
    """Random permutation over the tokens of a String, restricted to a range, drawn from the uniform distribution

    Args:
        sentence (str): sentence to be changed
        list_change_index_pair (list): list of index pairs to be permutated
    """
    sentence_split = return_tokens(sentence)
    new_indices = [i for i in range(len(sentence_split))]
    for change_pair in list_change_index_pair:
        assert change_pair[1] != change_pair[0], "Passados índices iguais"
        if change_pair[1] < len(sentence_split):
            new_indices[change_pair[0]] = change_pair[1]
            new_indices[change_pair[1]] = change_pair[0]
    res = [x for _, x in sorted(zip(new_indices, sentence_split), key=lambda pair: pair[0])]
    new_sentence = " ".join(res)
    # print(f"Sentença antes: {sentence}; após ruído: {new_sentence}")
    if new_sentence == sentence:
        print(f"Não houve mudança em sentença antes: {sentence}; após ruído: {new_sentence}")
        
    return new_sentence

def return_tokens(sentence:str)->list:
    """
    Given a sentence
    Return a list of tokens 
    Are considered words: ",?;.!" and numbers
    
    Args:
    sentence (str): sentence to be changed

    """
    # sentence_split = sentence.split()
    return re.findall(r"\w+\_\w+|\w+\'\w+|\w+\-\w+|\w+|^[0-9]$|[,?;.!]",sentence, re.IGNORECASE)