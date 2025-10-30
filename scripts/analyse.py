import gzip
import json
import os
import time

from collections import defaultdict
from spacy.tokens import DocBin


def store_as_doc_bins(docs, lang_code, doc_bin_dir):
    doc_bin_file = os.path.join(doc_bin_dir, f"parsed_reviews-{lang_code}.doc_bin")
    doc_bin = DocBin(docs=docs, store_user_data=True)
    doc_bin.to_disk(doc_bin_file)
        

def read_from_doc_bins(lang_code, doc_bin_dir, vocab):
    doc_bin_file = os.path.join(doc_bin_dir, f"parsed_reviews-{lang_code}.doc_bin")
    doc_bin = DocBin().from_disk(doc_bin_file)
    return list(doc_bin.get_docs(vocab))
        

def load_language_reviews(lang):
    review_file = f'../data/lang_reviews_sample/reviews-lang_{lang}.jsonl.gz'
    with gzip.open(review_file, 'rt') as fh:
        return [json.loads(line) for line in fh]

def sort_tokens_by_head(sent):
    head_tokens = defaultdict(list)
    for token in sent:
        head_tokens[token.head].append(token)
    return head_tokens


def has_person(token, person: int = None):
    if person is None:
        return 'Person' in token.morph.to_dict()
    elif 'Person' not in token.morph.to_dict():
        return False 
    return token.morph.to_dict()['Person'] == person
