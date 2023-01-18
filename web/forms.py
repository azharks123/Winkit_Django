from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from api.models import Posts,Userprofile

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["title","image"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-select"})
        }

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        fields=["profile_pic","timelinepic"]




