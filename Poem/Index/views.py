from django.shortcuts import render,HttpResponse
import json

# Create your views here.

def main_views(request):

    return render(request,"main.html")
    # return HttpResponse("1111")

def show_views(request):

    word=request.GET.get("word","word")
    dict = {"word": word}
    strjson=json.dumps(dict)
    return HttpResponse(strjson)