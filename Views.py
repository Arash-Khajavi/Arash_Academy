from django.http import HttpResponse
from django.shortcuts import render,redirect
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from django import forms
class AI_page_data(forms.Form):
    user = forms.CharField(max_length=100, required=True)
l=[]
import requests
from bs4 import BeautifulSoup
import os
# def search():
#     """it uses the website https://store.paeezanstudio.com/ in order
#      to gather data"""
#     resp = requests.get(
#         f"https://store.paeezanstudio.com/")
#     print(resp.text)
#     # print(resp.text[:500])  # first 500 chars for debugging
#     soup = BeautifulSoup(resp.text, "html.parser")
#     l.append(soup)
#     print(str(soup.text))
#     # return str(soup.prettify())
# search()
# def home(request):
#  if request.POST.get("login-button") == "search":
#     return render(request, 'P.html', context={"l":"".join(str(l))})
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from langchain.tools import tool
def home(request):
  return render(request, 'g.html')
import string
def g(request):
    v=""
    if request.method == 'POST':
             def search():
                     buy=request.POST.get("user")
                     """it uses the search engine 'google' to find information about various products according to the user's query
                     """
                     resp = requests.get(
                         f"https://www.digikala.com/search/?q={str(buy)}")
                     # print(resp.text)
                     print(f"https://www.digikala.com/search/?q={str(buy)}")
                     soup = BeautifulSoup(resp.text, "html.parser")
                     # print(soup)
                     v+str(soup)
                     print(soup)
                     return HttpResponse(str(soup))
             search()
             return HttpResponse(v)
    return render(request, "Sales_main_page.html")
def funds(request):
    return render(request, "Funds.html")
def Find_A_Peer(request):
    peers={"Marcus Tailer":{'Email':'Marcus456@gmail.com', 'Grade': 12} , "Rastin Geranmaye":{'Email':'Dick@gmail.com', 'Grade': 10}
           ,"Arash Khajavi":{'Email':'arash.khajavi.ghk123@gmail.com', 'Grade': 10}}
    if request.method == "POST":
        your_grade=request.POST.get("your_grade")
        print(your_grade)
        if int(your_grade) > 12:
            raise Exception ("the maximum acceptable grade is 12")
        elif int(your_grade) <1:
            raise Exception("the minimum acceptable grade is 1")
        else:
            k=[]
            v=int(your_grade)
            h = []
            for u, m in peers.items():
                for y, b in m.items():
                    k.append(y)
                    k.append(b)
            print(k)
            for yu in k:
                if type(yu) == int:
                    h.append(yu)

            print(h)
            jh=[]
            for u, m in peers.items():
                # print(m)
                for ui in h:
                  if ui < v:
                    print(ui)
                    h.remove(ui)
                for ty in h:
                  if ty in m.values():

                        # print(p[u])
                            print(m)
                        # if peers[u] == m:
                        #     print(u)
                            vc=u
                            jh.append(vc)
                            print(",".join(set(jh)))
            jh1=jh[0]


            return render(request, 'tutors.html', context={"jh1":jh1})
    return render(request, 'Sales.html')


acceptable_subjects_middle_and_high=["Mathematics" , "Physics", "Chemistry", "Biology", "IT", "General English"]
def list_of_peers(request):
    pass
def sign_up_as_a_peer(request):

    if request.method == "POST":
        peer_grade=request.POST.get("your_grade")
        subject=request.POST.get("Subject")
        if int(peer_grade) > 12:
            raise Exception ("The maximum acceptable grade is 12")
        elif int(peer_grade) <7:
            raise Exception ("The minimum acceptable grade is 7")
        else:
            if str(subject) not in acceptable_subjects_middle_and_high:
                raise Exception ("The subject of your expertise is not among the supported subjects. We recommend"
                                 "contacting the coordinator for addressing your issue.")
            else:
                pass
    return render(request, 'sign_up_as_a_peer.html')
                    # index1 = l[index+3:].index("<")
                    # if l[index+3:][index1+1] == "/":
                    #     if l[index+3:][index1+2] == "h":
                    #         if l[index + 3:][index1 + 3] == "2":
                    #               print(l[index + 3:][:index1+3])
                    #               # z.append(l[index + 3:][:index1+3])
                    #               # if len(z) == 5:
                    #               #     break
                    #         if l[index + 3:][index1 + 3] != "2":
                    #             l[index + 3].remove(l[index1])
                    #     if l[index+3:][index1+2] != "h":
def criteria(request):
    return render(request, 'Criteria.html')
def donations(request):
    j=[]
    if request.method == 'POST':
            amount=request.POST.get('amount')
            currency=request.POST.get('currency')
            EUR = request.POST.get('EUR')
            currencies = ["USD", "IRR", "GBP"]
            print(amount)
            print(currency)
            print(EUR)
            if int(amount) < 0:
                raise Exception ("The entered value can't be negative.")
            if str(currency) in currencies or str(currency) in str(currencies).lower():
                if  str(currency) != currencies[1] or  str(currency) != currencies[1].lower():
                    return redirect(foreign_currencies)



    return render(request, 'donations.html' , context={"j":"".join(j)})
def partners(request):
    return render(request, 'our partners.html')
def foreign_currencies(request):

    if request.method == 'POST':
        method=request.POST.get('Card_Number')
        country = request.POST.get('Country')
        not_accepted_countries=["Turkey", "Iran","Syria"]
        if len(str(method)) != 16:
            raise Exception ("")
        if str(country) in not_accepted_countries or str(country) in str(not_accepted_countries).lower() or str(country) in str(not_accepted_countries).upper() :
            raise Exception("")
    return render(request, 'foreign_currencies.html')


@tool
def search():
    """it uses the search engine 'google' to find information about the Pahlavi Dynasty(in Pahlavi supporters' perspectives)
    """
    resp = requests.get(
        f"https://www.google.com/search?q=")
    print(resp.text)
    # print(resp.text[:500])  # first 500 chars for debugging
    soup = BeautifulSoup(resp.text, "html.parser")
    print(soup)

def AI_page(request):
  l = []
  vo={}
  if request.method == 'POST':
        bv={}
        user = request.POST.get('user')
        language=request.POST.get('language')

        @tool
        def search():
            """it uses the search engine 'google' to find information about the Pahlavi Dynasty(in Pahlavi supporters' perspectives)
               """
            resp = requests.get(
                f"https://www.google.com/search?q={str(user)}")
            print(resp.text)
            # print(resp.text[:500])  # first 500 chars for debugging
            soup = BeautifulSoup(resp.text, "html.parser")
            print(soup)
        llm = ChatOpenAI(
                api_key=os.getenv("OPENAI_KEY"),
                base_url="https://api.gapgpt.app/v1",
                model="gpt-4o-mini",
        )
        agent = create_agent(
            model=llm,
            system_prompt=f"""
                           You are an AI assistant that is responsible for addressing School students
                           problems and issues. We are running an academy called Arash which 
                           has this helpful purpose of connecting 
                           students to their peers.
                           In this academy, there is criteria for getting hired as a peer which can
                           be viewed on http://127.0.0.1:8000/criteria. Students can find 
                           themselves their suitable peers on http://127.0.0.1:8000/FindAPeer. 
                           Additionally, generous funds are also available on http://127.0.0.1:8000/funds .
                           You aren't supposed to help them by answering a question regarding
                           mathematics or any other subjects. Instead, you should help the users with getting 
                           connected with the suitable older student (peer) according to their weakness and need.
                           You could also help them with creating a non-perfect study plan.
                           Make sure to remember the older
                           messages {vo} and answer according to them unless the user doesn't want to.
                           answer in {str(language)}.
                           """,
            tools=[search]
        )
        result = agent.invoke(input={"role": "user", "messages": str(
            user)})
        lk=[]
        for i in str(result):
            lk.append(i)
        print(lk)
        for i in range(len(lk)):
          if "\\" in lk:
            ind = lk.index("\\")
            print(lk[ind])
            if lk[ind + 1] == "n":
                lk[ind + 1] = "<br>"
                lk.remove(lk[ind])
            elif lk[ind+1] != "n":
                    lk.remove(lk[ind])
        c = 0
        c += 1
        if c == 3:
            return HttpResponse("Dear user, your limit has reached. Please upgrade for more usage.")
        print(lk)
        cx2="".join(lk)
        fg1=cx2.find("AIMessage")
        fg=cx2[fg1:].find("additional_kwargs")
        cx14="".join(lk)[fg1:][:fg]
        d=cx14.find("=")
        cx1 = "".join(lk)[fg1:][:fg][d:]
        vo[str(user)] = str(cx1)[d:]
        return render(request, 'University_systems.html', context={"cx1": cx1, "vo":vo})
         # jh="".join(lk).find("AIMessage")
         # return HttpResponse(lk[jh:])


        # return HttpResponse(str("".join(lk)))

        # if "tool_call_id" in str(result["messages"]):
        #         f=str(result["messages"]).find("tool_call_id")
        #         print(f)
        #         print(str(result["messages"])[f:])
        #
        #         c=str(result["messages"])[f:]
        #     # v=str(result["messages"]).replace(str(result["messages"])[f],"")
        #     #     d=c.find("AIMessage")
        #         ds=c.find("content")
        #         print(str(c)[ds+8:])
        #         # v=d[ds:].find("content")
        #         for i in str(c)[ds:]:
        #             l.append(i)
        #         print(l)
        #         for t in range(len(l)):
        #          if "\\" in l:
        #             index=l.index("\\")
        #             # print(index)
        #             if l[index+1] == "n":
        #                 l[index] = "<br>"
        #                 l[index+1]=''
        #                 # print("".join(l))
        #             elif  l[index+1] != "n":
        #                 l.remove(l[index])
        #         # print("".join(l),str(result["messages"])[f:])
        #         v = "".join(l).find("additional_kwargs={'refusal': None")
        #         cx="".join(l)[:v]
        #         # print("".join(l)[:v])
        #         print(cx)
        #         context={'cx':cx}
        #         print(context["cx"])
        #         cx=context["cx"].find("content")
        #         xz=str(context["cx"])[cx:]
        #         print(str(context["cx"])[cx:])
        #         return render(request, 'University_systems.html',context={"xz":xz})
        # else:
        #         p=str(result["messages"])
        #         ai=p.find("AIMessage")
        #         v=p[ai:].find("content")
        #         x1=p[v:].find("additional_kwargs={'refusal'")
        #         x=p[v:x1]
        #         l1=[]
        #         # for i in x:
        #         #     l1.append(i)
        #         # print(l1)
        #         # for ty in range(len(l1)):
        #         #   if "\\" in l1:
        #         #     index=l1.index("\\")
        #         #     if l1[index+1] == "n":
        #         #         l1[index+1] = "<br>"
        #         #         l1.remove(l1[index])
        #         #     elif l1[index+1] != "n":
        #         #         l1.remove(l1[index])
        #         # print(l1)
        #         cx1="".join(l1)
        #         print(cx1)
        #         # tr=str(cx1).find("c")
        #         # cx2=str(cx1)[tr+8:]
        #         # print(cx2)
        #         # r=str(cx2).find("content")
        #         # cx=cx2[r:]
        #         # vo[str(user)]=str(cx)
        #         # print(vo)
        #         # bv[user]=str(cx)

  return render(request, 'University_systems.html')
