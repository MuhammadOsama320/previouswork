from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Contact


# Create your views here.
def index(request):
    context = {
        "variable": "this is sent",
        "variable2": "this ali"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page")


def about(request):
    return HttpResponse("This is about page")


def service(request):
    return HttpResponse("This is service  page")


def contact(request):

    if request.method == "POST":
        import pdb; pdb.set_trace()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        des = request.POST.get('des')
        date = request.POST.get('date')
        contact = Contact(name=name, email=email, phone=phone, des=des, date=datetime.today())
        contact.save()

    return render(request, 'contact.html', {})

    # return HttpResponse("This is Contact page")
