from django.db import models

""""
prefetch_related() Query is used to boost database Performance in case of ManyToManyField
"""

class Genre(models.Model):
    """A genre indicates what type of content a book is based on, 
    such as Science Fiction, Mystery, Romance, Travel, or other categories.  """
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

""""prefetch_related() is Used only For ManyToManyField
 for OneToOne & ForeignKey select_related() is used"""
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    description=models.TextField()
    published_date=models.DateField()
    genres=models.ManyToManyField(Genre,related_name='book_data')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.title + "-->"+str(self.price)


class Department(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=124)
    age=models.IntegerField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name