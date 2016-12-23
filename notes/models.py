from django.db import models


class Note(models.Model):
    name = models.CharField(max_length=512)
    email = models.CharField(max_length=254)

    def __str__(self):
        return self.name, self.email