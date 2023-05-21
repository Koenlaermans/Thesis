import json
import re
import random
training_set = "D:\\Pycharm\\Thesis\\sample.json"
dev_set = "D:\\Pycharm\\Thesis\\dev.json"
cuad = "D:\\Pycharm\\Thesis\\CUADCompleteAnswerable.json"
#
# ttt="ment class\n\n1. Launch FEM\n2. Expand the object store and document class tree. Right click on the document class and select \"Properties\"\n3. Go to \"Properties Definitions\" tab, highlight the property definition and click \"Edit\"\n4. Make the modification and click OK\n5. Click OK again to save the change\n\nHow to perform the same operation with FileNet Content Engine - ACCE? \n\nANSWER\nFollow the below steps to update the property definition properties on ACCE: \n\n\n\n\n 1. Launch ACCE \n 2. Expand the object stores folder and click the object store to open the Object store tab \n 3. Expand the Data Design folder and Classes folder. Click the document class to open Document Class tab \n 4. From Properties tab, open Property Definitions drop down and select the property definition you want to modify \n 5. ACCE will open that property definition in a new Properties tab \n 6. Modify the property definition as required \n 7. Go back to the Class Definition tab and click Save"
# print(ttt.index("click Save")+9)#722:966
# print(ttt[381:967])
# # print(ttt.index("ed by the application directly in the instan"))
# # print(ttt.index(".ibm.")+5)
# exit(0)

file = open(cuad)
dataset = json.load(file)

count = 0
for para in dataset['data']:
    # para_data = para["paragraphs"][0]
    # lenn = len(para_data["qas"])
    # if lenn!=1:
    #     print(lenn)
    #print(count)
    count+=1
    para_data = para["paragraphs"][0]
    question_data = para_data["qas"][0]
    impossible = question_data["is_impossible"]
    answer_data =  question_data["answers"][0]
    answer = answer_data["text"]


    if not impossible:

        try:
            answer_index = para_data["context"].index(answer)
        except:
            print("error "+str(count))
            continue

        answer_length_in_tokens = int(len(answer)/5)
        residual_tokens = max(0, 512-answer_length_in_tokens)
        rand = random.randint(max(0, answer_index-(residual_tokens*5)), answer_index)

        start = rand
        end = answer_index+len(answer)+5000

        doc_new = para_data["context"][start:end]
        para_data["context"] = doc_new

        answer_data["answer_start"] = para_data["context"].index(answer)
        answer_data["answer_end"] = para_data["context"].index(answer)+len(answer)

    else:
        doc_wc = " ".join(para_data["context"].split(' ')[:512])

    para_data["qas"] = para_data["qas"][:1]



with open("sample_short_doc.json", "w") as outfile:
    json.dump(dataset, outfile)







