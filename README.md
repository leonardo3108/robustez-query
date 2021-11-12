# Análise de Robustez de Mecanismos de Busca Quanto a Ruídos na Query

**Projeto Final da Disciplina**  [IA376, Turma E - Tópicos em Engenharia de Computação VII - 2021.2S](https://www.dac.unicamp.br/portal/caderno-de-horarios/2021/2/S/P/FEEC/IA376)

**Deep Learning for NLP**

**Autores:** Leonardo Augusto da Silva Pacheco e  Marcus Vinícius Borela de Castro

## Documentação do projeto
* [Apresentação inicial](https://docs.google.com/presentation/d/1ABkHVwfJ2r5Sga0m-WXv1LlMiF9o8vpB7wpiZ8N5Oa8/edit?usp=sharing)
* [Apresentação 11/11/2021](https://github.com/leonardo3108/robustez-query/blob/main/docs/presentations/Apresenta%C3%A7%C3%A3o%202%20-%2020211111.pptx) (entrega parcial 1)

## Datasets
Dados:
* NIST judgments for the Passage Ranking task: https://trec.nist.gov/data/deep/2020qrels-pass.txt
* MS MARCO Passage Queries: https://msmarco.blob.core.windows.net/msmarcoranking/queries.tar.gz
* MS MARCO Passages: https://msmarco.blob.core.windows.net/msmarcoranking/collection.tar.gz

Informações adicionais:
* TREC 2020 Deep Learning Track: https://trec.nist.gov/data/deep2020.html
* TREC 2020 Deep Learning Track Guidelines: https://microsoft.github.io/msmarco/TREC-Deep-Learning-2020
* MS MARCO: https://microsoft.github.io/msmarco/

## Cadernos
* Análise exploratória dos datasets: [Exploring TREC Deep Learning 2020.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/code/Exploring%20TREC%20Deep%20Learning%202020.ipynb)
* Teste básico de uso do BM25 e Rerank sobre o MsMarco Passage: [Teste Marco Passage + BM25 + Rerank.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/code/Teste%20Marco%20Passage%20+%20BM25%20+%20Rerank.ipynb)
* Obtenção do nDCG@10 do BM25+Busca Densa sobre as queries originais: [Originals + Dense + nDCG.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/code/gerar_dcg10_por_dense_retrieval_base_passagens_com_julgamento_local.ipynb)
* Obtenção do nDCG@10 do BM25 sobre as queries originais: [Originals + BM25 + nDCG.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/code/Originals%20%2B%20BM25%20%2B%20nDCG.ipynb)
* Obtenção do nDCG@10 do BM25+Rerank (MonoT5) sobre as queries originais: [Originals + BM25 + Rerank + nDCG.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/code/Originals%20%2B%20BM25%20%2B%20Rerank%20%2B%20nDCG.ipynb)
* Consolidação das métricas: [consolidar_metricas.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/code/consolidar_metricas.ipynb)
* Geração de gráficos: [gerar_graficos_comparacao_metodos.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/code/gerar_graficos_comparacao_metodos.ipynb)

## Dados preparados
Queries originais:
* 54 queries do TREC 2020 DL Track sobre MsMarco passages: [queries-originals.txt](https://github.com/leonardo3108/robustez-query/blob/main/data/queries-originals.txt)
* Passagens com julgamentos do TREC 2020 DL Track: [passages-with-judment.txt](https://raw.githubusercontent.com/leonardo3108/robustez-query/main/data/passages-with-judment.txt) (utilizado na busca densa)
* DCG@10 (BM25, rerank e densa) e IDCG@10: [dcg10_originals.csv](https://github.com/leonardo3108/robustez-query/blob/main/data/dcg10_originals.csv)
* nDCG@10 (BM25, rerank e densa): [ndcg10_originals.csv](https://github.com/leonardo3108/robustez-query/blob/main/data/ndcg10_originals.csv)


## Ruídos
Serão analisados os impactos dos seguintes tipos de ruídos:
* permutação de palavras a uma probabilidade de 10%, com limite de 3 palavras(1)
* deleção de palavras a uma probabilidade de 10%(1)
* tradução para outra língua e retorno à língua original
* alguns erros ortográficos comuns   


(1) Código adaptado do utilizado na colocação de ruídos aplicada no artigo [Understanding Back-Translation at Scale. Edunov et al. 2018.](https://arxiv.org/abs/1808.09381)


## Próximos passos (TO DO):
- Ver issues: https://github.com/leonardo3108/robustez-query/issues
- Ver kanban: https://github.com/users/leonardo3108/projects/1?fullscreen=true

## Referências:
* [Pretrained Transformers for Text Ranking: BERT and Beyond. Jimmy Lin, Rodrigo Nogueira, and Andrew Yates](https://arxiv.org/abs/2010.06467) ([anotações](https://github.com/leonardo3108/robustez-query/blob/main/docs/references/Pretrained%20Transformers%20for%20Text%20Ranking%20-%20BERT%20and%20Beyond.pdf))
* [Overview of the TREC 2020 Deep Learning Track](https://arxiv.org/abs/2102.07662) ([anotações](https://github.com/leonardo3108/robustez-query/blob/main/docs/references/OVERVIEW%20OF%20THE%20TREC%202020%20DEEP%20LEARNING%20TRACK.pdf))
* [Pyserini](https://github.com/castorini/pyserini) - toolkit for reproducible information retrieval research with sparse and dense representations
* [PyGaggle](https://github.com/castorini/pygaggle/) - gaggle of deep neural architectures for text ranking and question answering
* [Pyserini: An Easy-to-Use Python Toolkit to Support Replicable IR Research with Sparse and Dense Representations. Lin, Jimmy & Ma, Xueguang & Lin, Sheng-Chieh & Yang, Jheng-Hong & Pradeep, Ronak & Nogueira, Rodrigo. (2021).](https://cs.uwaterloo.ca/~jimmylin/publications/Lin_etal_SIGIR2021_Pyserini.pdf)
