tech_questions = "D:\\Pycharm\\Thesis\\TechQA\\TechQA\\training_and_dev\\dev_Q_A.json"
tech_documents = "D:\\Pycharm\\Thesis\\TechQA\\TechQA\\training_and_dev\\training_dev_technotes.json"
#tech_questions_val = "D:\\Pycharm\\Thesis\\TechQA\\TechQA\\validation\\validation_questions.json"
import json
import random

f1 = open(tech_documents)
all_documents = {}
data1 = json.load(f1)
for i in data1:
    doc = data1[i]
    DOC_ID = i
    DOC_CONTENT = doc["text"]
    all_documents[DOC_ID] = DOC_CONTENT

f = open(tech_questions)
data = json.load(f)

all_questions = {}

questionss = {}
count = 0
for i in data:
    # count+=1
    # print(count)
    # continue
    QUESTION_ID = i['QUESTION_ID']
    QUESTION_TITLE = i['QUESTION_TITLE']
    QUESTION_TEXT = i['QUESTION_TEXT']
    if QUESTION_TEXT == "":
        QUESTION_TEXT = QUESTION_TITLE
        if QUESTION_TEXT == "":
            continue
    DOCUMENT = i['DOCUMENT']
    ANSWER = i['ANSWER']
    START_OFFSET = i['START_OFFSET']
    END_OFFSET = i['END_OFFSET']
    ANSWERABLE = i['ANSWERABLE']
    if ANSWERABLE == "N":
        ANSWERABLE = False
        START_OFFSET = -1
        END_OFFSET = 0
        ANSWER = ""
    else:
        ANSWERABLE = True
        START_OFFSET = int(START_OFFSET)
        END_OFFSET = int(END_OFFSET)
    DOC_IDS = i['DOC_IDS']
    count += 1
    print(count)
    DOC_ID_RANDOM = DOCUMENT
    if DOCUMENT == "-":
        DOC_ID_RANDOM = random.choice(DOC_IDS)

    DOC_CONTENT = all_documents[DOC_ID_RANDOM]

    question = {
        "question": QUESTION_TEXT,
        "id": QUESTION_ID,
        "answers": [
            {
                "answer_id": random.randint(0, 100000000),
                "document_id": DOC_ID_RANDOM,
                "question_id": QUESTION_ID,
                "text": ANSWER,
                "answer_start": START_OFFSET,
                "answer_end": END_OFFSET,
                "answer_category": None
            }
        ],
        "is_impossible": not ANSWERABLE
    }
    if DOCUMENT in questionss:
        questionss[DOC_ID_RANDOM]["q"].append(question)
    else:
        questionss[DOC_ID_RANDOM] = {"q": [question], "context": DOC_CONTENT, "document_id": DOC_ID_RANDOM,"all_doc_ids":i['DOC_IDS']}

squad = {"data": []}

for q in questionss:
    value = questionss[q]

    paragraphs = []

    qas = value["q"]
    context = value["context"]
    document_id = value["document_id"]

    squad["data"].append({
        "paragraphs": [
            {
                "qas": qas,
                "context": context,
                "document_id": document_id,
                "all_doc_ids":value["all_doc_ids"]
            }
        ]
    })
with open("dev_including_all_docs.json", "w") as outfile:
    json.dump(squad, outfile)
