# Análise de Robustez de Mecanismos de Busca Quanto a Ruídos na Query
Autores: Leonardo Augusto da Silva Pacheco e  Marcus Vinícius Borela de Castro

## Projeto Final da Disciplina DL for NLP

Documentação do projeto:
* Apresentação do Projeto: https://docs.google.com/presentation/d/1ABkHVwfJ2r5Sga0m-WXv1LlMiF9o8vpB7wpiZ8N5Oa8/edit?usp=sharing

Datasets:
* NIST judgments for the Passage Ranking task: https://trec.nist.gov/data/deep/2020qrels-pass.txt
* MS MARCO Passage Queries: https://msmarco.blob.core.windows.net/msmarcoranking/queries.tar.gz
* MS MARCO Passages: https://msmarco.blob.core.windows.net/msmarcoranking/collection.tar.gz

Mais informações:
* TREC 2020 Deep Learning Track: https://trec.nist.gov/data/deep2020.html
* TREC 2020 Deep Learning Track Guidelines: https://microsoft.github.io/msmarco/TREC-Deep-Learning-2020

Dados preparados:
* 54 queries do TREC 2020 DL Track sobre MsMarco passages: https://github.com/leonardo3108/robustez-query/blob/main/queries-originals.txt

Cadernos:
1 - Análise exploratória dos datasets: [Exploring TREC Deep Learning 2020.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/Exploring%20TREC%20Deep%20Learning%202020.ipynb)
2 - Teste básico de uso do BM25 e Rerank sobre o MsMarco Passage: [Teste Marco Passage + BM25 + Rerank.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/Teste%20Marco%20Passage%20%2B%20BM25%20%2B%20Rerank.ipynb)
3 - Obtenção de efetividade do BM25 sobre as queries originais: [Originals + BM25 + nDCG.ipynb](https://github.com/leonardo3108/robustez-query/blob/main/Originals%20%2B%20BM25%20%2B%20nDCG.ipynb)

Outras referências:
* Tutorial - Livro: Pretrained Transformers for Text Ranking: BERT and Beyond. Jimmy Lin,1 Rodrigo Nogueira,1 and Andrew Yates: https://drive.google.com/file/d/1d0DEGZb83m16LBVMJcEsmtjS2CjBzxZq/view?usp=sharing
