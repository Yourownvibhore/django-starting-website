from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # print(request.GET.get('text','default')),
    return render(request, 'index.html')
    # return HttpResponse("hello")


def about(request):
    return render(request, 'about.html')


def email(request):
    return render(request, 'email.html')


def phone(request):
    return render(request, 'ph.html')


def analyse(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    captialize = request.POST.get('captialize', 'off')
    charcount = request.POST.get('charcount', 'off')
    # print(removepunc)
    # print(djtext)
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed+char
        param = {'purpose': "removed punctuations", 'analysed_text': analysed}
        djtext = analysed
        # return render(request,'analyse.html',param)
    if captialize == "on":
        analysed = djtext.upper()
        # for char in djtext:
        #     analysed=analysed + char.upper()
        param = {'purpose': "Upper case", 'analysed_text': analysed}
        djtext = analysed
        # return render(request,'analyse.html',param)
    if charcount == "on":
        count = 0
        for i in djtext:
            if not (i == " "):
                count = count+1
        param = {'purpose': "Upper case", 'analysed_text': str(count)}

        return render(request, 'analyse.html', param)

    return render(request, 'analyse.html', param)
