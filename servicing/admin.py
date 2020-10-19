from django.contrib import admin
from .models import Car,Service
# Register your models here.

admin.site.site_header = "Instant Car Service"
admin.site.site_title = "Welcome to Instant Car Service"
admin.site.index_title = "Car Service"

admin.site.register(Service)

@admin.register(Car)
class CarAdmi(admin.ModelAdmin):
    search_fields = ('car_model', 'description','car_number','car_owner'  )
    list_display = ['car_model','car_owner','car_notes','car_number','description','service_type','submission_date','year_old']
    list_display_links=['car_model','car_owner','car_notes','car_number','description','service_type','submission_date','year_old']
    list_per_page =10
    list_max_show_all =5
    list_filter = ['service_type','submission_date','year_old']
    list_select_related =True