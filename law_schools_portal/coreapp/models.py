from django.db import models
from cities_light.models import City, Country
from django.contrib.auth.models import User

# Create your models here.


class LawSchool(models.Model):

    class Meta:
        verbose_name = "Law School"
        verbose_name_plural = "Law Schools"

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=500)
    city = models.ForeignKey(City)
    country = models.ForeignKey(Country)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    extension = models.CharField(max_length=5, blank=True, null=True)
    phone2 = models.CharField(max_length=15, blank=True, null=True)
    extension2 = models.CharField(max_length=5, blank=True, null=True)
    fb_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    address_line1 = models.CharField("Address line 1", max_length=45,
                                     blank=True, null=True)
    address_line2 = models.CharField("Address line 2", max_length=45,
                                     blank=True, null=True)
    postal_code = models.IntegerField("Postal Code", max_length=10,
                                      blank=True, null=True)
    submitted_by = models.ForeignKey(User, null=True)
