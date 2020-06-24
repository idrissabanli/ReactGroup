from django.shortcuts import render, redirect
from datetime import date
from stories.models import Recipe
from stories.forms import ContactForm, LoginForm
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def test(request):
    message = 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ea illo aliquam cumque, eum animi repudiandae nostrum optio quisquam, distinctio magni, impedit reiciendis similique ab! Reiciendis atque reprehenderit asperiores debitis laboriosam.'
    html_context = "<h1> Salam Dunya</h1>"
    new_date = date(2018, 3, 1)
    a = [1,2,3,4,5,6]
    context = {
        'pi': 3.1457,
        'msg': message,
        'new_date': new_date,
        'html_context': html_context,
        'a': a,
    }
    return render(request, 'test.html', context)


def recipes(request):
    recipe_list = Recipe.objects.all() # [{title:"sdjf", "image": "/sjhd/skjdf/p.png"}]
    context = {
        'recipes': recipe_list
    }
    return render(request, 'recipes.html', context)

def recipe_detail(request):
    return render(request, 'single.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            print('ok-dir')
            form.save()
            messages.success(request, 'Mesajiniz Ugurla gonderildi!')
            return redirect('/')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)

def login(request):
    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)