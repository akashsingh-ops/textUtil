# this file created by me
from django.http import HttpResponse
from django.shortcuts import render
# view return the hhttpresponse , 
# def index(request):
#     return  HttpResponse("hello Akash!")
# def about(request):
#     return  HttpResponse("<h1>hello Im Akash, learning django!</h1> <a href='https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7'>Email</a>")

# ---------pipeline
def index(request):
    # return  HttpResponse("Home!")
    # params={'name':"akash"}
    return render(request,'index.html')

# def ex1(request):
#    s='''<h2>NaviagtionBar <br></h2>
#    <a href="https://www.youtube.com/watch?v=lcpqpxVowU0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=12">Youtube</a><br>

#    <a href="google.com">Google</a> <br>
#    <a href="facebook.com">Facebook</a><br>
#    <a href="instagram.com">Instagram</a><br>
#    <a href="flipkart.com">Flipkart</a><br>

#    '''
#    return HttpResponse(s)
   
def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    removepunc=request.POST.get('removePunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlinerremover','off')
    extraspaceremover=request.POST.get('extraspaceremove','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n":
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    
    if (removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!='on'):
        return HttpResponse("Please select any operation adn try again!!")
    return render(request, 'analyzer.html', params)
    # return HttpResponse("remove punc")
# def capitalFirst(request):
#     return HttpResponse("capital first")
# def newLinerreomveFirst(request):
#     return HttpResponse("newLinerreomveFirst first")
# def spaceremove(request):
#     return HttpResponse("spaceremove ")
# def charcount(request):
#     return HttpResponse("charcount")