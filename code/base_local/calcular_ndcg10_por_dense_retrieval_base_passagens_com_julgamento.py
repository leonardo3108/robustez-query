import requests
import math


queries = []
for query in open('data/queries-originals.txt'):
    fields = query.strip().split()
    queries.append((fields[0], ' '.join(fields[1:])))
print(f"\nquery[0] {queries[0]}")

scale = {3:'perfectly relevant', 2:'highly relevant', 1:'related', 0:'Irrelevant'}
judment = {}
for i, line in enumerate(open('data/originals/2020qrels-pass.txt')):
    query_nr, _, pid, eval = line.rstrip().split()
    judment[(query_nr, pid)] = int(eval)

print(f"\njudment[0] {list(judment)[0], judment[list(judment)[0]], scale[judment[list(judment)[0]]]}")


for query_number, query_text in queries:
    print(query_number, query_text + ':')
    for i, result_busca in enumerate(retriever.retrieve(query_text, top_k=10)):
      if i >= 10:
        raise Exception('Mudar códido se trouxer mais do que 10')
      docid = result_busca.meta['docid']
      if (query_number, docid) not in judment:
        print(f'{(query_number, docid)} not in judment')
      eval = judment.get((query_number, docid), 0)
      content = result_busca.text
      print(f'\t{i+1:2} {docid:15} {result_busca.score:.5f}\t{eval} ({scale[eval]:18})    {content}')


dcg10 = {}

for query_number, query_text in queries:
    dcg = 0
    for i, result_busca in enumerate(retriever.retrieve(query_text, top_k=10)):
      if i >= 10:
        raise 'Mudar códido se trouxer mais do que 10'
      docid = result_busca.meta['docid']
      if (query_number, docid) not in judment:
        print(f'{(query_number, docid)} not in judment')
      eval = judment.get((query_number, docid), 0)
      dcg += (2**int(eval)-1) / math.log2(i+2)
    dcg10[query_number] = dcg
    print(f'{query_number}: {dcg}')


w = open('data/dcg10_dense_dpr_mmpr_com_julgamento.csv', 'w')
w.write('query, dcg@10\n')
for query in dcg10.keys():
    w.write('{}, {}\n'.format(query, dcg10[query]))
w.close()