tech_questions = "D:\\Pycharm\\Thesis\\dev.json"

import json
import random

f1 = open(tech_questions)

data = json.load(f1)
labels = []
for i in data["data"]:
    qas = i["paragraphs"][0]["qas"]
    context = i["paragraphs"][0]["context"]
    document_id = i["paragraphs"][0]["document_id"]

    new_label = {
        "query":qas[0]["question"],
        "document":{
            "content":context,
            "content_type":"text",
            "id":document_id
        },
        "is_correct_answer":True,
        "is_correct_document":True,
        "origin":"gold-label",
        "answer":{
            "answer":qas[0]["answers"][0]["text"]
        },
        "no_answer":qas[0]["is_impossible"]
    }
    labels.append(new_label)

squad = {"labels":labels}

with open("dev_eval.json", "w") as outfile:
    json.dump(squad, outfile)