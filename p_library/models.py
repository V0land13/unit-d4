from django.db import models

class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)
    def __str__(self):
        return self.full_name


class Redaction(models.Model):
    red_name = models.TextField()
    red_region = models.TextField()
    reg_contact = models.TextField()
    reg_site = models.TextField()
    def __str__(self):
        return self.red_name

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    redaction = models.ForeignKey(Redaction, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    def __str__(self):
        return self.title
