from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Vendor(models.Model):


    name = models.CharField(_("Customer name"), max_length=50)
    phone = models.CharField(_("Phone number"), max_length=50)
    alternate = models.CharField(_("Alternate number"), max_length=50, blank=True, null=True)
    address = models.TextField(_("Address"), blank=True, null=True)
    connection = models.CharField(_("Role"), max_length=50, blank=True, null=True)
    photo = models.ImageField(_("upload photo"), upload_to='vendor_photos/%Y/%m', blank=True)
    gst = models.CharField(_("GST no."), max_length=50, blank=True, null=True)
    tan = models.CharField(_("TAN no."), max_length=50, blank=True, null=True)
    pan = models.CharField(_("PAN no."), max_length=50, blank=True, null=True)

    

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Vendor_detail", kwargs={"pk": self.pk})


class VendorAccount(models.Model):

    account_type_choices = (
        ('current', 'Current'), 
        ('savings', 'Savings'),
    )

    vendor = models.ForeignKey(Vendor , verbose_name=_("Customer"), related_name="vendor_accounts",on_delete=models.CASCADE)
    account_name = models.CharField(_("Account Name"), max_length=50, blank=True, null=True)
    account_number = models.CharField(_("Account Number"), max_length=50, blank=True, null=True)
    bank_branch = models.CharField(_("Bank Branch"), max_length=50, blank=True, null=True)
    ifsc_code = models.CharField(_("IFSC code"), max_length=50, blank=True, null=True)
    account_type = models.CharField(_("Account Type"), max_length=50, choices=account_type_choices, blank=True, null=True)

    class Meta:
        verbose_name = _("Customer Account")
        verbose_name_plural = _("Customer Accounts")