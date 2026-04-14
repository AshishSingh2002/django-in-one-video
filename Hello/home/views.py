from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

#from django.shortcuts import render, redirect, get_object_or_404
#from .models import Image

def index(request): 
    context = {
        'variable1':"Ashish is good person",
        'variable2':"rahul is good person"
    }
    
   # ye test k liye likha h   messages.success(request,"this is test message")
    return render(request, 'index.html',context)  
# return HttpResponse("this is about page")

# Yha check krna padega page kha redirect ho rha h about me ya phir ye home pr
"""
def about(request):
    images = Image.objects.all()
    return render(request, 'index.html', {'images': images})


def edit_image(request, id):
    image = get_object_or_404(Image, id=id)

    if request.method == "POST":

        # file upload
        if request.FILES.get('image'):
            image.image = request.FILES.get('image')

        # url paste
        if request.POST.get('image_url'):
            image.image_url = request.POST.get('image_url')

        image.save()
        return redirect('/about/')

    return render(request, 'edit.html', {'image': image})


"""

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is services page")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            desc=desc,
            date=datetime.today()
        )

    messages.success(request, "Your message has been sent!.")
    return render(request, 'contact.html')
    #return HttpResponse("this is contact page")