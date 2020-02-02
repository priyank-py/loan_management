from django.db import models
from django.utils.translation import ugettext_lazy as _
from vendors.models import Vendor
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Budget(models.Model):

    budget_type_choices = (('personal', 'Personal'), ('corporate', 'Corporate'))

    title = models.CharField(_("Title"), max_length=50)
    budget_type = models.CharField(_("Loan Type Type"), choices=budget_type_choices, max_length=20, blank=True, null=True)
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    amount = models.IntegerField(_("Amount (in rupees)"))
    interest = models.FloatField(_("Rate of interest"), blank=True, null=True)
    duration = models.IntegerField(_("Duration (in months)"), blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    vendor = models.ForeignKey(Vendor , verbose_name=_("Customer"), on_delete=models.DO_NOTHING)
    

    class Meta:
        verbose_name = _("Loan")
        verbose_name_plural = _("Loans")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Budget_detail", kwargs={"pk": self.pk})
