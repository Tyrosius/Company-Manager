from django.contrib import admin
from .models import Company,CompanyType

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["id","name","company_type","company_size","description"]
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ["name",]

@admin.register(CompanyType)
class CompanyTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "name","description"]
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ["name",]