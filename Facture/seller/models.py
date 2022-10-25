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
    quantity = models.IntegerField(help_text='Armencho mihat gri sti', validators=[MinValueValidator(1.0)])
    percent = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(10.0)])
    quantity_after_percent = models.FloatField()
    net_a_payer = models.FloatField()
    advance_payment = models.CharField(max_length=10, blank=True)
    total_payment = models.FloatField()
    total_tax = models.FloatField()
    total_payment_after_tax = models.FloatField()
