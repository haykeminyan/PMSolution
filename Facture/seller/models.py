from django.core.exceptions import BadRequest, ValidationError
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
    ], default='RECHARGE EXPRESS 1234')
    quantity = models.IntegerField(help_text='Armencho mihat gri sti', validators=[MinValueValidator(1.0)], blank=True,
                                   null=True)
    percent = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(10.0)], blank=True, null=True)
    quantity_after_percent = models.FloatField(blank=True, null=True)
    net_a_payer = models.FloatField()
    advance_payment = models.CharField(max_length=10, blank=True)
    total_payment = models.FloatField(blank=True, null=True)
    total_tax = models.FloatField(blank=True, null=True)
    total_payment_after_tax = models.FloatField(blank=True, null=True)

    def __str__(self) -> str:
        """Return model string representation."""
        return f'{self.created_date} {self.name}'

    def clean(self):
        super().clean()
        if not self.quantity and not self.percent and not self.quantity_after_percent:
            raise ValidationError('Quantity, Percent, Quantity after percent are missing')
        if not self.quantity and not self.percent:
            raise ValidationError('Quantity, Percent are missing')
        elif not self.quantity and not self.quantity_after_percent:
            raise ValidationError('Quantity, Quantity after percent are missing')
        elif not self.percent and not self.quantity_after_percent:
            raise ValidationError('Percent, Quantity after percent are missing')

    # def save(self, *args, **kwargs):
    #     if not self.quantity_after_percent:
    #         self.quantity_after_percent = self.quantity * self.percent
    #     if not self.quantity:
    #         self.quantity = round(self.quantity_after_percent / self.percent, 2)
    #     if not self.percent:
    #         self.percent = round(self.quantity_after_percent / self.quantity, 2)
    #     super(Internal, self).save()

