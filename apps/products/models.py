from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def create_new_product(self, request):
        print '****************************************************************************************'
        catz = self.create(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
        print '*'*100
        print catz
        print '*'*100

    def update(self, request):
        pass
    def destroy(self, request):
        pass
    def show(self, request):
        pass


class Product(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = ProductManager()
