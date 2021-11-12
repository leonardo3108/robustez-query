"""
    Functions that add noise to text
    
    Original font (adapted): https://github.com/valentinmace/noisy-text

    The default parameters are to reproduce Edunov et al. (2018)* experiments but you can play with them and maybe find better values

    * Understanding Back-Translation at Scale. https://arxiv.org/abs/1808.09381

"""



import random


# Utility function 
def random_bool(probability=0.5):
    """Returns True with given probability

    Args:
        probability: probability to return True

    """
    assert (0 <= probability <= 1), "probability needs to be >= 0 and <= 1"
    return random.random() < probability

# Utility function 
def count_lines(filename):
    """Returns the number of sentences in the given file

    Args:
        filename: (string) path to the file

    """
    return sum(1 for sentence in open(filename))


def delete_random_token(sentence, probability):
    """Delete random tokens in a given String with given probability

    Args:
        sentence: a String
        probability: probability to delete each token

    """
    sentence_split = sentence.split()
    ret = [token for token in sentence_split if not random_bool(probability)]
    return " ".join(ret)


def random_token_permutation(sentence, _range:int = 3):
    """Random permutation over the tokens of a String, restricted to a range, drawn from the uniform distribution

    Args:
        sentence: a String
        _range: Max range for token permutation

    """
    sentence_split = sentence.split()
    new_indices = [i+random.uniform(0, _range+1) for i in range(len(sentence_split))]
    res = [x for _, x in sorted(zip(new_indices, sentence_split), key=lambda pair: pair[0])]
    return " ".join(res)

