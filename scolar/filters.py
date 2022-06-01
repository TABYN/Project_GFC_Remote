
############################# Project Inventaire ####################################
import django_filters
from .models import *

class ImmobilierFilter(django_filters.FilterSet):

   class Meta:
        model = Immobilier
        fields = ['code_barre','num_inventaire','Num_facture']


  
        
