from django.db import models


"""
 - CharField for adding a text field to a model.
 - IntegerField for adding an integer field to a model.
"""

# Parent Model


class Parent(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ['first_name']


# Child Model
class Child(models.Model):
    parent = models.ForeignKey(
        Parent, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name_plural = "Children"
        ordering = ['first_name']
