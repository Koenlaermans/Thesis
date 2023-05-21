tech_questions = "D:\\Pycharm\\Thesis\\dev_eval.json"
#tech_questions = "D:\\Pycharm\\Thesis\\dev_technotes_in_questions.json"

import json
import random

f1 = open(tech_questions)

data1 = json.load(f1)

print("#################################################")
#print("Here are 2 technical documents and a question about the document and the answer. The beginning of a document is marked by '*-*-*-*'. Come up with a different question about each document. Also give the answer.")
print("Ask a technical question about the following document as if you were a user with a technical problem. Give the start and end index of the answer:")
count =0
for i in data1["labels"]:
    query = i["query"]
    ctx = i["document"]["content"]
    print(ctx)
    break

print("#################################################")