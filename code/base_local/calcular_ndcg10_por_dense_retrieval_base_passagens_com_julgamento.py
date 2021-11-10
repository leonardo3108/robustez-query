import math
import csv

idcg = {}
with open('data/idcg.csv', newline='\n') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
    for query, value in csvreader:
        if query == 'query': continue
        idcg[query] = float(value)
print(f"\nidcg {idcg}")

dcg10 = {}
with open('data/dcg10_dense_dpr_mmpr_com_julgamento.csv', newline='\n') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
    for query, value in csvreader:
        if query == 'query': continue
        dcg10[query] = float(value)
print(f"\ndcg10 {dcg10}")


ndcg10 = {}
for query in dcg10.keys():
    ndcg10[query] = dcg10[query] / idcg[query]
print(f"\nndcg10 {ndcg10}")

w = open('data/ndcg10_dense_dpr_mmpr_com_julgamento.csv', 'w')
w.write('query, ndcg@10\n')
for query in dcg10.keys():
    w.write('{}, {}\n'.format(query, ndcg10[query]))
w.close()

print('Fim!')