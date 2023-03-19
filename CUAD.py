import json
import random

with open('CUAD/CUAD_v1.json', 'r', encoding="utf-8") as openfile:
    json_object = json.load(openfile)

count = 0
docs_to_remove = []
ans_count_max = 0
ans_counts = []
for item_a in json_object["data"]:
    for item_b in item_a["paragraphs"]:
        questions_to_delete = []

        for item_c in item_b["qas"]:
            question = item_c["question"]

            ans_count_max = max(ans_count_max, len(item_c["answers"]))
            ans_counts.append(len(item_c["answers"]))

            if len(item_c["answers"]) > 6:
                item_c["answers"] = item_c["answers"][:6]

            if random.randint(0,5) != 0:
                questions_to_delete.append(item_c)
                continue

            count += 1

            new_question = question[question.index("Details: ")+9:]
            item_c["question"] = new_question

        for to_delete in questions_to_delete:
            item_b["qas"].remove(to_delete)
        if len(item_b["qas"]) == 0:
            docs_to_remove.append(item_a)

for to_delete in docs_to_remove:
    json_object["data"].remove(to_delete)

with open("CUAD.json", "w") as outfile:
    json.dump(json_object, outfile)
