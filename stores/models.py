from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Pizzeria(models.Model):        
    pizzeria_name = models.CharField(max_length=200, blank=False)        
    street = models.CharField(max_length=400, blank=True)        
    city = models.CharField(max_length=400, blank=True)        
    state =  models.CharField(max_length=2, null=True, blank=True)        
    zip_code = models.IntegerField(blank=True, default=0)        
    website = models.URLField(max_length=420, blank=True)         
    phone_number = models.CharField( validators=[RegexValidator(regex=r"""(\+212|0)([\-_/]*)(\d[\-_/]*){9}
""")],max_length=13, blank=True )        
    description = models.TextField(blank=True)         
    logo_image = models.ImageField( upload_to='pizzariaImages',  blank=True)        
    email = models.EmailField(max_length=245, blank=True)        
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.pizzeria_name