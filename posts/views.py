from django.shortcuts import render,redirect
from . import models
from . import forms
from . forms import PostForm

# Create your views here.
def add_post(request):
    if request.method == "POST":
        Post_form = PostForm(request.POST)
        if Post_form.is_valid():
            Post_form.instance.author= request.user
            Post_form.save()
            return redirect("homepage")
    else :
        Post_form = PostForm()
    return render(request,"./add_post.html",{'Post_form':Post_form}) 



# function for editing post
def edit_post(request,id):
    Post = models.post.objects.get(pk = id) #filtering primary key , which is default by djagno
    Post_form = forms.PostForm(instance=Post)
    
    if request.method == "POST":
        Post_form = PostForm(request.POST,instance=Post)
        if Post_form.is_valid():
            Post_form.save()
            return redirect("homepage")
    return render(request,"./add_post.html",{'Post_form':Post_form}) 

#fucntion for deleteing post 

def delete_post(request,id):
    Post= models.post.objects.get(pk=id)
    Post.delete()
    return redirect("homepage")

        
