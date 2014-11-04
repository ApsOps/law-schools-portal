from django.db import models
from cities_light.models import City, Country

# Create your models here.


class Address(models.Model):

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __unicode__(self):
        pass

    address_line1 = models.CharField("Address line 1", max_length=45)
    address_line2 = models.CharField("Address line 2", max_length=45,
                                     blank=True)
    postal_code = models.CharField("Postal Code", max_length=10)


class LawSchool(models.Model):

    class Meta:
        verbose_name = "Law School"
        verbose_name_plural = "Law Schools"

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=500)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    fb_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    city = models.ForeignKey(City)
    country = models.ForeignKey(Country)
    address = models.ForeignKey(Address, blank=True)
