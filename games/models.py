from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='games/', blank=True, null=True)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100) 

    def __str__(self):
        return self.title

