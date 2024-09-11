from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def story(request):
    return render(request, 'story.html')

def contact(request):
    return render(request, 'contact.html')
