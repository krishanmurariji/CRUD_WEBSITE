from django.db import models
import uuid
# Create your models here.
class BaseMOdel(models.Model):
    uid = models.UUIDField(primary_key= True, editable=False, default = uuid.uuid4()) 
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now_add = True)
    
    class Meta:
        abstract = True

class student(BaseMOdel):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254, unique=True)
    def __str__(self):
        return self.name
