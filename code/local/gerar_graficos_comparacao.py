
# import matplotlib.pyplot as plt
# import pandas as pd
import util_bd_dataframe  as util_bd_pandas
import time
import matplotlib.pyplot as plt
import seaborn as sns

print("oi")
df_calculated_metric = util_bd_pandas.read_df_calculated_metric_with_label()[['search_context','cod_metric','noise_kind', 'value','qtd_judment_assumed', 'base_record_count','cod_original_query']]

#date_time_execution,cod_metric,cod_original_query,cod_noise_kind,cod_search_context,value,qtd_judment_assumed_zero_relevance
# util_bd_pandas.imprime_resumo_df(df_calculated_metric)
# grouped.boxplot(subplots=False, rot=45, fontsize=12, figsize=(8,10))
# df_calculated_metric.boxplot(rot=45, fontsize=12, figsize=(8,10), column=['value','qtd_judment_assumed_zero_relevance'], by=['cod_search_context','cod_metric', 'cod_noise_kind'])

fig_dims = (20, 80)
fig, ax = plt.subplots(figsize=fig_dims)
ax = sns.boxplot(x="search_context", hue="noise_kind", y="value", ax=ax, data=df_calculated_metric[df_calculated_metric['cod_metric']=='nDCG@10'])
#plt.xticks(rotation=0)
ax.set(ylabel = 'nDCG@10', xlabel = 'context')
plt.legend(loc='upper right', fontsize=6)
ax.set_title('Comparative of nDCG@10: search context and noise kind [boxplot]', y=1.0, pad=-14)
# fig.savefig('graphics\comparative_search_context_noise_kind_boxplot', transparent=False, dpi=80, bbox_inches='tight')
# Put the legend out of the figure
#plt.tight_layout()
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=3,  borderaxespad=0., mode="expand", fontsize=6) # 
# plt.legend(bbox_to_anchor=(1.05, 1), borderaxespad=0.) # loc=2,
plt.show()





exit()


fig_dims = (10, 20)
fig, ax = plt.subplots(figsize=fig_dims)




ax = sns.boxplot(x="search_context", y="value", ax=ax, data=df_calculated_metric[df_calculated_metric['cod_metric']=='nDCG@10'])
#plt.xticks(rotation=0)
ax.set(ylabel = 'nDCG@10', xlabel = 'context')
plt.legend(loc='upper right', fontsize=6)
ax.set_title('Comparative of nDCG@10: search context [boxplot]')
#plt.tight_layout()
fig.savefig('graphics\comparative_search_context_boxplot', transparent=False, dpi=80, bbox_inches='tight')
plt.show()

df_nDCG[['BM25_nDCG@10', 'Rerank_nDCG@10', 'Dense_nDCG@10']].describe()

fig, ax = plt.subplots()
ax.set_title('Queries originais - nDCG@10')
ax.boxplot(df_nDCG[['BM25_nDCG@10', 'Rerank_nDCG@10', 'Dense_nDCG@10']].values, vert=False)
ax.set(yticklabels=['BM25', 'BM25+Rerank', 'Dense_nDCG@10'])
fig.show()
fig.savefig('ndcg10_originals_boxplot.png', transparent=False, dpi=80, bbox_inches='tight')


data = df_nDCG.to_dict(orient='index')
for i, query in enumerate(sorted(data.keys(), reverse=True)):
  print(data[query]['BM25_nDCG@10'],data[query]['Rerank_nDCG@10'],data[query]['Dense_nDCG@10'])
  valores = numpy.array([data[query]['BM25_nDCG@10'],data[query]['Rerank_nDCG@10'],data[query]['Dense_nDCG@10']])
  print(valores)
  ordem = (-valores).argsort()
  print('ordem', ordem)
  if i > 2: break 

print(len(ordem))


x = 'BM25_nDCG@10'
x.split('_')[0]



fig = plt.figure(figsize=(10, 20))
ax = fig.subplots()
data = df_nDCG.to_dict(orient='index')

Y = np.zeros(10)
yticklabels = []

def plot_query(x, y, linestyle, dotstyle, color, label):
    if y:
        label = None
    ax.plot(np.linspace(0, x, 10), Y+i, linestyle=linestyle, linewidth=1.5, color=color, label=label)
    ax.plot(x, y, dotstyle)

metodos = ['BM25_nDCG@10','Rerank_nDCG@10','Dense_nDCG@10']
formato = ['solid', 'dashed', 'dotted']
cores = ['blue', 'green', 'red']
marcas = ['bo', 'go', 'ro']

for i, query in enumerate(sorted(data.keys(), reverse=True)):

  valores = numpy.array([data[query]['BM25_nDCG@10'],data[query]['Rerank_nDCG@10'],data[query]['Dense_nDCG@10']])
  #print(valores)
  ordem = (-valores).argsort()

  nDCG_BM25 = data[query]['BM25_nDCG@10']
  nDCG_rerank = data[query]['Rerank_nDCG@10']
  nDCG_dense = data[query]['Dense_nDCG@10']

  for pos in range(len(ordem)):
    prox_pos = ordem[pos]
    plot_query(data[query][metodos[prox_pos]], i, formato[prox_pos], marcas[prox_pos], cores[prox_pos], metodos[prox_pos].split('_')[0])

  yticklabels.append(data[query]['Text'])

#médias:
#ax.plot(np.zeros(10) + 100 * df_nDCG['BM25_nDCG@10'].mean(), np.linspace(-0.5, len(data), 10), linestyle='solid', linewidth=.5, color='blue')
#ax.plot(np.zeros(10) + 100 * df_nDCG['Rerank_nDCG@10'].mean(), np.linspace(-0.5, len(data), 10), linestyle='dashed', linewidth=.5, color='green')
#dotted, dashdot

legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large')
ax.set_title('Queries originais')
ax.set(ylim=(-1, len(data)+3.5),
        yticks=np.arange(len(data)), 
        xticks=np.arange(0, 1.10, .20),
        yticklabels=yticklabels)
ax.set_xlabel('nDCG@10')
ax.tick_params(left=False, bottom=True, labelbottom=True)
fig.savefig('ndcg10_originals.png', transparent=False, dpi=80, bbox_inches='tight')


fig, ax = plt.subplots(figsize=(5, 5))
data = df_nDCG[['BM25_nDCG@10', 'Rerank_nDCG@10', 'Dense_nDCG@10']].mean().to_dict()

ax.plot(np.zeros(10)+2, np.linspace(0, data['BM25_nDCG@10'], 10), linestyle='solid', linewidth=1, color='blue', label='BM25')
ax.plot(np.zeros(10), np.linspace(0, data['Rerank_nDCG@10'], 10), linestyle='solid', linewidth=1, color='green', label='BM25+Rerank')
ax.plot(np.zeros(10)+1, np.linspace(0, data['Dense_nDCG@10'], 10), linestyle='solid', linewidth=1, color='red', label='Dense')

ax.plot(2, data['BM25_nDCG@10'], 'bo')
ax.plot(0, data['Rerank_nDCG@10'], 'gs')
ax.plot(1, data['Dense_nDCG@10'], 'rd')

legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large')
ax.set_title('Queries originais - médias')
ax.set(ylim=(0, 1.2), xlim=(-20, 20),
        yticks=np.arange(0, 1.1, .2))
ax.set_ylabel('nDCG@10')
ax.tick_params(left=True, bottom=False, labelbottom=False)
fig.savefig('ndcg10_originals_means.png', transparent=False, dpi=80, bbox_inches='tight')
plt.show()