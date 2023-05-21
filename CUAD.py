import json
import os

with open('CUAD/CUAD_v1.json', 'r', encoding="utf-8") as openfile:
    json_object = json.load(openfile)

json_object_part = {"version":"aok_v1.0","data":[]}
json_object_part2 = {"version":"aok_v1.0","data":[]}
json_object_part3 = {"version":"aok_v1.0","data":[]}
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

            # if random.randint(0,5) != 0:# or item_c["is_impossible"]:
            #     questions_to_delete.append(item_c)
            #     continue

            new_question = question[question.index("Details: ")+9:]
            item_c["question"] = new_question

            if len(item_c["answers"]) == 0:
                questions_to_delete.append(item_c)

        for to_delete in questions_to_delete:
            item_b["qas"].remove(to_delete)
        # if len(item_b["qas"]) == 0:
        #     docs_to_remove.append(item_a)
    count += 1
    #if count >= (530 // 1) * (part) and count < (530 // 1) * (part + 1) :
    if int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1) < 0.20:
        json_object_part2["data"].append(item_a)
    else:
        if int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1) < 0.50:
            json_object_part["data"].append(item_a)
        else:
            json_object_part3["data"].append(item_a)


print(len(json_object_part2["data"]))
print(len(json_object_part["data"]))
print(len(json_object_part3["data"]))
# for to_delete in docs_to_remove:
#     json_object["data"].remove(to_delete)

with open("CUADCompleteAnswerable_training1.json", "w") as outfile:
    json.dump(json_object_part, outfile)
with open("CUADCompleteAnswerable_dev.json", "w") as outfile:
    json.dump(json_object_part2, outfile)
    with open("CUADCompleteAnswerable_training2.json", "w") as outfile:
        json.dump(json_object_part3, outfile)