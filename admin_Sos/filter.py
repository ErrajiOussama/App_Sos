import django_filters
from .models import *

class Cola_filter(django_filters.FilterSet):
    Nom = django_filters.CharFilter(lookup_expr='icontains')
    Prenom = django_filters.CharFilter(lookup_expr='icontains')
    Activite = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model= Collaborateur
        fields = ['Nom', 'Prenom','Activite']
"""
class salaire_filter(django_filters.FilterSet):
    Date = django_filters.MonthYearField(lookup_expr='icontains')
    class Meta:
        model= Collaborateur
        fields = ['Date']"""