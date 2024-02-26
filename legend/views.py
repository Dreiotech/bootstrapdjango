from django.shortcuts import render

def index(request):
    return render(request,template_name='index.html')
def contact(request):
    return render(request,template_name='contact.html')
def why(request):
    return render(request,template_name='why.html')
def trainer(request):
    return render(request,template_name='trainer.html')
# Create your views here.
