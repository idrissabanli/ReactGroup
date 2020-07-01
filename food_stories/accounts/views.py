from django.shortcuts import render
from accounts.forms import RegisterForm
from django.shortcuts import redirect
from django.contrib import messages

def register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print('form validdir')
            form.save()
            messages.success(request, 'User created' )
            return redirect('/')
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)
