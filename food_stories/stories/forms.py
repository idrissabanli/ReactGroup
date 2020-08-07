from django import forms
from stories.models import Contact, Recipe, Subscriber, Story, Tag, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

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


class RecipeForm(forms.ModelForm):
    long_description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Recipe
        fields = '__all__'


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address',
            }),
        }


class StoryForm(forms.ModelForm):
    long_description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Story
        fields = (
            'title',
            'image',
            'long_description',
            'tags',
            'category',
        )
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),
            'tags': forms.SelectMultiple(attrs={
                    'class': 'form-control',
                    'placeholder': 'Tags',
                }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Tags',
            }),
        }

class RecipeForm(forms.ModelForm):
    long_description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Recipe
        fields = (
            'title',
            'image',
            'short_description',
            'long_description',
            'tags',
            'category',
        )

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write short description',
            }),
            'tags': forms.SelectMultiple(attrs={
                    'class': 'form-control',
                    'placeholder': 'Tags',
                }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Tags',
            }),
        }



# class LoginForm(forms.Form):
#     username = forms.CharField(label="Istifadeci adi", help_text="Bura istifadeci adi yazilmalidir", required=False, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Write your username'
#     }))
#     password = forms.CharField(label="Sifre", required=False, widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Write your password'
#     }))
#     # class Meta:


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'comment_msg',
            'parent_comment',
        )
        widgets = {
            'comment_msg': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'parent_comment': forms.HiddenInput()
        }