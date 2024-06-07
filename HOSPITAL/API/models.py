from django.db import models
from .models import*
class PATIENT(models.Model):
    p_id = models.AutoField(primary_key = True)
    p_name = models.CharField(max_length=100)
    p_age = models.IntegerField()
    p_gender = models.CharField(max_length=10)
    p_mobile = models.IntegerField()
    p_address = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.p_mobile)

class DOCTOR(models.Model):
    d_id = models.AutoField(primary_key = True)
    d_name = models.CharField(max_length=100)
    d_age = models.IntegerField()
    d_gender = models.CharField(max_length=10)
    d_mobile = models.IntegerField()
    d_department = models.CharField(max_length= 100)

class MEDICINE(models.Model):
    m_id = models.AutoField(primary_key = True)
    m_name = models.CharField(max_length=100)
    m_unitPrice = models.IntegerField()
    p_id = models.ForeignKey(PATIENT,on_delete= models.CASCADE)

class REPORT(models.Model):
    r_id = models.AutoField(primary_key = True)
    p_id = models.CharField(max_length=100)
    d_id = models.IntegerField()
    s_id = models.CharField(max_length=10)
    dept_id = models.IntegerField()

class STAFF(models.Model):
    s_id = models.AutoField(primary_key = True)
    s_name = models.CharField(max_length=100)
    s_age = models.IntegerField()
    s_gender = models.CharField(max_length=10)
    s_mobile = models.IntegerField()
    s_department = models.CharField(max_length= 100)


class DEPARTMENT(models.Model):
    dept_id =models.AutoField(primary_key = True)
    dept_name = models.CharField(max_length=100)
    
