# Search Engine Robustness Analysis for Noise in Query

**Final Project at Discipline**
[IA376, Deep Learning for NLP, Turma E - Tópicos em Engenharia de Computação VII - 2021.2S](https://www.dac.unicamp.br/portal/caderno-de-horarios/2021/2/S/P/FEEC/IA376)

**Authors:** Leonardo Augusto da Silva Pacheco e  Marcus Vinícius Borela de Castro

## Documentação do projeto
* [Apresentação inicial](https://docs.google.com/presentation/d/1ABkHVwfJ2r5Sga0m-WXv1LlMiF9o8vpB7wpiZ8N5Oa8/edit?usp=sharing)
* [Apresentação 11/11/2021](https://github.com/leonardo3108/robustez-query/blob/main/docs/presentations/Apresenta%C3%A7%C3%A3o%202%20-%2020211111.pptx) (entrega parcial 1)
* [Apresentação 11/11/2021](https://github.com/leonardo3108/robustez-query/blob/main/docs/presentations/Apresenta%C3%A7%C3%A3o%203%20-%2020211124.pptx) (entrega parcial 2)
* [Apresentação 09/12/2021](https://github.com/leonardo3108/robustez-query/blob/main/docs/presentations/Apresenta%C3%A7%C3%A3o%20final%20-%2020211209.pptx) (entrega final)
* [Relatório final](https://docs.google.com/document/d/1qKcAyIeIsg9NzwFDsiEImhU1i_mZw4Ye2pQmFh5Lbxw/edit?usp=sharing)
## Metodology
* Apply [noise kind](https://github.com/leonardo3108/robustez-query/blob/main/data/tab_noise_kind.csv)
* over [original queries](https://github.com/leonardo3108/robustez-query/blob/main/data/tab_original_query.csv)
* generating [noisy queries](https://github.com/leonardo3108/robustez-query/blob/main/data/tab_noisy_query.csv)

* Analyse impact over [ranking functions](https://github.com/leonardo3108/robustez-query/blob/main/data/tab_ranking_function.csv)
* and [text base](https://github.com/leonardo3108/robustez-query/blob/main/data/tab_text_base.csv)
* considering some Information Retrieval [Metrics](https://github.com/leonardo3108/robustez-query/blob/main/data/tab_metric.csv)

## Code
* [noise](https://github.com/leonardo3108/robustez-query/blob/main/code/noise)
* [calculation](https://github.com/leonardo3108/robustez-query/blob/main/code/calculation)
* [data manipulation](https://github.com/leonardo3108/robustez-query/blob/main/code/data_related)
* [analysis](https://github.com/leonardo3108/robustez-query/blob/main/code/analysis)
* [utility](https://github.com/leonardo3108/robustez-query/blob/main/code/util)

## Data 
Originals
* NIST judgments for the Passage Ranking task: https://trec.nist.gov/data/deep/2020qrels-pass.txt
* MS MARCO Passage Queries: https://msmarco.blob.core.windows.net/msmarcoranking/queries.tar.gz
* MS MARCO Passages: https://msmarco.blob.core.windows.net/msmarcoranking/collection.tar.gz

Manipulated
* 54 queries of TREC 2020 DL Track over MsMarco passages: [tab_original_query.csv](https://github.com/leonardo3108/robustez-query/blob/main/data/tab_original_query.csv)
* Passages with judment - TREC 2020 DL Track: [passages-with-judment.txt](https://raw.githubusercontent.com/leonardo3108/robustez-query/main/data/passages-with-judment.txt)
* All data described in [Project Data Model](https://raw.githubusercontent.com/leonardo3108/robustez-query/main/data/model/robustez-query-mer.pdf) are [avaiable](https://raw.githubusercontent.com/leonardo3108/robustez-query/main/data)

## Next steps (TO DO):
- Ver issues: https://github.com/leonardo3108/robustez-query/issues
- Ver kanban: https://github.com/users/leonardo3108/projects/1?fullscreen=true

## References:
1. [Pretrained Transformers for Text Ranking: BERT and Beyond. Jimmy Lin, Rodrigo Nogueira, and Andrew Yates](https://arxiv.org/abs/2010.06467) ([anotações](https://github.com/leonardo3108/robustez-query/blob/main/docs/references/Pretrained%20Transformers%20for%20Text%20Ranking%20-%20BERT%20and%20Beyond.pdf))
2. [Overview of the TREC 2020 Deep Learning Track](https://arxiv.org/abs/2102.07662) ([anotações](https://github.com/leonardo3108/robustez-query/blob/main/docs/references/OVERVIEW%20OF%20THE%20TREC%202020%20DEEP%20LEARNING%20TRACK.pdf))
3. [Pyserini: An Easy-to-Use Python Toolkit to Support Replicable IR Research with Sparse and Dense Representations. Lin, Jimmy & Ma, Xueguang & Lin, Sheng-Chieh & Yang, Jheng-Hong & Pradeep, Ronak & Nogueira, Rodrigo. (2021).](https://cs.uwaterloo.ca/~jimmylin/publications/Lin_etal_SIGIR2021_Pyserini.pdf)
4. [Understanding Back-Translation at Scale. Edunov et al. 2018.](https://arxiv.org/abs/1808.09381)
5. [mMARCO: A Multilingual Version of the MS MARCO Passage Ranking Dataset. Luiz Henrique Bonifacio and Israel Campiotti and Vitor Jeronymo and Roberto Lotufo and Rodrigo Nogueira.2021](https://arxiv.org/pdf/2108.13897)
6. [Dense Passage Retrieval for Open-Domain Question Answering. Vladimir Karpukhin and Barlas Oğuz and Sewon Min and Patrick Lewis and Ledell Wu and Sergey Edunov and Danqi Chen and Wen-tau Yih.2020.](https://arxiv.org/pdf/2004.04906)
7. [mT5 AMassively Multilingual Pre-trained Text-to-Text Transformer.Linting Xue and Noah Constant and Adam Roberts and Mihir Kale and Rami Al-Rfou and Aditya Siddhant and Aditya Barua and Colin Raffel.2021](https://arxiv.org/pdf/2010.11934)
8. [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer.Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu.2020](https://arxiv.org/pdf/1910.10683)
9. [The Probabilistic Relevance Framework: BM25 and Beyond.Stephen Robertson & Hugo Zaragoza. 2009](https://www.researchgate.net/publication/220613776_The_Probabilistic_Relevance_Framework_BM25_and_Beyond)


## Other links :
* [TREC 2020 Deep Learning Track](https://trec.nist.gov/data/deep2020.html)
* [TREC 2020 Deep Learning Track Guidelines](https://microsoft.github.io/msmarco/TREC-Deep-Learning-2020)
* [MS MARCO](https://microsoft.github.io/msmarco/)
* [Pyserini](https://github.com/castorini/pyserini) - toolkit for reproducible information retrieval research with sparse and dense representations
* [PyGaggle](https://github.com/castorini/pygaggle/) - gaggle of deep neural architectures for text ranking and question answering
* [Haystack](https://haystack.deepset.ai/overview/intro) 
* [huggingface-transformers](https://huggingface.co/docs/transformers/index)
* [huggingface-Unicamp](https://huggingface.co/unicamp-dl)
