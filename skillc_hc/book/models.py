from django.db import models

class Author(models.Model):
    name = models.CharField(blank=False,max_length=250)
    birth_date = models.DateField(blank=True,auto_now=True)
    nationality = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(blank=False, unique=True, max_length=400)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author_name")
    genre = models.ManyToManyField(Genre,related_name="genre_names")
    publication_date = models.DateField(auto_now=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.title} written by {self.author} "


