from rest_framework import serializers
from seller.models import Internal


class InternalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internal
        fields = [
            'id',
            'name',
            'reference',
            'destination',
            'quantity',
            'percent',
            'quantity_after_percent',
            'net_a_payer',
            'advance_payment',
            'total_payment',
            'total_tax',
            'total_payment_after_tax',
        ]
