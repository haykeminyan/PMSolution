from io import BytesIO

from django.contrib import messages
from django.shortcuts import render, redirect
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
        internal_form = InternalForm(request.POST, request.FILES)
        if internal_form.is_valid():
            internal_form.save()
            messages.success(request, 'Yalla habibi')
        else:
            messages.error(request, 'Poshel v jopy Armen')

        return redirect("seller:home")

    internal_form = InternalForm()
    internals = Internal.objects.all()
    return render(request=request, template_name='home.html', context={'internals': internals, 'internal_form':internal_form})