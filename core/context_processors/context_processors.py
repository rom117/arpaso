#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sites.models import Site

#Q4: add all the variables of the settings file in the context object
#this object is sent by views and can be used in any template (ex in homepage)
def add_settings_variables(request):
    return {'settings' : settings}

def get_current_path(request):
    return {'current_path': request.get_full_path()}
