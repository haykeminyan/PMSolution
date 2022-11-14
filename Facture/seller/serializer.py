from seller.models import Internal
from rest_framework import serializers


class InternalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Internal
        fields = ['id', 'name', 'created_date', 'updated_date',
                  'reference', 'destination', 'quantity', 'percent', 'quantity_after_percent',
                  'net_a_payer', 'advance_payment', 'total_payment', 'total_tax',
                  'total_payment_after_tax']

        def create(self, validated_data):
            return Internal.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.created_date = validated_data.get('created_date', instance.created_date)
            instance.updated_date = validated_data.get('updated_date', instance.updated_date)
            instance.reference = validated_data.get('reference', instance.reference)
            instance.destination = validated_data.get('destination', instance.destination)
            instance.quantity = validated_data.get('quantity', instance.quantity)
            instance.quantity_after_percent = validated_data.get('quantity_after_percent', instance.quantity_after_percent)
            instance.net_a_payer = validated_data.get('net_a_payer', instance.net_a_payer)
            instance.advance_payment = validated_data.get('advance_payment', instance.advance_payment)
            instance.total_payment = validated_data.get('total_payment', instance.total_payment)
            instance.total_tax = validated_data.get('total_tax', instance.total_tax)
            instance.total_payment_after_tax = validated_data.get('total_payment_after_tax', instance.total_payment_after_tax)
            instance.save()
            return instance

