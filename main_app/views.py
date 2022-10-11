from django.shortcuts import render
from .models import Listing
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

# listings = [
#   Listing("Jordan 1 Low Bleached Coral", "https://i.ebayimg.com/images/g/xMAAAOSwp2xjPd5S/s-l500.jpg",
#           "Cool shoes."),
#   Listing("Nike Stussy Spiridon Fossil",
#           "https://i.ebayimg.com/images/g/vToAAOSwNPti-wZp/s-l500.jpg", "Also more cool shoes."),
#   Listing("Nike Air Max 1 Patta White Waves", "https://i.ebayimg.com/images/g/pMUAAOSw-DBjJdcu/s-l500.jpg",
#           "Second best Patta collaboration."),
# ]

class ListingsList(TemplateView):
    template_name = "listings_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["artists"] = Listing.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["listings"] = Listing.objects.all()
            context["header"] = f"Searching for {name}"
        return context

class ListingsCreate(CreateView):
    model = Listing
    fields = ['name', 'img', 'ships_from', 'price', 'condition', 'shipping_details', 'delivery', 'returns', 'payments', 'authenticity', 'money_back', 'seller_information']
    template_name = "listings_create.html"
    def get_success_url(self):
        return reverse('listings_detail', kwargs={'pk': self.object.pk})

class ListingsDetail(DetailView):
    model = Listing
    template_name = "listings_detail.html"

class ListingsUpdate(UpdateView):
    model = Listing
    fields = ['name', 'img', 'ships_from', 'price', 'condition', 'shipping_details', 'delivery', 'returns', 'payments', 'authenticity', 'money_back', 'seller_information']
    template_name = "listings_update.html"
    def get_success_url(self):
        return reverse('listings_detail', kwargs={'pk': self.object.pk})

class ListingsDelete(DeleteView):
    model = Listing
    template_name = "listings_delete_confirmation.html"
    success_url = "/listings/"
