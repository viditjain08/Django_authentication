from django import forms
from main.models import Erpuser
import re
class loginform(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput)

class signupform(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    password1 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput)
    firstname= forms.CharField(max_length=20, required=True)
    lastname = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=30, required=True)
    bitsid = forms.CharField(max_length=12, required=True)

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def clean_bitsid(self):
        bitsid2 = self.cleaned_data['bitsid']
        temp = re.compile(r'^201([0-6])([ABH])(\d)PS(\d{3})P$')
        flag = temp.search(bitsid2)
        flag2 = Erpuser.objects.get(bitsid = bitsid2)
        if flag is None:
            raise forms.ValidationError("Invalid BitsID")
        if flag2 is not None:
            raise forms.ValidationError("BITS ID already registered")
        return bitsid

    def clean_username(self):
        username2 = self.cleaned_data['username']
        flag = Erpuser.objects.get(username = username2)
        if flag is not None:
            raise forms.ValidationError("Username exists")
        return username

    def clean_email(self):
        email2 = self.cleaned_data['email']
        flag = Erpuser.objects.get(email = email2)
        if flag is not None:
            raise forms.ValidationError("Email exists")
        return email
