from django.db import models

# Create your models here.
class SimpleModel(models.Model):
    name =  models.CharField(max_length=20, null=True, blank= False)

    class Meta:
        abstract = True
    def __str__(self):
        return f"{self.name}"
    def __repr__(self):
        return f"{self.pk}" 

class Product(SimpleModel):
    '''Extended From SimpleModel fields'''

class ModelB1(SimpleModel):
    '''Extended From SimpleModel fields'''

class ModelB2(SimpleModel):
    '''Extended From SimpleModel fields'''

class ModelC1(SimpleModel):
    '''Extended From SimpleModel fields'''

class ModelC2(SimpleModel):
    '''Extended From SimpleModel fields'''

class ModelD(SimpleModel):
    '''Extended From SimpleModel fields'''

class ModelA(models.Model):
    buy_sell = models.CharField(max_length=10, choices=(
                ("buy", "Buy"), ("sell", "Sell") ), null=True, blank= False)
    variableA1 = models.ForeignKey(ModelD,related_name='model_d_model_a', on_delete=models.CASCADE, blank=False, null=True)
    date_start = models.DateField(null=True)
    date_end = models.DateField(null= True)
    variableA2 = models.CharField(choices = ( ("aa1", "AA1"), ("aa2", "AA2")), max_length=10,
                    null=True, blank= False )
    product = models.ForeignKey(Product, related_name='product_model_a', on_delete=models.CASCADE, blank=False, null=True)

class ModelB(models.Model):
    variableB1 = models.ForeignKey(ModelB1,related_name='model_b1_model_b_1',
                    on_delete=models.CASCADE, blank=False, null=True )
    variableB2 = models.IntegerField(null=True)
    variableB3 = models.ForeignKey(ModelB2,related_name='model_b2_model_b_3',
                    on_delete=models.CASCADE, blank=False, null=True )
    variableB4 = models.ForeignKey(ModelB1,related_name='model_b1_model_b_4',
                    on_delete=models.CASCADE, blank=False, null=True )
    variableB5 = models.IntegerField(null= True)
    product = models.ForeignKey(Product, related_name='product_model_b',
                on_delete=models.CASCADE, blank=True, null= True)



class ModelC(models.Model):
    variableC1 = models.ForeignKey(ModelC1,related_name='model_c1_model_c_1',
                    on_delete=models.CASCADE, blank=False, null=True )
    variableC2 = models.IntegerField(null= True)
    variableC3 = models.ForeignKey(ModelC2,related_name='model_c2_model_c_3',
                    on_delete=models.CASCADE, blank=False, null=True )
    variableC4 = models.ForeignKey(ModelC1,related_name='model_c1_model_c_4',
                    on_delete=models.CASCADE, blank=False, null=True )
    variableC5 = models.IntegerField(null= True)
    product = models.ForeignKey(Product, related_name='product_model_c',
                on_delete=models.CASCADE, blank=True, null=True)
    # PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$
