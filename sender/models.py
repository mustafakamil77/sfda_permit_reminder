from django.db import models

# Create your models here.
class SdfaPermit(models.Model):
    id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=200, null=False, blank=False)
    application_date = models.DateTimeField(auto_now=False)
    transaction_number = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    invoice_number = models.CharField(max_length=100, unique=True)
    notes = models.CharField(max_length=250, null=True, blank=True)
    release_date = models.DateTimeField(auto_now=False, null=True, blank=True)
    expiry_date = models.DateTimeField(auto_now=False, null=True, blank=True)
    renewal_date = models.DateTimeField(auto_now=False, null=True, blank=True)
    notify = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.company_name)