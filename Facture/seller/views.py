from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormView, CreateView
from excel_response import ExcelResponse
import logging
from seller.models import Internal

logger = logging.getLogger(__name__)


class InternalCreateData(CreateView):
    model = Internal
    template_name = 'create_data.html'
    fields = ['id', 'name',
              'reference', 'destination', 'quantity', 'percent', 'quantity_after_percent',
              'net_a_payer', 'advance_payment', 'total_payment', 'total_tax',
              'total_payment_after_tax']

    def get_success_url(self):
        return reverse('seller:detail', kwargs={'pk': self.object.pk})


class InternalAllData(ListView):
    model = Internal
    template_name = 'all_data.html'


class InternalDetailView(DetailView):
    model = Internal
    template_name = 'detail.html'


class InternalDetailUpdate(UpdateView):
    model = Internal
    template_name = 'update.html'
    fields = ['id', 'name',
              'reference', 'destination', 'quantity', 'percent', 'quantity_after_percent',
              'net_a_payer', 'advance_payment', 'total_payment', 'total_tax',
              'total_payment_after_tax']
    success_url = "/"


class InternalDetailDelete(DeleteView):
    model = Internal
    template_name = 'delete.html'
    success_url = "/"


#
#     def valuate(self, request):
#         if request.method == 'POST':
#             # internal_form = InternalForm(request.POST)
#             name = request.POST['name']
#             destination = request.POST['destination']
#             net_a_payer = request.POST['net_a_payer']
#             quantity = int(request.POST['quantity'])
#             percent = int(request.POST['percent'])
#             quantity_after_percent = request.POST['quantity_after_percent']
#             total_payment = request.POST['total_payment']
#             total_tax = request.POST['total_tax']
#             total_payment_after_tax = request.POST['total_payment_after_tax']
#             # if internal_form.is_valid():
#             new_item = Internal(name=name, destination=destination, net_a_payer=net_a_payer,
#                                 quantity=quantity, percent=percent,
#                                 quantity_after_percent=quantity_after_percent,
#                                 total_payment=total_payment, total_tax=total_tax,
#                                 total_payment_after_tax=total_payment_after_tax)
#             new_item.save()
#             form = [{'name': name, 'destination': destination, 'net_a_payer': net_a_payer,
#                      'quantity': quantity, 'percent': percent, 'quantity_after_percent': quantity_after_percent,
#                      'total_payment': total_payment, 'total_tax': total_tax,
#                      'total_payment_after_tax': total_payment_after_tax}]
#
#             return ExcelResponse(data=form, output_filename=f'Facture {new_item.created_date}')
#
# logger.info('!!!')
#
#
#
