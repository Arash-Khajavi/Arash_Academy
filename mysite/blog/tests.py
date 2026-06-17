from django.test import TestCase

# Create your tests here.
import requests
from bs4 import BeautifulSoup
v=""
# from langchain.tools import tool
# # @tool
# def search():
#     """it uses the search engine 'google' to find information about various products according to the user's query
#                          """
#     resp = requests.get(
#      f"https://www.digikala.com")
#     # print(resp.text)
#     print(f"https://www.digikala.com")
#     soup = BeautifulSoup(resp.text, "html.parser")
#     # print(soup)
#     v+str(soup)
#     # print(soup)
#     # print(v)
#     lk=[]
#     # for i in range(len(v)):
#
#
#     for i in range(len(soup)):
#      if 'href' in str(soup):
#         d=str(soup).find("href")
#         pr=str(soup)[d:]
#         # print(pr)
#         rel=str(pr).find("rel")
#         # print(rel)
#         # print(d)
#         # print(str(soup)[d:][:rel])
#         for b in str(soup)[d:]:
#             lk.append(b)
#         print(lk)
#         h=lk.index("h")
#         print(lk[h])
#         if lk[h + 1] == 'r' and lk[h+ 2] == 'e' and lk[h+ 3] == 'f':
#            # print(lk[h + 3:]);
#             print(lk[h:h+4])
#         f=lk.index('r')
#         print(lk[f])
#         if lk[f+1] == 'e' and lk[f+2] == 'l':
#             print(lk[f:f+4])
#             print("".join(lk[h + 3:f]))
#         else:
#             lk.remove(lk[f])
#         # if 'r' in lk:
#         #     ind=lk.index('r')
#         #     if lk[ind+1] == 'e' and lk[ind+1] == 'e' and lk[ind+2] == 'l':
#         #         lk.remove('r')
#         # if 'h' in lk:
#         #     ind=lk.index('h')
#         #     if lk[ind+1] == 'r' and lk[ind+2] == 'e' and lk[ind+3] == 'f':
#         #         lk.remove('h')
#         # print(lk)
#
#
#
# search()
m="m\\nm"
k=[]
for u in m:
  k.append(u)
print(k)
ind=k.index("\\")
if k[ind+1] == "n":
    print(k[ind])
    k[ind+1] = "<br>"
    k.remove(k[ind])
    print(k)