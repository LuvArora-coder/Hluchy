from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def audiotogesture(request):
    return render(request,'audio_to_image.html')
