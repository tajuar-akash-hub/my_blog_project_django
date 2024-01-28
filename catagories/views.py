from django.shortcuts import render,redirect
from . forms import catagoryForm

# Create your views here.
def add_catagory(request):
    if request.method == "POST":
        category_form = catagoryForm(request.POST)
        if  category_form.is_valid():
            category_form.save()
            return redirect("add_catagory")
    else : 
        category_form = catagoryForm()
    return render(request,"./add_category.html",{'category_form':category_form})




    

