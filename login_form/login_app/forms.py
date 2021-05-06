from django import forms
from django.core import validators
from .models import login_table



### This is the code for form gernate and link to html
# def check_pass(password):
#
#     if len(password) < 8:
#         #print("password is of length",len(password))
#         raise forms.ValidationError("Your password is too weak.")
#     return password
#
# class FormPage(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(validators=[check_pass], widget=forms.PasswordInput)
###



## This is the code for form gernate and link to model and html FormPage

class FormPage(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = login_table
        fields = "__all__"
