from django.contrib import admin
from .models import *

admin.site.register(Question)
admin.site.register(Tag)
admin.site.register(CaseStudy)
admin.site.register(TagRelationship)
admin.site.register(MedicalHistory)
admin.site.register(Medication)
