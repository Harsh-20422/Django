# i have created this file Dhruv
from django.http import HttpResponse
from django.shortcuts import render
import re


def index(request):
    params = {"name": "Dhruv", "age": "18", "place": "Udaipur"}
    return render(request, 'index.html', params)
    # return HttpResponse('<marquee>Dhruv</marquee>')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def analyse(request):
    # Getting values from template
    djtext = request.POST.get("text", "None!")
    removepunc = request.POST.get("removepunc", "off")
    isCapitalise = request.POST.get("fullcaps", "off")
    isNewLine = request.POST.get("newline", "off")
    isExtraSpaceRemover = request.POST.get("extraspaceremover", "off")

    # Defining function
    if removepunc == "on":
        analysed_text = re.sub(r'[^\w\s]', '', djtext)
        params = {"purpose": "Remove punctuations", "analysed_text": analysed_text}
        djtext = analysed_text

    if isCapitalise == "on":
        analysed_text = djtext.upper()
        params = {"purpose": "Capitalise text", "analysed_text": analysed_text}
        djtext = analysed_text

    if isNewLine == "on":
        analysed_text = ""
        for char in djtext:
            if char == "\n" and char == "\r":
                analysed_text += " "
            else:
                analysed_text = analysed_text + char
        params = {"purpose": "New Line Remover", "analysed_text": analysed_text}
        djtext = analysed_text

    if isExtraSpaceRemover == "on":
        analysed_text = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analysed_text = analysed_text + char
        params = {"purpose": "Extra Space Remover", "analysed_text": analysed_text}
        djtext = analysed_text

    if removepunc != "on" and isCapitalise != "on" and isNewLine != "on" and isExtraSpaceRemover != "on":
        return HttpResponse("PLease select an operation")

    return render(request, "analyse.html", params)


def facebook(request):
    return HttpResponse('''<a href="http://127.0.0.1:8000/"> Back </a><hr>
                         <a href="https://www.facebook.com/" > Facebook </a>''')


def google(request):
    return HttpResponse('''<a href="http://127.0.0.1:8000/"> Back </a><hr>
    <a href="https://www.google.com" >Google</a>''')


def youtube(request):
    return HttpResponse('''<a href="http://127.0.0.1:8000/"> Back </a><hr>
    <a href="https://www.Youtube.com" >Youtube </a>''')


def twitter(request):
    return HttpResponse('''<a href="http://127.0.0.1:8000/"> Back </a><hr>
    <a href="https://www.Twitter.com" >Twitter</a>''')
