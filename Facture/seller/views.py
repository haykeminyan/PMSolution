from io import BytesIO
from openpyxl import Workbook
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from openpyxl.styles import Alignment, Font
from rest_framework.exceptions import NotFound
from rest_framework.parsers import JSONParser

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from seller.serializer import InternalSerializer
from seller.models import Internal


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

    def export_data_to_excel(self, request, pk):
        excelfile = BytesIO()
        workbook = Workbook()
        workbook.remove(workbook.active)
        workbook.remove(workbook.active)
        worksheet = workbook.create_sheet(title='oppa', index=1)

        coin_queryset = Internal.objects.get(pk=pk)
        columns = ['id', 'name', 'created_date', 'updated_date',
                  'reference', 'destination', 'quantity', 'percent', 'quantity_after_percent',
                  'net_a_payer', 'advance_payment', 'total_payment', 'total_tax',
                  'total_payment_after_tax']

        row_num = 1

        # Assign the titles for each cell of the header
        for col_num, column_title in enumerate(columns, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = column_title
            cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
            cell.font = Font(bold=True)
        # Iterate through all coins
        for _, field in enumerate(coin_queryset, 1):
            row_num += 1

            # Define the data for each cell in the row
            row = [
                field.id,
                field.name,
                field.created_time
            ]

            # Assign the data for each cell of the row
            for col_num, cell_value in enumerate(row, 1):
                cell = worksheet.cell(row=row_num, column=col_num)
                cell.value = cell_value
        workbook.save(excelfile)
        return excelfile
