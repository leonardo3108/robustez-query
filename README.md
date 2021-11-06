# Análise de Robustez de Mecanismos de Busca Quanto a Ruídos na Query

**Autores:** Leonardo Augusto da Silva Pacheco e  Marcus Vinícius Borela de Castro

**Projeto Final da Disciplina** [IA376, Turma E - Tópicos em Engenharia de Computação VII - 2021.2S](https://www.dac.unicamp.br/portal/caderno-de-horarios/2021/2/S/P/FEEC/IA376) - **Deep Learning for NLP**

## Documentação do projeto
* [Apresentação inicial](https://docs.google.com/presentation/d/1ABkHVwfJ2r5Sga0m-WXv1LlMiF9o8vpB7wpiZ8N5Oa8/edit?usp=sharing)

## Datasets
Dados:
* NIST judgments for the Passage Ranking task: https://trec.nist.gov/data/deep/2020qrels-pass.txt
* MS MARCO Passage Queries: https://msmarco.blob.core.windows.net/msmarcoranking/queries.tar.gz
* MS MARCO Passages: https://msmarco.blob.core.windows.net/msmarcoranking/collection.tar.gz

Mais informações:
* TREC 2020 Deep Learning Track: https://trec.nist.gov/data/deep2020.html
* TREC 2020 Deep Learning Track Guidelines: https://microsoft.github.io/msmarco/TREC-Deep-Learning-2020

## Dados preparados
Queries originais:
* 54 queries do TREC 2020 DL Track sobre MsMarco passages: [queries-originals.txt](https://github.com/leonardo3108/robustez-query/blob/main/queries-originals.txt)
* DCG@10 (BM25 e rerank): [dcg10_originals.csv](https://github.com/leonardo3108/robustez-query/blob/main/dcg10_originals.csv)
* nDCG@10 (BM25 e rerank): [ndcg10_originals.csv](https://github.com/leonardo3108/robustez-query/blob/main/ndcg10_originals.csv)

## Cadernos
1. Análise exploratória dos datasets: [Exploring TREC Deep Learning 2020.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/Exploring%20TREC%20Deep%20Learning%202020.ipynb)
2. Obtenção do IDCG das queries originais: [IDCG.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/IDCG.ipynb)
3. Teste básico de uso do BM25 e Rerank sobre o MsMarco Passage: [Teste Marco Passage + BM25 + Rerank.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/Teste%20Marco%20Passage%20+%20BM25%20+%20Rerank.ipynb)
4. Obtenção do nDCG@10 do BM25 sobre as queries originais: [Originals + BM25 + nDCG.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/Originals%20%2B%20BM25%20%2B%20nDCG.ipynb)
5. Obtenção do nDCG@10 do BM25+Rerank (MonoT5) sobre as queries originais: [Originals + BM25 + Rerank + nDCG.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/Originals%20%2B%20BM25%20%2B%20Rerank%20%2B%20nDCG.ipynb)
6. Consolidação das métricas: [Consolidação das métricas.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/Consolida%C3%A7%C3%A3o%20das%20m%C3%A9tricas.ipynb)

## Próximos passos (TO DO):
- Ver issues: https://github.com/leonardo3108/robustez-query/issues
- Ver kanban: https://github.com/users/leonardo3108/projects/1

## Referências:
* [Pretrained Transformers for Text Ranking: BERT and Beyond. Jimmy Lin, Rodrigo Nogueira, and Andrew Yates](https://arxiv.org/abs/2010.06467) ([anotações](https://github.com/leonardo3108/robustez-query/blob/main/Pretrained%20Transformers%20for%20Text%20Ranking%20-%20BERT%20and%20Beyond.pdf))
* [Overview of the TREC 2020 Deep Learning Track](https://arxiv.org/abs/2102.07662) ([anotações](https://github.com/leonardo3108/robustez-query/blob/main/OVERVIEW%20OF%20THE%20TREC%202020%20DEEP%20LEARNING%20TRACK.pdf))
* [Pyserini](https://github.com/castorini/pyserini) - toolkit for reproducible information retrieval research with sparse and dense representations
* [PyGaggle](https://github.com/castorini/pygaggle/) - gaggle of deep neural architectures for text ranking and question answering
