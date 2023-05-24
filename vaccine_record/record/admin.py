from django.contrib import admin
from .models import PersonalInfo, VaccineInfo,Relative,RelativeVaccineInfo



admin.site.register(PersonalInfo)
admin.site.register(VaccineInfo)
admin.site.register(Relative)
admin.site.register(RelativeVaccineInfo)
