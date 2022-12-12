from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from excel_response import ExcelResponse
import logging
from seller.models import Internal

logger = logging.getLogger('django')

logger.info('here goes your message')


def post(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST['name']
        destination = request.POST['destination']
        reference = request.POST['reference']
        net_a_payer = request.POST['net_a_payer']
        quantity = request.POST['quantity']
        percent = request.POST['percent']
        quantity_after_percent = request.POST['quantity_after_percent']
        total_payment = request.POST['total_payment']
        total_tax = request.POST['total_tax']
        total_payment_after_tax = request.POST['total_payment_after_tax']

        if not quantity_after_percent:
            quantity_after_percent = int(quantity) * float(percent)
        if not quantity:
            quantity = round(float(quantity_after_percent) / float(percent), 2)
        if not percent:
            percent = round(float(quantity_after_percent) / int(quantity), 2)

        new_item = Internal(
            name=name,
            destination=destination,
            reference=reference,
            net_a_payer=net_a_payer,
            quantity=quantity,
            percent=percent,
            quantity_after_percent=quantity_after_percent,
            total_payment=total_payment,
            total_tax=total_tax,
            total_payment_after_tax=total_payment_after_tax,
        )
        new_item.save()
        form = [
            {
                'name': name,
                'destination': destination,
                'net_a_payer': net_a_payer,
                'quantity': quantity,
                'percent': percent,
                'quantity_after_percent': quantity_after_percent,
                'total_payment': total_payment,
                'total_tax': total_tax,
                'total_payment_after_tax': total_payment_after_tax,
            }
        ]

        return ExcelResponse(data=form, output_filename=f'Facture {new_item.created_date}')


class InternalCreateData(CreateView):
    model = Internal
    template_name = 'create_data.html'
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

    success_message = 'successfully created'

    def get_success_url(self):
        return reverse('seller:detail', kwargs={'pk': self.object.pk})

    def post(self, request, **kwargs):
        return post(request)


class InternalListData(ListView):
    model = Internal
    template_name = 'list_data.html'
    queryset = model.objects.order_by('-id')


class InternalDetailView(DetailView):
    model = Internal
    template_name = 'detail.html'


class InternalDetailUpdate(UpdateView):
    model = Internal
    template_name = 'update.html'
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

    def post(self, request, **kwargs):
        return post(request)

    def get_success_url(self):
        return reverse('seller:detail', kwargs={'pk': self.object.pk})


class InternalDetailDelete(DeleteView):
    model = Internal
    template_name = 'delete.html'
    success_url = '/'
