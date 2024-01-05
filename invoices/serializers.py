# Creating Django Rest Framework serializers for the models Invoice and InvoiceDetail to convert them to and from JSON

from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['id', 'description', 'quantity', 'unit_price', 'price']

# The update method in the InvoiceSerializer needs to be implemented based on the specific requirements for handling updates.

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['id', 'date', 'customer_name', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return invoice

    def update(self, instance, validated_data):
        # Update logic here
        return instance
