from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, TemplateView, \
    UpdateView, DeleteView
from datetime import date
from stories.models import Recipe, Story, Category
from stories.forms import ContactForm, SubscriberForm, StoryForm, RecipeForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



# def home(request):
#     return render(request, 'index.html')

class Home(TemplateView):
    template_name = 'index.html'

# def about(request):
#     return render(request, 'about.html')


class AboutView(TemplateView):
    template_name = 'about.html'


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


# def recipes(request):
#     recipe_list = Recipe.objects.all()
#     context = {
#         'recipes': recipe_list
#     }
#     return render(request, 'recipes.html', context)


class RecipeList(ListView):
    model = Recipe
    template_name = 'recipes.html'
    context_object_name = 'recipes'
    paginate_by = 2


class StoryList(ListView):
    model = Story
    template_name = 'stories.html'
    # context_object_name = 'recipes'
    paginate_by = 2


class RecipeDetail(DetailView):
    model = Recipe
    template_name = 'single.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context

from stories.tasks import dump_database
from django.http import HttpResponse

def dump(request):
    dump_database.delay()
    return HttpResponse('Database dump olunur!')


class SubscribeView(CreateView):
    form_class = SubscriberForm
    success_url = reverse_lazy('home')
    http_method_names = ('post',)

    def form_valid(self, *args, **kwargs):
        messages.success(self.request, 'Ugurla subscribe oldunuz her gun bilgilendirileceksiniz!')
        return super().form_valid(*args, **kwargs)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Dogru email daxil edin!')
        return redirect(reverse_lazy('home'))


class UserProfile(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'user-profile.html'


    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        return queryset.filter(author=user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['story_list'] = Story.objects.filter(author=self.request.user)
        return context




class CreateStory(LoginRequiredMixin, CreateView):
    form_class = StoryForm
    template_name = 'create_blog.html'
    success_url = '/'

    def form_valid(self, form):
        story = form.save(commit=False)
        story.author = self.request.user
        story.save()
        return super().form_valid(form)


class CreateRecipe(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    template_name = 'create_blog.html'

    def form_valid(self, form):
        story = form.save(commit=False)
        story.author = self.request.user
        story.save()
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'create_blog.html'


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('user-profile')


    # def form_valid(self, form):
    #     story = form.save(commit=False)
    #     story.author = self.request.user
    #     story.save()
    #     return super().form_valid(form)





# def recipe_detail(request):
#     return render(request, 'single.html')

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(data=request.POST)
#         if form.is_valid():
#             print('ok-dir')
#             form.save()
#             messages.success(request, 'Mesajiniz Ugurla gonderildi!')
#             return redirect('/')
#     else:
#         form = ContactForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'contact.html', context)

class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/'

    def form_valid(self, *args, **kwargs):
        messages.success(self.request, 'Mesajiniz Ugurla gonderildi!')
        return super().form_valid(*args, **kwargs)




# def login(request):
#     form = LoginForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'login.html', context)