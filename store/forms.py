from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','username', 'email', 'password1', 'password2']

    first_name = forms.CharField(label='Nombre', required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'type': 'text',
                                                                'placeholder': 'Name',
                                                                'id':'name',
                                                                'data-sb-validations':'required'}))
   

    username = forms.CharField(label='Nombre de usuario', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 
                                                             'type': 'text',
                                                             'placeholder': 'Username',
                                                             'id':'username',
                                                             'data-sb-validations':'required'}))
    
    email = forms.EmailField(label='Email', required=True,
                               widget=forms.EmailInput(attrs={'class': 'form-control', 
                                                             'type': 'email',
                                                             'placeholder': 'Email',
                                                             'id':'email',
                                                             'data-sb-validations':'required,email',
                                                             
                                                         
                                                             }))
    
    password1 = forms.CharField(label='Password', required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 
                                                             'type': 'password',
                                                             'placeholder': 'Password',
                                                             'id':'password',
                                                             'data-sb-validations':'required',
                                                         
                                                             }))
    
    password2 = forms.CharField(label='Confirm password', required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 
                                                             'type': 'password',
                                                             'placeholder': 'Confirm Password',
                                                             'id':'confirmPassword',
                                                             'data-sb-validations':'required',
                                                         
                                                             }))
    



class UserLoginForm(AuthenticationForm):


    class Meta:
        model = User
        fields = [ 'username', 'password']

    username = forms.CharField(label='Nombre de usuario', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 
                                                             'type': 'text',
                                                             'placeholder': 'Username',
                                                             'id':'username',
                                                             'data-sb-validations':'required'}))
            
                                                             
                                                             
                                                
    
    password = forms.CharField(label='Password', required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 
                                                             'type': 'password',
                                                             'placeholder': 'Password',
                                                             'id':'password',
                                                             'data-sb-validations':'required',
                                                         
                                                             }))
    


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'



    username = forms.CharField(label='Nombre de usuario', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 
                                                             'type': 'text',
                                                             'placeholder': 'Username',
                                                             'id':'username',
                                                             'data-sb-validations':'required'}))

    email = forms.EmailField(label='Email', required=True,
                               widget=forms.EmailInput(attrs={'class': 'form-control', 
                                                             'type': 'email',
                                                             'placeholder': 'Email',
                                                             'id':'email',
                                                             'data-sb-validations':'required,email',
                                                             
                                                         
                                                             }))
   
    name = forms.CharField(label='Nombre personal', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 
                                                             'type': 'text',
                                                             'placeholder': 'Username',
                                                             'id':'username',
                                                             'data-sb-validations':'required'}))
    password = forms.CharField(label='Password', required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 
                                                             'type': 'password',
                                                             'placeholder': 'Password',
                                                             'id':'password',
                                                             'data-sb-validations':'required',
                                                         
                                                             }))