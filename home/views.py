from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.

# def index(request):
    # return HttpResponse("This is a homepage")

# def home(request):
#     return HttpResponse("i am homepage who are you")


# def home(request):
#     return render(request, '/')
def home(request):

    return render(request, 'index.html')

def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name,email,phone,content)
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
        messages.success(request, 'Your message has been sent')

        


    return render(request, 'contact.html')


def services(request):
    
    return render(request, 'services.html')