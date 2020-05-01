from django.db import models

STATUS_CHOICES = (
    ('In Stock', 'In Stock'),
    ('Temporary Out of Stock', 'Temporary Out of Stock'),
)


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    author = models.CharField(max_length=254, default='')
    school_level = models.CharField(max_length=40, default='')
    stage = models.CharField(max_length=40, default='')
    subject = models.CharField(max_length=40, default='')
    publisher = models.CharField(max_length=50, default='')
    product = models.CharField(max_length=20, default='')
    cover_format = models.CharField(max_length=20, default='')
    language = models.CharField(max_length=40, default='')
    pages = models.IntegerField()
    publication_year = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    status = models.CharField(max_length=40, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
