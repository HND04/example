from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'render/index.html', {})

def data_view(request):
    return render(request, 'render/data.html',{})