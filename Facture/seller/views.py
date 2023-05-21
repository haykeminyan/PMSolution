import logging
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, filters
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from seller.models import Internal

from seller.serializers import InternalSerializer
from django_filters.rest_framework import DjangoFilterBackend

logger = logging.getLogger('django')

logger.info('here goes your message')


class InternalListView(APIView):
    def get(self, request):
        snippets = Internal.objects.all()
        serializer = InternalSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        if not data.get('quantity_after_percent'):
            data['quantity_after_percent'] = int(data['quantity']) * float(data['percent'])
        if not data.get('quantity'):
            data['quantity'] = round(
                float(data['quantity_after_percent']) / float(data['percent']), 2
            )
        if not data.get('percent'):
            data['percent'] = round(
                float(data['quantity_after_percent']) / int(data['quantity']), 2
            )

        serializer = InternalSerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        except ValidationError:
            return JsonResponse(serializer.errors, status=400)


class InternalDetailListView(APIView):
    def get_facture(self, pk):
        try:
            facture = Internal.objects.get(pk=pk)
        except Internal.DoesNotExist:
            raise NotFound(f'Facture Numero {pk} is not found')
        return facture

    def get(self, request, pk):
        serializer = InternalSerializer(self.get_facture(pk))
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        data = JSONParser().parse(request)
        serializer = InternalSerializer(self.get_facture(pk), data=data)

        if not data.get('quantity_after_percent'):
            data['quantity_after_percent'] = int(data['quantity']) * float(data['percent'])
        if not data.get('quantity'):
            data['quantity'] = round(
                float(data['quantity_after_percent']) / float(data['percent']), 2
            )
        if not data.get('percent'):
            data['percent'] = round(
                float(data['quantity_after_percent']) / int(data['quantity']), 2
            )

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        except ValidationError:
            return JsonResponse(serializer.errors, status=400)

    def delete(self, request, pk):
        facture = self.get_facture(pk)
        facture.delete()
        return HttpResponse(status=204)


class InternalDetailListFilterView(generics.ListAPIView):
    queryset = Internal.objects.all()
    serializer_class = InternalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

    def get(self, request, *args, **kwargs):
        return Response(self.list(request, *args, **kwargs).data['results'])
