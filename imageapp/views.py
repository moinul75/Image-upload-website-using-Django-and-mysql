from django.shortcuts import render,HttpResponse
from django.contrib import admin
from .forms import FormImage
from .models import Image


#change the admin panel Name 
admin.site.site_header = "My Image App"
admin.site.site_title = "My Image"
admin.site.index_title = "Welcome to My Image App"



# Create your views here.
def home(request):
    #save the input image
    if request.method == 'POST':
        form = FormImage(request.POST, request.FILES)
        #check if its all valid or not 
        if form.is_valid():
            form.save()
    form = FormImage()
    #pass the save image in the ui 
    image = Image.objects.all()
    return render(request,'index.html',context={'form':form,'image':image})



