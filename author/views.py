from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render,redirect
from . forms import Registration_form,changeUserData
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView
from posts.models import post
from django.urls import reverse_lazy


# Create your views here.
def register(request):
    if request.method == "POST":
        register_Form = Registration_form(request.POST)
        if register_Form.is_valid():
            messages.success(request,"Account Created Successfully")
            register_Form.save()
            # print(author_Form.cleaned_data)  #printing in the terminal
            return redirect("user_login")
    else:
        register_Form = Registration_form()
    return render(request,'./register_form.html',{'form': register_Form,'type':'Register page'})

# handling login related work 
# def user_login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request,request.POST)
#         if form.is_valid():
#             user_name = form.cleaned_data['username']
#             user_pass = form.cleaned_data['password']
#             user = authenticate(username=user_name,password= user_pass)
#             if user is not None:
#                 messages.success(request,"Successfully logged in , welcome man")
#                 login(request,user)
#                 return redirect("profilepage")
#             else:
#                 messages.warning(request,"Create an Account First")
#                 return redirect("register")
#     else:
#         form = AuthenticationForm()
#     return render(request,'./register_form.html',{'form': form,'type':'login page'})

# user login using class based view 

class UserLoginView(LoginView):
    template_name='register_form.html'

    def form_valid(self, form):
        messages.success(self.request,"Logged in successfull")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,"Please Enter correct information")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['type']='Login'
        return context
    
    
    def get_success_url(self) -> str:
        return reverse_lazy("profilepage")
    
    
    



@login_required
def profile(request):
    data = post.objects.filter(author = request.user)
    
    return render(request,'./profile.html',{'data':data})

@login_required
def edit_profile(request):
    if request.method == "POST":
        profile_Form = changeUserData(request.POST,instance = request.user)
        if profile_Form.is_valid():
            messages.success(request,"Account updated Successfully")
            profile_Form.save()
            # print(author_Form.cleaned_data)  #printing in the terminal
            return redirect("profilepage")
    else:
        profile_Form = changeUserData(instance = request.user)
    return render(request,'./update_profile.html',{'form': profile_Form})

# user password change 
def pass_change(request):
    if request.method == "POST":
        pass_change_form = PasswordChangeForm(request.user,data=request.POST)
        if pass_change_form.is_valid():
            pass_change_form.save()
            messages.success(request,"Password Changed Successfully")
            update_session_auth_hash(request,pass_change_form.user)
            return redirect("profilepage")
    else:
        pass_change_form = PasswordChangeForm(user = request.user)
    return render(request,'./change_password.html',{'form': pass_change_form})

# user logout section
def user_logout(request):
    logout(request)
    return redirect("user_login")

# log out view as class based view





    



    

    

