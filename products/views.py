from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add(request):
    return render(request, 'add.html')

def edit(request):
    return render(request, 'edit.html')

def delete(request):
    pass
