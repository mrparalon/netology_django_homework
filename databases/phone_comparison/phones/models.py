from django.db import models



class Phone(models.Model):
    name = models.CharField(max_length=128)
    brand = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ddr = models.IntegerField()
    screen_size = models.DecimalField(max_digits=3, decimal_places=1)
    ppi = models.IntegerField()
    system = models.CharField(max_length=128)
    memory = models.IntegerField()
    camera_resolution = models.DecimalField(max_digits=3, decimal_places=1)
    double_camera = models.BooleanField()
    bluetooth_version = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return f'{self.name}'


class PhoneApple(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    apple_id = models.BooleanField()
    face_id = models.BooleanField()

    def __str__(self):
        return self.phone.name


class PhoneSamsung(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    stylus = models.BooleanField()

    def __str__(self):
        return self.phone.name