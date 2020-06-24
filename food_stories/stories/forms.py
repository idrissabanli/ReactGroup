from django import forms
from stories.models import Contact

class ContactForm(forms.ModelForm):
    # website = forms.CharField()
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'user_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message'
            }),
        }


class LoginForm(forms.Form):
    username = forms.CharField(label="Istifadeci adi", help_text="Bura istifadeci adi yazilmalidir", required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Write your username'
    }))
    password = forms.CharField(label="Sifre", required=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Write your password'
    }))
    # class Meta:
        