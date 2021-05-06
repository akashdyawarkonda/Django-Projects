from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def login_form(request):
    form = forms.FormPage()
    #print(form)
    if request.method == 'POST':
        form = forms.FormPage(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['password'])
    return render(request, 'login_app/login.html', {'form':form})
