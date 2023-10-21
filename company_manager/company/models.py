from django.db import models
from django.utils.text import slugify

# Create your models here.
class CompanyType(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    ordering = ["name"]
    slug=models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class Company(models.Model):

    class CompanySize(models.TextChoices):
        # TODO ändern, dass nicht zahl sondern bezeichnung angezeigt wird
        SMALLEST = "Kleinstunternehmen (<10 Beschäftigte)"
        SMALL = "Kleinunternehmen (10-49 Beschäftigte)"
        MEDIUM = "mittleres Unternehmen(50-249 Beschäftigte)"
        LARGE = "Großunternehmen(250+ Beschäftigte)"

    name=models.CharField(max_length=100)
    company_type = models.ForeignKey(
            CompanyType,
            on_delete=models.CASCADE,
            related_name="companies")
    description = models.TextField( 
            blank=True, null=True)
    company_size = models.CharField(max_length=100,
                                choices=CompanySize.choices
                                )
    slug=models.SlugField(unique=True)
    
    class Meta:
        verbose_name = "company"
        verbose_name_plural = "companies"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

