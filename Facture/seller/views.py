from io import BytesIO

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from openpyxl import Workbook
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from openpyxl.styles import Alignment, Font
from rest_framework.exceptions import NotFound
from rest_framework.parsers import JSONParser
import logging
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from seller.forms import InternalForm
from seller.serializer import InternalSerializer
from seller.models import Internal

logger = logging.getLogger(__name__)


class InternalList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Internal.objects.all()
        serializer = InternalSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InternalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return render(request, template_name='index.html')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InternalDetail(APIView):
    def get_object(self, pk):
        try:
            return Internal.objects.get(pk=pk)
        except Internal.DoesNotExist:
            raise NotFound()

    def get(self, request, pk, format=None):
        internal = self.get_object(pk)
        serializer = InternalSerializer(internal)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        internal = self.get_object(pk)
        serializer = InternalSerializer(internal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        internal = self.get_object(pk)
        internal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    if request.method == 'POST':
        internal_form = InternalForm(request.POST)
        name = request.POST['name']
        destination = request.POST['destination']
        net_a_payer = request.POST['net_a_payer']
        quantity = request.POST['quantity']
        percent = request.POST['percent']
        quantity_after_percent = request.POST['quantity_after_percent']
        total_payment = request.POST['total_payment']
        total_tax = request.POST['total_tax']
        total_payment_after_tax = request.POST['total_payment_after_tax']
        if internal_form.is_valid():
            new_item = Internal.objects.create(name=name, destination=destination, net_a_payer=net_a_payer,
                                               quantity=quantity, percent=percent,
                                               quantity_after_percent=quantity_after_percent,
                                               total_payment=total_payment, total_tax=total_tax,
                                               total_payment_after_tax=total_payment_after_tax)

            new_item.save()
            return render(request, template_name='home.html', context={'new_item': new_item})
        else:
            messages.error(request, 'error')

    return render(request, template_name='home.html')
