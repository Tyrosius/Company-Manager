import factory
import random
from .models import Company, CompanyType

class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model= Company

    name=factory.Faker("company")
    description=factory.Faker("catch_phrase")
    company_size=factory.LazyAttribute(
        lambda _:random.choice(list(Company.CompanySize))
    )

COMPANYTYPES =[
    "food",
    "tech",
    "finanzial",
    "mining",
    "agriculture",
    "comercials",
    "entertainment",
    "shipping",
    "processing"
]

class CompanyTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=CompanyType

    name=factory.Iterator(COMPANYTYPES)
    description=factory.Faker("paragraph", nb_sentences=4)