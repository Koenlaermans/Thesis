tech_questions = "D:\\Pycharm\\Thesis\\dev.json"
import json
import random
import re
f1 = open(tech_questions)

data1 = json.load(f1)
count = 0
count2=0
#print("Here are 2 technical documents and a question about the document and the answer. The beginning of a document is marked by '*-*-*-*'. Come up with a different question about each document. Also give the answer.")
#print("Ask a technical question about the following document as if you were a user with a technical problem and also extract the paragraph containing the answer from the document. There should be as little overlap as possible between question and answer: ")

for i in data1["data"]:

    if i["paragraphs"][0]["qas"][0]["is_impossible"]:
        count+=1
    else:
        count2+=1

print(count)
print(count2)
