from haystack.document_stores import InMemoryDocumentStore
from sentence_transformers import SentenceTransformer, util
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import EmbeddingRetriever
from haystack.pipelines import ExtractiveQAPipeline
from haystack.nodes import FARMReader
from pprint import pprint
from haystack.utils import print_answers
from haystack.utils import fetch_archive_from_http
from haystack.nodes import BM25Retriever
import os
from haystack.pipelines import Pipeline

from haystack.pipelines.standard_pipelines import TextIndexingPipeline


document_store = ElasticsearchDocumentStore(
    similarity="dot_product",
    embedding_dim=768
)

doc_dir = "corpus\content\manuals_dump"

files_to_index = [doc_dir + "/" + f for f in os.listdir(doc_dir)]
indexing_pipeline = TextIndexingPipeline(document_store)
indexing_pipeline.run_batch(file_paths=files_to_index)

retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model="sentence-transformers/multi-qa-mpnet-base-dot-v1",
    model_format="sentence_transformers"
)

document_store.update_embeddings(retriever)

reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)

pipe = ExtractiveQAPipeline(reader, retriever)

prediction = pipe.run(
    query="How do I change the radio frequencies?",
    params={
        "Retriever": {"top_k": 20},
        "Reader": {"top_k": 20}
    }
)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
pprint(prediction)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print_answers(
    prediction,
    details="minimum" ## Choose from `minimum`, `medium`, and `all`
)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print_answers(
    prediction,
    details="all" ## Choose from `minimum`, `medium`, and `all`
)