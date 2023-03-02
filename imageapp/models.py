from django.db import models
from PIL import Image
import PIL

# Create your models here.
#image app has photo fields and  data 
class Image(models.Model):
    photo = models.ImageField(upload_to='myimage')
    date = models.DateTimeField(auto_now_add=True)
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        img = PIL.Image.open(self.photo.path)
        
        myHeight, myWidth = img.size 
        img = img.resize((myHeight,myWidth) , PIL.Image.LANCZOS)
        img.save(self.photo.path)
        
            
        
    
   
   
    
    
