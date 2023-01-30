from django.contrib import admin
from api.models import Project,Employee
# Register your models here..

class ProjectAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)   
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','project')
    list_filter=('project',)

admin.site.register(Project,ProjectAdmin)
admin.site.register(Employee,EmployeeAdmin)