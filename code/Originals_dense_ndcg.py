"""
    Em construção
"""

from pyserini.dsearch import SimpleDenseSearcher,  DprQueryEncoder

encoder =  DprQueryEncoder('facebook/dpr-question_encoder-multiset-base', device='cpu')
dsearcher = SimpleDenseSearcher.from_prebuilt_index('msmarco-passage', encoder)

queries = []
for query in open('data/queries-originals.txt'):
    fields = query.strip().split()
    queries.append((fields[0], ' '.join(fields[1:])))

print(f"query[0] {queries[0]}")

scale = {3:'perfectly relevant', 2:'highly relevant', 1:'related', 0:'Irrelevant'}
judment = {}
for i, line in enumerate(open('data/originals/2020qrels-pass.txt')):
    query_nr, _, pid, eval = line.rstrip().split()
    judment[(query_nr, pid)] = int(eval)

print(f"judment[0] {list(judment)[0], judment[list(judment)[0]], scale[judment[list(judment)[0]]]}")