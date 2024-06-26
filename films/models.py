from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class film(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=150, verbose_name="Başlıq")
    content = RichTextField(verbose_name="Məzmun")  
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to="film Images",blank=True, null=True,verbose_name="Şəkil")   

    def __str__(self):   
        return self.title
    
    
    
class Comment(models.Model):
    films = models.ForeignKey(film, on_delete=models.CASCADE, verbose_name="Məqalə", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="Ad")
    comment_content = models.TextField(verbose_name="Şərh")
    comment_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
            return f"{self.comment_author}"