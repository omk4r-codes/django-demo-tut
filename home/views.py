from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("Hi this is Home page!")
    # var1 = "Omkar"
    # not working as context must be a dict rather than str. SO:
    context = {
        "var1" : "Omkar",
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    confirmation = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save()
        confirmation = "Thanks for contacting, we'll get in touch with you soon!"
    context = {
        "confirmation" : confirmation,
    }
    return render(request, 'contact.html', context)


def services(request):
    return render(request, 'services.html')

def add_form(request):
    res = None
    if request.method == "GET":
        num1 = request.GET.get('num1', 0)
        num2 = request.GET.get('num2', 0)
        try:
            res = int(num1) + int(num2)
        except ValueError:
            res = "Invalid Numbers!"
    context = {
        "result" : res, 
    }
    return render(request, 'add_form.html', context)
    