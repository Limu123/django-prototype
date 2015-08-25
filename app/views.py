from django.shortcuts import render

# Create your views here.

def app_list(request):
    return render(request, 'app_list.html', {})