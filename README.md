# Análise de Robustez de Mecanismos de Busca Quanto a Ruídos na Query

**Autores:** Leonardo Augusto da Silva Pacheco e  Marcus Vinícius Borela de Castro

**Projeto Final da Disciplina [Deep Learning for NLP](https://www.dac.unicamp.br/portal/caderno-de-horarios/2021/2/S/P/FEEC/IA376)**

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

## Referências:
* Tutorial - Livro: [Pretrained Transformers for Text Ranking: BERT and Beyond. Jimmy Lin,1 Rodrigo Nogueira,1 and Andrew Yates]( https://drive.google.com/file/d/1d0DEGZb83m16LBVMJcEsmtjS2CjBzxZq/view?usp=sharing)

## Dados preparados
Queries originais:
* 54 queries do TREC 2020 DL Track sobre MsMarco passages: [queries-originals.txt](https://github.com/leonardo3108/robustez-query/blob/main/queries-originals.txt)
* IDCG@10: [idcg.csv](https://github.com/leonardo3108/robustez-query/blob/main/idcg.csv)
* DCG@10 do BM25: [dcg_bm25_original.csv](https://github.com/leonardo3108/robustez-query/blob/main/dcg_bm25_original.csv)
* nDCG@10 do BM25: [ndcg_bm25_original.csv](https://github.com/leonardo3108/robustez-query/blob/main/ndcg_bm25_original.csv)

## Cadernos
* Análise exploratória dos datasets: [Exploring TREC Deep Learning 2020.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/Exploring%20TREC%20Deep%20Learning%202020.ipynb)
* Obtenção do IDCG das queries originais: [IDCG.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/Originals%20%2B%20BM25%20%2B%20nDCG.ipynb)
* Teste básico de uso do BM25 e Rerank sobre o MsMarco Passage: [Teste Marco Passage + BM25 + Rerank.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/IDCG.ipynb)
* Obtenção do nDCG do BM25 sobre as queries originais: [Originals + BM25 + nDCG.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/Originals%20%2B%20BM25%20%2B%20nDCG.ipynb)
 
