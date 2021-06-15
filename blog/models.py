from django.db import models
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    status= models.BooleanField(default=True,verbose_name="Visible")
    position= models.IntegerField(default=0)

    class Meta:
        verbose_name_plural="Categories"
        ordering=['position']
        
    def __str__(self):
         return self.title
    
class Article(models.Model):
    STATUS_CHOICES=(
        ('d','Draft'),
        ('p','Published')
    )
    category=models.ManyToManyField(Category)
    author=models.CharField(max_length=50,default='admin')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField()
    thumbnail=models.ImageField(upload_to="images")
    publish= models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    status= models.CharField(max_length=1,choices=STATUS_CHOICES)


    def __str__(self):
        return self.title