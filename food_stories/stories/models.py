import math
from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()

# class Author(models.Model):
#     full_name = models.CharField('Tam Adı', max_length=60)
#     description = models.TextField()
#     image = models.ImageField(upload_to="media/authors/")

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = 'Müəllif'
#         verbose_name_plural = 'Müəlliflər'
    
#     def __str__(self):
#         return self.full_name


class Tag(models.Model):
    title = models.CharField('Title', max_length=20)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField('Title', max_length=50)
    image = models.ImageField('Şəkil', upload_to="categories/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'

    def __str__(self):
        return self.title


class Recipe(models.Model):
    # relations
    tags = models.ManyToManyField(Tag, related_name='recipes')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #information
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='recipes/')
    short_description = models.TextField(max_length=1000, help_text="bu reseptler siyahisinda cixacaq metindir")
    long_description = RichTextField(null=True, blank=True)
    min_read_time = models.PositiveIntegerField("Min read time", editable=False)

    # moderation
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "recipes"
        verbose_name = "Resept"
        verbose_name_plural = "Reseptlər"
        ordering = 'created_at',

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        length_long_desc = len(self.long_description.split(' '))
        min_read_sec = length_long_desc/2
        self.min_read_time = math.ceil(min_read_sec/60)
        super().save(*args, **kwargs)


class Story(models.Model):
    tags = models.ManyToManyField(Tag, related_name='stories')

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='recipes/')
    long_description = RichTextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    min_read_time = models.PositiveIntegerField("Min read time", editable=False, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # db_table = "stories"
        verbose_name = "Hekaye"
        verbose_name_plural = "Hekayeler"
        ordering = 'created_at',

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        length_long_desc = len(self.long_description.split(' '))
        min_read_sec = length_long_desc/2
        self.min_read_time = math.ceil(min_read_sec/60)
        super().save(*args, **kwargs)


class Contact(models.Model):
    user_name = models.CharField('User name', max_length=50)
    user_email = models.EmailField('User email', max_length=50)
    subject = models.CharField('Subject', max_length=255)
    message = models.TextField('Message')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
    
    def __str__(self):
        return self.user_name


class About(models.Model):
    title = models.CharField('Title', max_length=50)
    phone_number = models.CharField('Phone Number', max_length=20)
    location = models.CharField('Location', max_length=50)
    email = models.EmailField('Email', max_length=30)
    description = models.TextField('Description')
    daily_visitors = models.PositiveIntegerField('Daile Visitors',)
    facebook_page_url = models.URLField('Facebook page url')
    instagram_page_url = models.URLField('Instagram page url')
    twitter_page_url = models.URLField('Twitter page url')

    class Meta:
        verbose_name = 'About Site Information'
        verbose_name_plural = 'About Site Informations'
    
    def __str__(self):
        return self.title

    
class Subscriber(models.Model):
    #informations
    email = models.EmailField('Email', max_length=30, unique=True)

    # moderations
    is_active = models.BooleanField('is_active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"
    
    def __str__(self):
        return self.email