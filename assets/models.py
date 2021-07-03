from django.db import models

class ProductType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class ModuleType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Version(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Unit(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    version = models.ForeignKey(Version, on_delete=models.RESTRICT)
    serial = models.CharField(max_length=200)
    mfg_date = models.DateTimeField('date manufactured')

    def __str__(self):
        return '%s SN: %s' % (self.product_type.name, self.serial) 

class Module(models.Model):
    module_type = models.ForeignKey(ModuleType, on_delete=models.RESTRICT)
    version = models.ForeignKey(Version, on_delete=models.RESTRICT)
    serial = models.CharField(max_length=200)
    mfg_date = models.DateTimeField('date manufactured')
    unit = models.ManyToManyField(Unit, blank=True)

    def __str__(self):
        return '%s SN: %s' % (self.module_type.name, self.serial) 




