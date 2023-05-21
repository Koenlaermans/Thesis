tech_questions = "D:\\Pycharm\\Thesis\\sample.json"
import json
import random

f1 = open(tech_questions)

data1 = json.load(f1)
count = 0
#print("Here are 2 technical documents and a question about the document and the answer. The beginning of a document is marked by '*-*-*-*'. Come up with a different question about each document. Also give the answer.")
#print("Ask a technical question about the following document as if you were a user with a technical problem and also extract the paragraph containing the answer from the document. There should be as little overlap as possible between question and answer: ")
for i in data1["data"][8:10]:
    print("\nDocument: ")
    print('"'+i["paragraphs"][0]["context"]+'"') # without overlap between question and document
    print("")
    print("Ask a technical question about the previous technical document. Extract the exact answer from the document without rewording:")
    print("\nQuestion: ")
    print(i["paragraphs"][0]["qas"][0]["question"].replace("\n", ""))
    print("\nAnswer: ")
    print(i["paragraphs"][0]["qas"][0]["answers"][0]["text"])


print("\nAsk a technical question about the previous technical document. Extract the exact answer from the document without rewording:")

# a = i["paragraphs"][0]
    # if a["qas"][0]["is_impossible"]:
    #     continue
    # q = a["qas"][0]["question"].replace("\n", "")
    # ans = a["qas"][0]["answers"][0]["text"]
    # context = a["context"]
    # print("*-*-*-*")
    # print("Document: ")
    # print(context)
    # print("Question: ")
    # print(q)
    # print("Answer:")
    # print(ans)
    # count+=1
    # if count == 2:
    #     break
