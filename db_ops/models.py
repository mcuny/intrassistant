from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255, primary_key=True, db_index=True, unique=True)
    type = models.CharField(max_length=255)
    subLocation = models.OneToOneField('Location', default=None, blank=True, null=True, on_delete='')

class Hardware(models.Model):
    id = models.CharField(max_length=255, primary_key=True, db_index=True, unique=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    power = models.OneToOneField('PowerCable', null=True, on_delete='')
    documentation = models.CharField(max_length=512)
    location = models.OneToOneField('Location', null=True, on_delete='')

class PowerCable(models.Model):
    id = models.CharField(max_length=255, primary_key=True, db_index=True, unique=True)
    name = models.CharField(max_length=255)
    location = models.OneToOneField('Location', null=True, on_delete='')

class NetworkCable(models.Model):
    id = models.CharField(max_length=255, primary_key=True, db_index=True, unique=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    location = models.OneToOneField('Location', null=True, on_delete='')

class HardwareCable(models.Model):
    hardware = models.OneToOneField('Hardware', null=True, on_delete='')
    cable = models.OneToOneField('NetworkCable', null=True, on_delete='')

