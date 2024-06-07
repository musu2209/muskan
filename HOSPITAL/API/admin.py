from django.contrib import admin

from . models import*

admin.site.register(PATIENT)
admin.site.register(MEDICINE)
admin.site.register(REPORT)
admin.site.register(DOCTOR)
admin.site.register(STAFF)
admin.site.register(DEPARTMENT)


