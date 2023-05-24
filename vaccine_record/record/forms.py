from django import forms
from django.forms import ModelForm
from .models import PersonalInfo, VaccineInfo,Relative,RelativeVaccineInfo
from django.contrib.auth.models import  User
from django.forms import DateInput

class UserProfileInfo(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ("Họ_và_Tên","Ngày_sinh","Số_điện_thoại","Tuoi")
        labels = {
            'Tuoi': 'Tuổi',
        }
        widgets = {
            'Ngày_sinh': DateInput(attrs={'type': 'date'}),
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-group'}))
    class Meta:
        model= User
        fields = ("username","email","password")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-group'}),
            'email': forms.EmailInput(attrs={'class': 'form-group'})
        }

class vaccine(forms.ModelForm):
    class Meta:
        model = VaccineInfo
        fields = ("Tên_Vaccine", "Ngày_tiêm", "Nơi_tiêm", "Sức_khỏe_trước_khi_tiêm", "Sức_khỏe_sau_khi_tiêm", "Liều_lượng", "Ghi_chú")
        widgets = {
            'Ngày_tiêm': DateInput(attrs={'type': 'date'}),
        }
        
class RelativeInfo(forms.ModelForm):
    class Meta:
        model = Relative
        fields = ("Relative_name", "Role", "Tuoi", "Ngày_sinh")
        labels = {
            'Relative_name': 'Họ và tên',
            'Role': 'Quan hệ',
            'Tuoi': 'Tuổi',
        }
        widgets = {
            'Ngày_sinh': DateInput(attrs={'type': 'date'}),
        }
class RelativeVaccine(forms.ModelForm):
    class Meta:
        model= RelativeVaccineInfo
        fields = ("Tên_Vaccine", "Ngày_tiêm", "Nơi_tiêm", "Sức_khỏe_trước_khi_tiêm", "Sức_khỏe_sau_khi_tiêm", "Liều_lượng", "Ghi_chú")
        widgets = {
            'Ngày_tiêm': DateInput(attrs={'type': 'date'}),
        }