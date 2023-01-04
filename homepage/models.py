from django.db import models

# Create your models here.
class Benh(models.Model):
    ten_benh = models.CharField(max_length=200)
    kh = models.CharField(max_length=50)
    nguyen_nhan = models.TextField(blank=True)
    dieu_tri = models.TextField(blank=True)

    def __str__(self):
        return self.ten_benh

class TrieuChung(models.Model):
    benh = models.ForeignKey(Benh, on_delete= models.CASCADE)
    ten = models.CharField(max_length=200)
    ki_hieu = models.CharField(max_length=50)
    trongso = models.IntegerField(default=1)
    gia_tri = models.FloatField(default=0)
    def __str__(self):
        return self.ten