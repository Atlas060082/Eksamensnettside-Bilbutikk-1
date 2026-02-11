from django.contrib import admin
from .models import Bil, Service

class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1
    fields = ['type', 'beskrivelse', 'planlagt_dato', 'fullført', 'ansvarlig']

@admin.register(Bil)
class BilAdmin(admin.ModelAdmin):
    list_display = ['regnummer', 'merke', 'modell', 'årsmodell', 'status', 'innkommet_dato']
    list_filter = ['status', 'merke', 'drivstoff']
    search_fields = ['regnummer', 'merke', 'modell']
    list_editable = ['status']
    
    inlines = [ServiceInline]
    
    fieldsets = (
        ('Bilinfo', {
            'fields': ('merke', 'modell', 'årsmodell', 'regnummer')
        }),
        ('Teknisk', {
            'fields': ('kilometerstand', 'drivstoff', 'girkasse', 'farge')
        }),
        ('Økonomi', {
            'fields': ('innkjøpspris', 'salgspris')
        }),
        ('Status', {
            'fields': ('status', 'innkommet_dato')
        }),
        ('Detaljer', {
            'fields': ('beskrivelse', 'bilde'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['bil', 'type', 'planlagt_dato', 'fullført', 'ansvarlig']
    list_filter = ['fullført', 'type', 'planlagt_dato']
    search_fields = ['bil__regnummer', 'bil__merke', 'beskrivelse']
    list_editable = ['fullført']
    
    fieldsets = (
        ('Service', {
            'fields': ('bil', 'type', 'beskrivelse')
        }),
        ('Planlegging', {
            'fields': ('planlagt_dato', 'ansvarlig')
        }),
        ('Kostnader', {
            'fields': ('estimert_kostnad', 'faktisk_kostnad')
        }),
        ('Status', {
            'fields': ('fullført', 'fullført_dato', 'notater')
        }),
    )