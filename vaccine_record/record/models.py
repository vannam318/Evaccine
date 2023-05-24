from django.db import models
import uuid
from django import forms
from django.contrib.auth.models import User

# Thông tin người dùng

class PersonalInfo(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    Họ_và_Tên = models.CharField(max_length=200, help_text='', default='')
    Tuoi = models.IntegerField(help_text='')
    Ngày_sinh = models.DateField(blank=True, null=True, help_text='(vd: 2002-08-31)')
    Số_điện_thoại = models.CharField(max_length=20, help_text='', default='')
    def __str__(self):
        return self.Họ_và_Tên
    
# Thông tin vaccine

class VaccineInfo(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    personal_info = models.ForeignKey(PersonalInfo, null=True, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='')
    Tên_Vaccine = models.CharField(max_length=200, help_text='')
    Ngày_tiêm = models.DateField(blank=True, null=True, help_text='(vd: 2002-08-31)')
    Nơi_tiêm = models.CharField(max_length=200, help_text='')
    Sức_khỏe_trước_khi_tiêm = models.TextField(blank=True, help_text='')
    Sức_khỏe_sau_khi_tiêm = models.TextField(blank=True, help_text='')
    Liều_lượng = models.CharField(max_length=200, blank=True, help_text='')
    Ghi_chú = models.TextField(blank=True, help_text='')
    class Meta:
        ordering = ['Tên_Vaccine']   
    def __str__(self):
        return self.Tên_Vaccine
    
    # Thông tin người thân
class Relative(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    Role = models.CharField(max_length=200, help_text='Quan hệ')
    Relative_name = models.CharField(max_length=200, help_text='Họ và tên')
    Ngày_sinh = models.DateField(blank=True, null=True, help_text='(vd: 2002-08-31)')
    Tuoi = models.IntegerField(blank=True, null=True, help_text='Tuổi')
    def __str__(self):
        return self.Role
    
# Thông tin Vaccine cho người thân   
class RelativeVaccineInfo(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    relative_info = models.ForeignKey(Relative, null=True, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='')
    Tên_Vaccine = models.CharField(max_length=200, help_text='')
    Ngày_tiêm = models.DateField(blank=True, null=True, help_text='(vd: 2002-08-31)')
    Nơi_tiêm = models.CharField(max_length=200, help_text='')
    Sức_khỏe_trước_khi_tiêm = models.TextField(blank=True, help_text='')
    Sức_khỏe_sau_khi_tiêm = models.TextField(blank=True, help_text='')
    Liều_lượng = models.CharField(max_length=200, blank=True, help_text='')
    Ghi_chú = models.TextField(blank=True, help_text='')
    class Meta:
        ordering = ['Tên_Vaccine']   
    def __str__(self):
        return self.Tên_Vaccine
    
    
# Thanh tìm kiếm
class Filter(models.Model):
    Họ_và_Tên = models.CharField(max_length=200, help_text='', default='')    
    Tên_Vaccine = models.CharField(max_length=200, help_text='')
    Ngày_sinh = models.DateField(blank=True, null=True, help_text='(vd: 2002-08-31)')
    Số_điện_thoại = models.CharField(max_length=20, help_text='', default='')
    Role = models.CharField(null=True,max_length=200, help_text='Quan hệ')
    Relative_name = models.CharField(null=True,max_length=200, help_text='Họ và tên')
    
     # Thông tin người đăng ký
class User(models.Model):
    username = models.CharField(max_length=254, help_text= 'Username')
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.username
    
