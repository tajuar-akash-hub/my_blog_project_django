from django.shortcuts import render
from posts.models import post
from catagories.models import Catagory

def home(request,catagory_slug=None):
    data = post.objects.all()
    if catagory_slug is not None:
        ctg= Catagory.objects.get(slug = catagory_slug) #reciving data from category 
        # print("printing category ",ctg)
        data = post.objects.filter(catagory = ctg)
    categories = Catagory.objects.all()
 
    return render(request,"./home.html",{'data':data,'category':categories})
