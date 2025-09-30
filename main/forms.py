from django import forms
from django.forms import ModelForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'category',
                  'description', 'thumbnail', 'is_featured']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        text_input_class = 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm'

        self.fields['name'].widget.attrs.update(
            {'class': text_input_class, 'placeholder': 'e.g., Slime Ball Keychain'})
        self.fields['price'].widget.attrs.update(
            {'class': text_input_class, 'placeholder': 'e.g., 50000'})
        self.fields['stock'].widget.attrs.update(
            {'class': text_input_class, 'placeholder': 'e.g., 100'})
        self.fields['category'].widget.attrs.update(
            {'class': text_input_class, 'placeholder': 'e.g., Accessories'})
        self.fields['thumbnail'].widget.attrs.update(
            {'class': text_input_class, 'placeholder': 'https://example.com/image.jpg'})

        self.fields['description'].widget.attrs.update(
            {'class': text_input_class, 'rows': 4, 'placeholder': 'Describe your product here...'})

        self.fields['is_featured'].widget.attrs.update(
            {'class': 'h-4 w-4 text-emerald-600 border-gray-300 rounded focus:ring-emerald-500'})


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm',
                'placeholder': 'Enter your username'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm',
                'placeholder': 'Enter your password'
            }
        )
    )


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        tailwind_class = 'appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm'

        for fieldname, field in self.fields.items():
            field.widget.attrs.update({'class': tailwind_class})

            if fieldname == 'username':
                field.widget.attrs.update(
                    {'placeholder': 'Choose a unique username'})
            elif fieldname == 'password1':
                field.widget.attrs.update(
                    {'placeholder': 'Enter a strong password'})
                field.label = "Password"
            elif fieldname == 'password2':
                field.widget.attrs.update(
                    {'placeholder': 'Confirm your password'})
                field.label = "Password confirmation"
