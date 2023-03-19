import csv
import requests
from bs4 import BeautifulSoup

# f = open("./TechQA/TechQA/technote_corpus/full_technote_collection.txt", "r")
# for x in f:
#   print(x)

# with open('emanual_annotated/smart_tv_remote_50_questions.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     count =0
#     for row in spamreader:
#         count +=1
#         if count > 1:
#             question = row[1]
#             webpage = row[3]
#             answer = row[4]
#             # print(question)
#             # print(webpage)
#             # print(answer)
#
#             r = requests.get(webpage)
#             soup = BeautifulSoup(r.content, 'html.parser')
#             content = soup.find("div", class_="pdf").get_text().replace("\n",". ")
#             content = content.replace("●","")
#             content = content.replace("..", ".")
#             content = content.replace(". .", ".")
#             print(content)
#
#             break