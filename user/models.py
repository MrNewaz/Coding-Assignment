from django.db import models


# Parent Model
class Parent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()

    # def __str__(self):
    #     return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ['first_name']


# Child Model
class Child(models.Model):
    parent = models.ForeignKey(
        Parent, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name_plural = "Children"
        ordering = ['first_name']
