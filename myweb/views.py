from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def story(request):
    #response=requests.get('https://buchpawares.github.io/my_measure/measure.json').json()
    #{'response':response}
    return render(request, 'story.html',)

def contact(request):
    return render(request, 'contact.html')