from django.http import HttpResponse
from django.shortcuts import render
import math

def homepage(request):
    return render(request, "home.html")

def evenodd(request):
    context= {}
    value=""
    #n1=None
    try:
        if request.method == 'POST':
            n1=request.POST.get('number', {})
            if n1 and n1.isdigit():
                n1=int(n1)
                if n1 % 2 == 0:
                    value=f"{n1} is even"
                else:
                    value=f"{n1} is odd."
            else:
                value = "Please enter digits."

        context={'result': value, 'n1':n1}
    except:
        pass
    return render(request, "evenodd.html", context)

def palindrome(request):
    context={}
    answer=""
    text=""
    if request.method == "POST":
        text = request.POST.get("word", {})
        text=text.lower()
        if text == text[::-1]:
            answer=f"{text} is palindrome"
        else:
            answer=f"{text} is not a palindrome"
    context = {'result': answer, 'text':text}
    return render(request, "palindrome.html", context)

def primecomposite(request):
    ans=""
    num1=None
    if request.method == "POST":
        num1 = int(request.POST.get("number", ''))
        if num1 < 2:
            ans = f"{num1} is neither prime nor composite!"
        else:
            for i in range(2, int(num1 ** 0.5) + 1):
                if num1 % i == 0:
                    ans = f"{num1} is Composite."
                    break
            else:
                ans = f"{num1} is Prime."

    return render(request, "primeComp.html", {'result': ans, 'num1': num1})