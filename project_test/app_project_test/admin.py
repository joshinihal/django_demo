from django.contrib import admin
from app_project_test.models import Category, Brand, Webpage, AccessRecord, Employee

# Register your models here.
# admin.site.register(Topic)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Employee)


admin.site.register(Webpage)
admin.site.register(AccessRecord)
