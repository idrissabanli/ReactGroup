from django.db import models

class Author(models.Model):
    full_name = models.CharField('Tam Adı', max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to="media/authors/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Müəllif'
        verbose_name_plural = 'Müəlliflər'
    
    def __str__(self):
        return self.full_name


class Category(models.Model):
    title = models.CharField('Title', max_length=50)
    image = models.ImageField('Şəkil', upload_to="media/categories/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'

    def __str__(self):
        return self.title


class Recipe(models.Model):
    
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/recipes/')
    short_description = models.TextField(max_length=1000, help_text="bu reseptler siyahisinda cixacaq metindir")
    long_description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "recipes"
        verbose_name = "Resept"
        verbose_name_plural = "Reseptlər"
        ordering = 'created_at',

    def __str__(self):
        return f"title: {self.title}  category: {self.get_category_display()}"


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

