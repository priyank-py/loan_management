from django.db import models
from django.utils.translation import ugettext_lazy as _
from budgets.models import Budget
from vendors.models import Vendor
from django.core.mail import EmailMessage

# Create your models here.
class Expense(models.Model):

    expense_types = (('personal', 'Personal'), ('corporate', 'Corporate'))

    budget = models.ForeignKey(Budget , verbose_name=_("Loan"), on_delete=models.CASCADE, blank=True, null=True)
    vendor = models.ForeignKey(Vendor , verbose_name=_("Customer"), on_delete=models.CASCADE)
    purpose = models.CharField(_("Remarks"), max_length=50, blank=True, null=True)
    expense_type = models.CharField(_("Loan Type"), max_length=50, choices=expense_types)


    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def __str__(self):
        return f'{self.budget} - {self.expense_type}'

    # def get_absolute_url(self):
    #     return reverse("Expense_detail", kwargs={"pk": self.pk})
    
    # def save(self, *args, **kwargs):
    #     msg = EmailMessage('Expense is added!', f'Expense for {self.expense_type} have been made to {self.vendor.name}\n\nRemarks:{self.purpose}', 'factscred@gmail.com', ['priyank7137@gmail.com'])
    #     msg.content_subtype = "html" 
    #     msg.send()

    #     super(Expense, self).save(*args, **kwargs)
    


class ExpenseInstallment(models.Model):

    PAY_CHOICES = (
        ('cash', 'Cash'),
        ('cheque', 'Cheque'),
        ('online', 'Online'),
        ('card', 'Credit/Debit Card'),
        ('DD', 'Demand Draft')
    )
    pay_status = (
        ('payed', 'Payment Cleared'), 
        ('pending', 'Payment Pending')
    )

    expense = models.ForeignKey(Expense, related_name="installments", on_delete=models.CASCADE)
    amount_paid = models.IntegerField(_("Amount Paid"), blank=True, null=True)
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=False, blank=True, null=True)
    payment_method = models.CharField(_("Payment Method"), choices=PAY_CHOICES, max_length=50, blank=True, null=True)
    transaction_no = models.CharField(_("Cheque/Transaction/Card/DD number"), default="NA", max_length=50, null=True)
    payed = models.CharField(_("Payment status"), choices=pay_status, max_length=20, blank=True)
    next_pay_date = models.DateField(_("Next Pay Date"), auto_now=False, auto_now_add=False, blank=True, null=True)


    class Meta:
        verbose_name = _("PaymentInstallment")
        verbose_name_plural = _("PaymentInstallments")

    def __str__(self):
        return f'{self.expense}'

    # def get_absolute_url(self):
    #     return reverse("ExpenseInstallment_detail", kwargs={"pk": self.pk})

    # def save(self, *args, **kwargs):
    #     self.this_expense = Expense.objects.all().filter(id=expense.id)
    #     setattr(self.this_expense, f'amount{id}', self.amount_paid)
    #     print(self.this_expense._meta)
        
    #     super(ExpenseInstallment, self).save(*args, **kwargs)
