tech_questions = "D:\\Pycharm\\Thesis\\TechQA\\TechQA\\training_and_dev\\training_Q_A.json"
tech_documents = "D:\\Pycharm\\Thesis\\TechQA\\TechQA\\training_and_dev\\training_dev_technotes.json"
samples = "D:\\Pycharm\\Thesis\\sample.json"

import json
import random

f1 = open(samples)
all_question_documents = []
data1 = json.load(f1)

for i in data1["data"][:300]:

    id = i["paragraphs"][0]["document_id"]
    impossible = i["paragraphs"][0]["qas"][0]["is_impossible"]
    answer = i["paragraphs"][0]["qas"][0]["answers"][0]["text"]

    if not impossible and answer!="":
        all_question_documents.append(id)

# print(len(all_question_documents))
# print(all_question_documents[:5])


f = open(tech_documents)
data = json.load(f)

filtered_documents = {}

for i in data:
    if i in all_question_documents:
        if i in filtered_documents:
            print(i)
        filtered_documents[i] = data[i]

print(len(filtered_documents))

with open("training_technotes_in_questions.json", "w") as outfile:
    json.dump(filtered_documents, outfile)
