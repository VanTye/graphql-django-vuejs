from django.contrib import admin
from .models import City, EmployeeTitle, Employee

class CityAdmin(admin.ModelAdmin):
    fields = ('city_name',)
    search_fields = ('name',)
    list_display = ('id','city_name')

class EmployeeTitleAdmin(admin.ModelAdmin):
    fields = ('title_name',)
    search_fields = ('title_name',)
    list_display = ('id','title_name')

class EmployeeAdmin(admin.ModelAdmin):
    fields = ('employee_name', 'employee_city', 'employee_title',)
    search_fields = ('employee_name', 'employee_city', 'employee_title',)
    list_display = ('employee_name', 'employee_city', 'employee_title',)

admin.site.register(City, CityAdmin)
admin.site.register(EmployeeTitle, EmployeeTitleAdmin)
admin.site.register(Employee, EmployeeAdmin)

