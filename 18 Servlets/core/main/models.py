from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    @classmethod
    def create(cls, title, photo):
        obj = cls(title=title, photo=photo)
        # do something with the book
        return obj        