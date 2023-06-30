import json
import hashlib
from pathlib import Path

input_filepath = Path('./data/questions.json')
# load data from JSON file
with open(input_filepath, 'r') as f:
    data = json.load(f)

# function to hash question-answer pair
def hash_pair(pair):
    return hashlib.md5((pair['question'] + pair['answer']).encode('utf-8')).hexdigest()

# function to remove duplicates
def remove_duplicates(data):
    seen_hashes = set()
    no_duplicates = []

    for pair in data:
        pair_hash = hash_pair(pair)

        if pair_hash not in seen_hashes:
            seen_hashes.add(pair_hash)
            no_duplicates.append(pair)

    return no_duplicates

# remove duplicates
data = remove_duplicates(data)
output_filepath = Path('./data/questions_postProcess.json')
# write the filtered data back to JSON
with open(output_filepath, 'w') as f:
    json.dump(data, f)
