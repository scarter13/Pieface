from tastypie.resources import ModelResource
from tastypie.constants import ALL

from pieface.models import Whatever, Entry

class WhateverResource(ModelResource):
    class Meta:
        queryset = Whatever.objects.all()
        resource_name = 'whatever'
        filtering = {'title': ALL}

class EntryResource(ModelResourced):
    
