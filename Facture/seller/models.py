from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


# Create your models here.


class Internal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    reference = models.CharField(max_length=10, blank=True)
    destination = models.CharField(max_length=30, validators=[
        RegexValidator(
            regex='(RECHARGE\sEXPRESS\s.+)',
        ),
    ])
    quantity = models.IntegerField(help_text='Armencho mihat gri sti', validators=[MinValueValidator(1.0)], blank=True,
                                   null=True)
    percent = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(10.0)], blank=True, null=True)
    quantity_after_percent = models.FloatField(blank=True, null=True)
    net_a_payer = models.FloatField()
    advance_payment = models.CharField(max_length=10, blank=True)
    total_payment = models.FloatField()
    total_tax = models.FloatField()
    total_payment_after_tax = models.FloatField()

    def __str__(self) -> str:
        """Return model string representation."""
        return f'{self.created_date} {self.name}'

    @property
    def get_quantity_after_percent(self):
        # if not self.quantity_after_percent:
        return self.quantity * self.percent

    @property
    def get_quantity(self):
        return round(self.quantity_after_percent / self.percent, 2)

    @property
    def get_percent(self):
        return round(self.quantity_after_percent / self.quantity, 2)

    def save(self, *args, **kwargs):
        if not self.quantity_after_percent:
            self.quantity_after_percent = self.get_quantity_after_percent
        if not self.quantity:
            self.quantity = self.get_quantity
        if not self.percent:
            self.percent = self.get_percent
        super(Internal, self).save()
