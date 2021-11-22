from haystack.retriever import ElasticsearchRetriever
from haystack.retriever.dense import DensePassageRetriever

def init_retriever_es_bm25(document_store):
    retriever = ElasticsearchRetriever(document_store)
    return retriever


def init_retriever_es_dpr(document_store):
    retriever = DensePassageRetriever(
    document_store=document_store,
    query_embedding_model='facebook/dpr-question_encoder-single-nq-base',
    passage_embedding_model='facebook/dpr-ctx_encoder-single-nq-base',
    # use_gpu=True, 
    use_gpu=False,
    embed_title=True
    )
    return retriever
