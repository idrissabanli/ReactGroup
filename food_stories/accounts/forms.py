from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.password_validation import validate_password

USER_MODEL = get_user_model()

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
            }))

    class Meta:
        model = USER_MODEL
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'confirm_password',
        )

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),
            'username':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm password does not match"
            )
        return cleaned_data

    def clean_password(self):
        password = self.cleaned_data.get('password')
        print(self.instance)
        try:
            validate_password(password, self.instance)
        except forms.ValidationError as error:
            self.add_error('password', error)
        return password