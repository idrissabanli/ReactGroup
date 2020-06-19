from django.db import models


class Author(models.Model):
    GENDER_CHOICES = (
        (1, 'Kişi'),
        (2, 'Qadın')
    )
    full_name = models.CharField('Tam Adı', max_length=255)
    image = models.ImageField('Şəkil', upload_to='author_images')
    gender = models.IntegerField('Cins', choices=GENDER_CHOICES)
    date_of_birthday = models.DateField('Doğum günü', null=True, blank=True)
    nationality = models.CharField('Milliyəti', max_length=50, null=True, blank=True)
    info = models.TextField('Haqqında Məlumat', null=True, blank=True )

    # moderation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Müəllif'
        verbose_name_plural = 'Müəlliflər'

    def __str__(self):
        return self.full_name


class Category(models.Model):
    # information
    title = models.CharField('Başlığı', max_length=50)

    # moderation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'

    def __str__(self):
        return self.title

# book = Book.objects.create(title="Book 1", description="knfkdsnf", price=12.5, page_count=50, cover_image='/home/idris/book.jpg',
class Book(models.Model):
    # relations
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='books')

    # information
    title = models.CharField('Başlığı', max_length=255)
    description = models.TextField('Məzmunu', )
    price = models.DecimalField('Qiyməti', max_digits=6, decimal_places=2)
    page_count = models.PositiveSmallIntegerField('Səhifə sayı', null=True, blank=True)
    cover_image = models.ImageField('Şəkil', upload_to='book_images')

    # moderation
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Kitab'
        verbose_name_plural = 'Kitablar'

    def __str__(self):
        return self.title

