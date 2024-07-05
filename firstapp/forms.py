from django import forms
from django.contrib.auth.models import User
from .models import Products
import re
class Signup(forms.ModelForm):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)
    email=forms.CharField(max_length=30)
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    def clean(self):
        prod = Products.objects.all()
        list = []
        for i in prod:
            list.append(i.user)
        total_data=super().clean()
        username1=total_data['username']
        password1=total_data['password']
        email1=total_data['email']
        first_name1=total_data['first_name']
        last_name1=total_data['last_name']
        p1=re.fullmatch(r'[A-Za-z0-9]+',str(username1))
        p2=re.fullmatch(r'[a-zA-Z0-9]+',str(password1))
        p3=re.fullmatch(r'[a-zA-Z0-9]+@[a-z]+\.[a-z]{2,3}',str(email1))
        p4=re.fullmatch(r'[a-zA-Z]+',str(first_name1))
        p5=re.fullmatch(r'[a-zA-Z]+',str(last_name1))
        if username1 in list:
            raise forms.ValidationError('Username already exists try another name')
        if not p1:
            raise forms.ValidationError('No special characters in username')
        if not p2:
            raise forms.ValidationError('No special characters in Password')
        if not p3:
            raise forms.ValidationError('email address should be proper, with no special characters')
        if not p4:
            raise forms.ValidationError('enter proper firstname, with no special characters and numbers')
        if not p5:
            raise forms.ValidationError('enter proper lastname, with no special characters and numbers')
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']