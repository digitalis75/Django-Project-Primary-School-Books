from django.db import models

SCHOOL_LEVEL_CHOICES = (
    ('Primary', 'Primary'),
    ('Secondary', 'Secondary'),
)

STAGE_CHOICES = (
    ('Junior_Infants', 'Junior Infants'),
    ('Senior_Infants', 'Senior Infants'),
    ('First_Class', 'First Class'),
    ('Second_Class', 'Second Class'),
    ('Third_Class', 'Third Class'),
    ('Fourth_Class', 'Fourth Class'),
    ('Fifth_Class', 'Fifth Class'),
    ('Sixth_Class', 'Sixth Class'),
)

SUBJECT_CHOICES = (
    ('English', 'English'),
    ('Irish', 'Irish'),
    ('Maths', 'Maths'),
    ('Science', 'Science'),
    ('SESE', 'SESE'),
    ('Science/SESE', 'Science/SESE'),
    ('Geograghy', 'Geograghy'),
    ('History', 'History'),
)

COVER_FORMAT_CHOICES = (
    ('Softback', 'Softback'),
    ('Hardback', 'Hardback'),
)

STATUS_CHOICES = (
    ('In Stock', 'In Stock'),
    ('Temporary Out of Stock', 'Temporary Out of Stock'),
)


# Create your models here
class Product(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False,
                            default='')
    author = models.CharField(max_length=254, default='')
    school_level = models.CharField(max_length=40,
                                    choices=SCHOOL_LEVEL_CHOICES, default='')
    stage = models.CharField(max_length=40, choices=STAGE_CHOICES, default='')
    subject = models.CharField(max_length=40, choices=SUBJECT_CHOICES, default='')
    publisher = models.CharField(max_length=50, default='')
    product = models.CharField(max_length=20, default='')
    cover_format = models.CharField(max_length=20,
                                    choices=COVER_FORMAT_CHOICES, default='')
    language = models.CharField(max_length=40, default='')
    pages = models.IntegerField()
    publication_year = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=False, blank=False, default='', unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    status = models.CharField(max_length=40, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('name', 'slug')

    def __str__(self):
        return self.name
