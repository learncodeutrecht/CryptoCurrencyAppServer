from django.db import models

# https://docs.djangoproject.com/en/2.0/ref/django-admin/#dumpdata
# https://docs.djangoproject.com/en/2.0/ref/django-admin/#loaddata
# https://docs.djangoproject.com/en/2.0/ref/models/fields/


class Coin(models.Model):
    name = models.TextField(unique=True)

class Pair(models.Model):
    # todo: add default from bitcoin  https://docs.djangoproject.com/en/2.0/ref/models/fields/#default
    frm = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name="frm", null=True, blank=True, default='')
    to  = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name="to")


class Price(models.Model):
    # <time>, <open>, <high>, <low>, <close>, <vwap>, <volume>, <count>
    # [1511680500,"7490.0","7490.0","7488.0","7490.0","7489.1","0.08708089",5]
    time   = models.BigIntegerField()
    open   = models.DecimalField(max_digits=24, decimal_places=12) # max = 99999.9
    high   = models.DecimalField(max_digits=24, decimal_places=12)
    low    = models.DecimalField(max_digits=24, decimal_places=12)
    close  = models.DecimalField(max_digits=24, decimal_places=12)
    vwap   = models.DecimalField(max_digits=24 , decimal_places=12)
    volume = models.DecimalField(max_digits=24, decimal_places=12) # max = 999.99999999
    count  = models.BigIntegerField()
    pair   = models.ForeignKey(Pair, on_delete=models.CASCADE)


class Symbol(models.Model):
    name    = models.CharField(max_length=5, unique=True)
    coin    = models.ForeignKey(Coin, on_delete=models.CASCADE)
    website = models.TextField()