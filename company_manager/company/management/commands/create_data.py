import random
from django.core.management.base import BaseCommand
from company.factories import CompanyTypeFactory,CompanyFactory
from company.models import Company,CompanyType

class Command(BaseCommand):

    def add_arguments(self, parser)->None:
        parser.add_argument("-c",
                            "--company",
                            type=int,
                            help="Amount of companies to be created.",
                            required=True)

        parser.add_argument("-t",
                            "--companytype",
                            type=int,
                            help="Amount of companytypes to be created.",
                            required=True)

        parser.epilog = "Usage: python manage.py create_data -c 50 -t 5"

    def handle(self, *args, **kwargs):

        number_companies = kwargs.get("company")
        number_companytypes = kwargs.get("companytype")

        for m in [Company, CompanyType]:
            m.objects.all().delete()

        companytype_list =[]
        for _ in range(number_companytypes):
            companytype_list.append(
                CompanyTypeFactory()
            )

        for _ in range(number_companies):
            CompanyFactory(
                company_type=random.choice(companytype_list)
            )