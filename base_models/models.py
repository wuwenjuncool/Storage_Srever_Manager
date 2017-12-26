from django.db import models

class Server(models.Model):
    name = models.CharField(max_length=30,blank=True)
    os = models.CharField(max_length=30,blank=True)
    kernel = models.CharField(max_length=30,blank=True)
    ssd = models.CharField(max_length=30,blank=True)
    nic = models.CharField(max_length=30,blank=True)
    owner = models.CharField(max_length=30,blank=True)
    used_for = models.CharField(max_length=30,blank=True)
    status =models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    bios = models.CharField(max_length=30,blank=True)
    cpu = models.CharField(max_length=30,blank=True)
    test_type = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Server_info'


# Create your models here.
