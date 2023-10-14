from django.db import models

# Create your models here.


class BookingForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    guest = models.CharField(max_length=5)

    class Meta:
        verbose_name_plural = ("BookingForm")

    def __str__(self):
        return self.name
    

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    massage = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = ("ContactForm")

    def __str__(self):
        return self.name
    





class blog_img_1(models.Model):
    date = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pros')
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = ("blog_img_1")

    def __str__(self):
        return self.date


class blog_img_2(models.Model):
    date = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pros')
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = ("blog_img_2")

    def __str__(self):
        return self.date
    

class blog_img_3(models.Model):
    date = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pros')
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = ("blog_img_3")

    def __str__(self):
        return self.date





