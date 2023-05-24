import django_filters
from .models import Filter


class FilterBar(django_filters.FilterSet):
    class Meta:
        model = Filter
        fields = ("Tên_Vaccine",) 
        
class NameFilter(django_filters.FilterSet):
    class Meta:
        model = Filter
        fields = ("Họ_và_Tên", "Ngày_sinh", "Số_điện_thoại")
        
class RelativeNameFilter(django_filters.FilterSet):
    class Meta:
        model = Filter
        fields = ("Role", "Relative_name")
        labels = {
            'Relative_name': 'Họ và tên',
            'Role': 'Quan hệ',
        }