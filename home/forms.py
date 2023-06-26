from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email','password1','password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        # self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 100 characters or fewer. Letters, digits and @/./+/_ only.</small></span>'


        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        # self.fields['password1'].help_text = '<ul class="form-text text-muted"><small>Your password can\'t be too similar to your other things.</small></span>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''


class AddStocksForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title','image','price','quantity','description','category','total_price')

        labels = {
            'title':'Product Name:',
            'image': 'Product Image:',
            'price': 'Price:',
            'quantity': 'Quantity:',
            'description': 'Description:',
            'total_price':'Total Price:',
            'category':'Category:',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Product Name'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Description of Products'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'total_price': forms.HiddenInput(),
        }