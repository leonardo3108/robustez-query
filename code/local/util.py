""" 
Utility functions for calculatint Informational Retrieval Metrics
"""


def load_judment()->dict:
    """
        Gets data from data/originals/2020qrels-pass.txt 
            (got from https://trec.nist.gov/data/deep/2020qrels-pass.txt)

        Returns 2 dicts:
            dict_judment:
                key: tuple formed by (query_nr, passage_id)
                value: relevance registered for the tuple
            dict_scale_relevance:
                key: relevance (number between 0 and 3)
                value: label associated
    Obs.:
        **Passages** were judged on a four-point scale of:
        * Not Relevant (0), 
        * Related (1), 
        * Highly Relevant (2), and 
        * Perfect (3), 

        where 'Related' is actually NOT Relevant---it means that the passage was on the same general topic, but did not answer the question. 

        Thus, for Passage Ranking task runs (only), to compute evaluation measures that use binary relevance judgments using 
        trec_eval, you either need to use 
        trec_eval's -l option [trec_eval -l 2 qrelsfile runfile]
        or modify the qrels file to change all 1 judgments to 0.
        

    """
    scale = {3:'perfectly relevant', 2:'highly relevant', 1:'related', 0:'Irrelevant'}
    judment = {}
    for i, line in enumerate(open('data/originals/2020qrels-pass.txt')):
        query_nr, _, pid, eval = line.rstrip().split()
        query_nr = int(query_nr)
        judment[(query_nr, pid)] = int(eval)

    print(f"\nLoaded len: {len(judment)} judments; judment[0] {list(judment)[0], judment[list(judment)[0]], scale[judment[list(judment)[0]]]}")
    assert len(judment)==11386, f" len(judment) {len(judment)} was expected to be 11386 as it is in https://trec.nist.gov/data/deep/2020qrels-pass.txt"
    return judment, scale