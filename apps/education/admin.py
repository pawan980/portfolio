from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Education, Certification


@admin.register(Education)
class EducationAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('institution', 'degree', 'field_of_study', 'start_date', 'is_current', 'is_visible', 'order')
    list_filter = ('degree', 'is_current', 'is_visible')
    list_editable = ('is_current', 'is_visible')


@admin.register(Certification)
class CertificationAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'issuing_organization', 'date_obtained', 'is_visible', 'order')
    list_filter = ('issuing_organization', 'is_visible')
    list_editable = ('is_visible',)