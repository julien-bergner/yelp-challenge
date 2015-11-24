#!/usr/local/bin/python3

import sys
import json
from datetime import datetime

from gensim import corpora, models
import gensim

print("Start: ", str(datetime.now()))

# Open a file
file = open(sys.argv[1], "r")
print("Loaded file: ", file.name)

texts = []

with file as source:
    for review in source:
        prepared_review = json.loads(review)
        texts.append(prepared_review["tokens"])

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
print("Dictionary created: ", str(datetime.now()))

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]
print("Corpus created: ", str(datetime.now()))

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary, passes=20)

print(ldamodel.print_topics(num_topics=2, num_words=4))

print("End: ", str(datetime.now()))

