import random
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Company, CompanyType
from .forms import CompanyForm
# Create your views here.

class CompanyListView(ListView):
    model = Company

class CompanyDetailView(DetailView):
    model = Company

''' veraltet
# def show_company(request, pk: int):
#     company_obj = get_object_or_404(Company, pk=pk)
#     return render(request, "company/company_details.html",
#     {"company": company_obj})
    # qs = request.GET
    # try:
    #     id_ = qs["id"]
    #     try: 
    #         obj = Company.objects.get(pk=id_)
    #         return HttpResponse(obj)
    #     except Company.DoesNotExist:
    #         raise Http404("This company ist not registered!")
            
    # except (MultiValueDictKeyError, ValueError):
    #     raise Http404("Es wurde kein gültiger Querystring übergeben!")

# def companies(request):
#     """ 
#     shows all registered companies
#     company/companies
#     """
#     companies_list = Company.objects.all()
#     return render(request, "company/companies.html",
#                 {"companies": companies_list})
    # qs = request.GET
    # if not qs:
    #     company_list = Company.objects.all()
    #     company_list_name = []
    #     for company in company_list:
    #         company_list_name.append(str(company))
    #     return HttpResponse("<br>".join(company_list_name))
    
    # try:
    #     order = qs["order"]
    #     """ 
    #     shows the companies in a defined order
    #     company/companies?order=name
    #     """
    #     company_list = Company.objects.order_by(order)
    #     company_list_name = []
    #     for company in company_list:
    #         company_list_name.append(str(company))
    #     return HttpResponse("<br>".join(company_list_name))
    # except (MultiValueDictKeyError, ValueError):

    #     try:
    #         start = qs["from"]
    #         stop = qs["to"]
    #         """ 
    #         shows the companies in a selected intervall(from/to)
    #         company/companies?from=1&to=3
    #         """
    #         company_list = Company.objects.filter(id__range=(start,stop))
    #         company_list_name = []
    #         for company in company_list:
    #             company_list_name.append(str(company))
    #         return HttpResponse("<br>".join(company_list_name))
    #     except(MultiValueDictKeyError, ValueError):
    #         return HttpResponse("Es wurde kein gültiger Querystring übergeben!")
'''

def companies_random(request):
    """ 
    shows a randomly selected company
    company/random
    """
    company_list = Company.objects.all()
    random_company = random.choice(company_list)
    return render(request, 
                "company/random.html", 
                {"company": random_company,}
                )

def company_add(request):
    if request.method == "POST":
        form = CompanyForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("company:companies")
    else:
        form = CompanyForm()
    
    return render(request, "company/company_add.html", {
        "form": form,
    })

def company_update(request, slug):

    company = get_object_or_404(Company, slug=slug)
    form = CompanyForm(request.POST or None, instance=company)
    if form.is_valid():
        form.save()
        return redirect("company:companies")

    return render(request, 
                "company/company_update.html", 
                {"form": form,}
                )

class CompanyTypeListView(ListView):
    model = CompanyType

class CompanyTypeDetailView(DetailView):
    model = CompanyType