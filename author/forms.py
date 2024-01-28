from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class Registration_form(UserCreationForm):
    # firstname = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    # lastname = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    class Meta :
        model = User
        fields = ['username','first_name','last_name','email']


# if user wants to change his/her data
class changeUserData(UserChangeForm):
    password= None
    class Meta :
        password= None
        model = User
        # fields = ['username','first_name','last_name','email']
        fields = ['username','first_name','last_name','email']


   