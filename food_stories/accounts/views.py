from django.shortcuts import render
from accounts.forms import RegisterForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from accounts.tasks import send_confirmation_email, account_activation_token
from django.contrib.auth import get_user_model
from django.utils.encoding import force_text

User = get_user_model()

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