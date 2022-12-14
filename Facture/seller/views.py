import logging
from django.http import HttpResponse, JsonResponse
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from seller.models import Internal

from seller.serializers import InternalSerializer

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


#
# def post(request, *args, **kwargs):
#     if request.method == 'POST':
#         name = request.POST['name']
#         destination = request.POST['destination']
#         reference = request.POST['reference']
#         net_a_payer = request.POST['net_a_payer']
#         quantity = request.POST['quantity']
#         percent = request.POST['percent']
#         quantity_after_percent = request.POST['quantity_after_percent']
#         total_payment = request.POST['total_payment']
#         total_tax = request.POST['total_tax']
#         total_payment_after_tax = request.POST['total_payment_after_tax']
#
#         if not quantity_after_percent:
#             quantity_after_percent = int(quantity) * float(percent)
#         if not quantity:
#             quantity = round(float(quantity_after_percent) / float(percent), 2)
#         if not percent:
#             percent = round(float(quantity_after_percent) / int(quantity), 2)
#
#         new_item = Internal(
#             name=name,
#             destination=destination,
#             reference=reference,
#             net_a_payer=net_a_payer,
#             quantity=quantity,
#             percent=percent,
#             quantity_after_percent=quantity_after_percent,
#             total_payment=total_payment,
#             total_tax=total_tax,
#             total_payment_after_tax=total_payment_after_tax,
#         )
#         new_item.save()
#         form = [
#             {
#                 'name': name,
#                 'destination': destination,
#                 'net_a_payer': net_a_payer,
#                 'quantity': quantity,
#                 'percent': percent,
#                 'quantity_after_percent': quantity_after_percent,
#                 'total_payment': total_payment,
#                 'total_tax': total_tax,
#                 'total_payment_after_tax': total_payment_after_tax,
#             }
#         ]
#
#         return ExcelResponse(data=form, output_filename=f'Facture {new_item.created_date}')
#
#
# class InternalCreateData(CreateView):
#     model = Internal
#     template_name = 'create_data.html'
#     fields = [
#         'id',
#         'name',
#         'reference',
#         'destination',
#         'quantity',
#         'percent',
#         'quantity_after_percent',
#         'net_a_payer',
#         'advance_payment',
#         'total_payment',
#         'total_tax',
#         'total_payment_after_tax',
#     ]
#
#     success_message = 'successfully created'
#
#     def get_success_url(self):
#         return reverse('seller:detail', kwargs={'pk': self.object.pk})
#
#     def post(self, request, **kwargs):
#         return post(request)
#
#
# class InternalListData(ListView):
#     model = Internal
#     template_name = 'list_data.html'
#     queryset = model.objects.order_by('-id')
#
#
# class InternalDetailView(DetailView):
#     model = Internal
#     template_name = 'detail.html'
#
#
# class InternalDetailUpdate(UpdateView):
#     model = Internal
#     template_name = 'update.html'
#     fields = [
#         'id',
#         'name',
#         'reference',
#         'destination',
#         'quantity',
#         'percent',
#         'quantity_after_percent',
#         'net_a_payer',
#         'advance_payment',
#         'total_payment',
#         'total_tax',
#         'total_payment_after_tax',
#     ]
#
#     def post(self, request, **kwargs):
#         return post(request)
#
#     def get_success_url(self):
#         return reverse('seller:detail', kwargs={'pk': self.object.pk})
#
#
# class InternalDetailDelete(DeleteView):
#     model = Internal
#     template_name = 'delete.html'
#     success_url = '/'
