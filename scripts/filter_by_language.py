#!/usr/local/bin/python3

import sys
import json
import pdb
from datetime import datetime
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

if len(sys.argv) != 4:
    sys.exit("Usage: filter_py_language.py source_file target_file iso_of_language_to_filter_for")

print("Start: ", str(datetime.now()))

source_file = open(sys.argv[1], "r")
target_file = open(sys.argv[2], "w")
print("Source file: ", source_file.name)
print("Target file: ", target_file.name)

with source_file as source:
    for review in source:

        parsed_json = json.loads(review)
        review_id = parsed_json['review_id']
        review_text = parsed_json['text']

        try:
            language = detect(review_text)

            if language == sys.argv[3]:
                line = { "review_id" : review_id, "text" : review_text }
                target_file.write(json.dumps(line))
                target_file.write('\n')

        except LangDetectException:
            pass

print("End: ", str(datetime.now()))

