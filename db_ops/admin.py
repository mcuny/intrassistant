from django.contrib import admin
from .models import Location, Hardware, PowerCable, NetworkCable, HardwareCable
# Register your models here.

admin.site.register(Location)
admin.site.register(Hardware)
admin.site.register(PowerCable)
admin.site.register(NetworkCable)
admin.site.register(HardwareCable)
