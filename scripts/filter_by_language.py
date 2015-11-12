#!/usr/local/bin/python3

# This scripts reads the reviews, detects their language and writes
# then to target_file_en or target_file_de depending on their language.

import sys
import json
import pdb
from datetime import datetime
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

if len(sys.argv) != 4:
    sys.exit("Usage: filter_py_language.py source_file target_file_en target_file_de")

print("Start: ", str(datetime.now()))

source_file = open(sys.argv[1], "r")
target_file_en = open(sys.argv[2], "w")
target_file_de = open(sys.argv[3], "w")
print("Source file: ", source_file.name)
print("Target file: ", target_file.name)

with source_file as source:
    for review in source:

        parsed_json = json.loads(review)
        review_id = parsed_json['review_id']
        review_text = parsed_json['text']

        try:
            language = detect(review_text)
            line = { "review_id" : review_id, "text" : review_text }

            if language == 'en':
                target_file_en.write(json.dumps(line))
                target_file_en.write('\n')
            elif language == 'de':
                target_file_de.write(json.dumps(line))
                target_file_de.write('\n')
            else:
                print("Other language: ", language, parsed_json)

        except LangDetectException:
            pass

print("End: ", str(datetime.now()))

