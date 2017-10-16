from django.db import models


class Product(models.Model):
    product_model = models.CharField(max_length=200)
    processor_model = models.CharField(max_length=64)
    processor_frequency = models.IntegerField()
    ram_value = models.IntegerField()
    display_size = models.FloatField()
    videocard = models.CharField(max_length=128)
    video_memory_value = models.IntegerField()
    weight = models.FloatField()
    optical_drive = models.BooleanField()
    lte_4g = models.BooleanField()
    bluetooth = models.BooleanField()
    wi_fi = models.BooleanField()
    price = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='products_images')

    def __str__(self):
        return self.product_model


class Color(models.Model):
    product = models.ForeignKey(Product, related_name='colors',
                                on_delete=models.CASCADE)
    product_color = models.CharField(max_length=64)

    def __str__(self):
        return self.product_color


class Hdd(models.Model):
    product = models.ForeignKey(Product,related_name='hdd_capacity',
                                on_delete=models.CASCADE)
    hdd_capacity = models.IntegerField()

    def __str__(self):
        return str(self.hdd_capacity)


