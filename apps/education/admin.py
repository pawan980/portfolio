from django.contrib import admin
from .models import Education, Certification


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'field_of_study', 'start_date', 'is_current', 'is_visible')
    list_filter = ('degree', 'is_current', 'is_visible')
    list_editable = ('is_current', 'is_visible')


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuing_organization', 'date_obtained', 'is_visible')
    list_filter = ('issuing_organization', 'is_visible')
    list_editable = ('is_visible',)