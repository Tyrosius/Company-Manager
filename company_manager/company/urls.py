from django.urls import path
from . import views

app_name = "company"

urlpatterns=[
    path("show-company/<slug:slug>", 
        views.CompanyDetailView.as_view(), 
        name="show_company"),

    path("companies", 
        views.CompanyListView.as_view(), 
        name="companies"),

    path("random", 
        views.companies_random, 
        name="companies_random"),
        
    path("add-companie",
        views.company_add,
        name="company_add"),

    path("company-update/<slug:slug>",
        views.company_update,
        name="company_update"),

    path("companytype/<slug:slug>", 
        views.CompanyTypeDetailView.as_view(), 
        name="show_companytype"),

    path("companytypes", 
        views.CompanyTypeListView.as_view(), 
        name="companytypes"),
]

