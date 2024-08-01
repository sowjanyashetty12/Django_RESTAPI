from django.db import models

# Create your models here.
class product(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price)*0.8)
