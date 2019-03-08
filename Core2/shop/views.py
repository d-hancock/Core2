from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from bootstrap_modal_forms.mixins import PassRequestMixin
from shop.models import Shop
from shop.forms import ShopForm
from django.contrib.auth.models import User


class ShopListView(LoginRequiredMixin, ListView):
    model = Shop

    def get_queryset(self):
        return Shop.objects.all().filter(profile=User.profile)


class ShopCreateView(PassRequestMixin, SuccessMessageMixin,
                     CreateView):
    template_name = 'shop/create_shop.html'
    form_class = ShopForm
    success_message = 'Success: Shop was created.'
    success_url = reverse_lazy('shop-list')
