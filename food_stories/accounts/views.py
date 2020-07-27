from django.shortcuts import render
from accounts.forms import RegisterForm, LoginForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from accounts.tasks import send_confirmation_email, account_activation_token
from django.contrib.auth import get_user_model
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django import forms
from django.contrib.auth.views import LoginView


User = get_user_model()


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'sign_in.html'


# def login(request):
#     if request.method == 'GET':
#         form = LoginForm()
#     else:
#         user_data = request.POST
#         form = LoginForm(user_data)
#         if form.is_valid():
#             user = authenticate(request, **form.cleaned_data)
#             if user:
#                 auth_login(request, user)
#                 return redirect('/')
#             else:
#                 messages.error(request, 'Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive.')
#     context = {
#         'form': form,
#     }
#     return render(request, 'sign_in.html', context)


# def logout(request):
#     auth_logout(request)
#     return redirect('/')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print('form validdir')
            user = form.save()
            user.set_password(form.cleaned_data.get('password'))
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            send_confirmation_email(current_site, user.id)
            messages.success(request, 'User created, please go to your mail and activate your account' )
            return redirect('/')
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'User activated PLease login' )
        return redirect('/')
    else:
        messages.error(request, 'User not activated' )
        return redirect('/')

