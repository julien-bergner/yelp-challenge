#!/usr/local/bin/python3
import sys
import json
from datetime import datetime

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer

import helper

if len(sys.argv) != 3:
    sys.exit("Usage: filter_py_language.py source_file target_file")

print("Start: ", str(datetime.now()))

source_file = open(sys.argv[1], "r")
target_file = open(sys.argv[2], "w")
print("Source file: ", source_file.name)
print("Target file: ", target_file.name)

stemmer = PorterStemmer()

with source_file as source:
    for review in source:

    	  # Load review text
        parsed_json = json.loads(review)
        raw_review_text = parsed_json['text']

        # Remove newline and indent characters
        raw_review_text = raw_review_text.replace("w/", "")
        raw_review_text = raw_review_text.replace("\n", "")

        # Lowercase
        raw_lower = raw_review_text.lower()

        # Expand contractions
        raw_expanded = helper.expand_contractions(raw_lower)

        # Tokenize
        tokens = RegexpTokenizer(r'\w+').tokenize(raw_expanded)

        # Remove stop words
        stop_words = get_stop_words('en')
        stopped_tokens = [i for i in tokens if not i in stop_words]

        # Stem tokens
        stemmed_tokens = [stemmer.stem(i) for i in stopped_tokens]

        target_file.write(json.dumps(stopped_tokens))
        target_file.write('\n')

print("End: ", str(datetime.now()))

