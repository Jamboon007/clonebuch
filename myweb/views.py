from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def story(request):
    response=requests.get('https://buchpawares.github.io/my_measure/measure.json').json()
    return render(request, 'story.html',{'response':response})

def contact(request):
    return render(request, 'contact.html')

def ppg(request):
    data = requests.get('https://buchpawares.github.io/my_measure/measure.json').json()
    result = None
    if request.method == 'POST':
        query = request.POST.get('na', '')
        filtered_data = [item for item in data if query.lower() in item['name'].lower()]

        if filtered_data:
            result = filtered_data[0]

    return render(request, 'story.html',{'result': result})