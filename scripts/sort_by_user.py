#!/usr/local/bin/python3

import sys
import json
import pdb
import os.path
from datetime import datetime

if len(sys.argv) != 3:
    sys.exit("Usage: sort_by_user.py source_file target_directory")

print("Start: ", str(datetime.now()))

source_file = open(sys.argv[1], "r")
target_directory = sys.argv[2]
print("Source file: ", source_file.name)
print("Target directory: ", target_directory)

if not os.path.exists(target_directory):
        os.makedirs(target_directory)

with source_file as source:
    for review in source:

        parsed_json = json.loads(review)
        review_id = parsed_json['review_id']
        user_id = parsed_json['user_id']
        review_text = parsed_json['text']

        output_file = open(target_directory + user_id + ".json", "w")

        line = { "review_id" : review_id, "user_id" : user_id, "text" : review_text }
        output_file.write(json.dumps(line))
        output_file.write('\n')

        output_file.close


print("End: ", str(datetime.now()))

