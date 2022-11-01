from django.db import models

<<<<<<< HEAD
# Custom queryset


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)


class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

=======
#Custom queryset
class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active = True)

    def featured(self):
        return self.filter(featured = True, active = True)

class ProductManager(models.Manager):
    
    def get_queryset(self):
        return ProductQuerySet(self.model, using = self._db)
    
>>>>>>> featured_custom_queryset
    def all(self):
        return self.get_queryset().active()

    def featured(self):
<<<<<<< HEAD
        # return self.get_queryset().filter(featured = True)
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

# Create your models here.
=======
        #return self.get_queryset().filter(featured = True)
        return self.get_queryset().featured()
>>>>>>> featured_custom_queryset

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        if qs.count() == 1:
            return qs.first()
        return None

# Create your models here.
class Product(models.Model): #product_category
    title       = models.CharField(max_length=120)
    description = models.TextField()
<<<<<<< HEAD
    price = models.DecimalField(
        decimal_places=2, max_digits=20, default=100.00)
    image = models.FileField(upload_to='products/', null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = ProductManager()
=======
    price       = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    image       = models.FileField(upload_to = 'products/', null = True, blank = True)
    featured    = models.BooleanField(default = False)
    active      = models.BooleanField(default = True)

>>>>>>> featured_custom_queryset

    objects = ProductManager()
    
    #python 3
    def __str__(self):
        return self.title
<<<<<<< HEAD
    # python 2

=======
    #python 2
>>>>>>> featured_custom_queryset
    def __unicode__(self):
        return self.title