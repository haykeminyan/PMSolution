from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


# Create your models here.


class Internal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default='Ayk')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    reference = models.CharField(max_length=10, blank=True)
    destination = models.CharField(max_length=30, validators=[
        RegexValidator(
            regex='(RECHARGE\sEXPRESS\s.+)',
        ),
    ], default='RECHARGE EXPRESS 1234')
    quantity = models.IntegerField(help_text='Armencho mihat gri sti', validators=[MinValueValidator(1.0)], blank=True,
                                   null=True, default=12)
    percent = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(10.0)], blank=True, null=True, default=3)
    quantity_after_percent = models.FloatField(blank=True, null=True, default=3)
    net_a_payer = models.FloatField(default=123)
    advance_payment = models.CharField(max_length=10, blank=True, default=4)
    total_payment = models.FloatField(default=34)
    total_tax = models.FloatField(default=1)
    total_payment_after_tax = models.FloatField(default=3)

    def __str__(self) -> str:
        """Return model string representation."""
        return f'{self.created_date} {self.name}'

    def save(self, *args, **kwargs):
        if not self.quantity_after_percent:
            self.quantity_after_percent = self.quantity * self.percent
        if not self.quantity:
            self.quantity = round(self.quantity_after_percent / self.percent, 2)
        if not self.percent:
            self.percent = round(self.quantity_after_percent / self.quantity, 2)
        super(Internal, self).save()
