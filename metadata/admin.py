# -*- coding: utf-8 -*-
from django.contrib.contenttypes import generic
from metadata.models import MetaData


class MetaDataTabularInline(generic.GenericTabularInline):
    model = MetaData


class MetaDataStackedInline(generic.GenericStackedInline):
    model = MetaData
