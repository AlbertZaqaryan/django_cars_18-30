from django.shortcuts import render
from django.views.generic import ListView
from .models import HomeSlider
# Create your views here.

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        slider = HomeSlider.objects.all()
        return render(request, self.template_name, {'slider':slider})


class AboutListView(ListView):
    template_name = 'about.html'

    def get(self, request):
        slider = HomeSlider.objects.all()
        return render(request, self.template_name, {'slider':slider})

class ContactListView(ListView):
    template_name = 'contact.html'

    def get(self, request):
        slider = HomeSlider.objects.all()
        return render(request, self.template_name, {'slider':slider})


class GalleryListView(ListView):
    template_name = 'gallery.html'

    def get(self, request):
        slider = HomeSlider.objects.all()
        return render(request, self.template_name, {'slider':slider})


class ProductsListView(ListView):
    template_name = 'products.html'

    def get(self, request):
        slider = HomeSlider.objects.all()
        return render(request, self.template_name, {'slider':slider})


class ServicesListView(ListView):
    template_name = 'services.html'

    def get(self, request):
        slider = HomeSlider.objects.all()
        return render(request, self.template_name, {'slider':slider})