from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Slider, Service, Team, Faq, Gallery
from django.views.generic import ListView, DetailView, TemplateView


class HomeView(ListView):
    template_name = 'myweb/index.html'
    queryset = Service.objects.all()
    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['sliders'] = Slider.objects.all()
        context['experts'] = Team.objects.all()
        return context


class ServiceListView(ListView):
    queryset = Service.objects.all()
    template_name = "myweb/services.html"


class ServiceDetailView(DetailView):
    queryset = Service.objects.all()
    template_name = "myweb/service_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        return context


class TeamListView(ListView):
    template_name = 'myweb/team.html'
    queryset = Team.objects.all()
    paginate_by = 8


class TeamDetailView(DetailView):
    template_name = 'myweb/team-details.html'
    queryset = Team.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teams"] = Team.objects.all()
        return context


class FaqListView(ListView):
    template_name = 'myweb/faqs.html'
    queryset = Faq.objects.all()


class GalleryListView(ListView):
    template_name = 'myweb/gallery.html'
    queryset = Gallery.objects.all()
    paginate_by = 9


class ContactView(TemplateView):
    template_name = "myweb/contact.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if subject == '':
            subject = "Samsi Networks Contact"

        if name and message and email and phone:
            send_mail(
                subject+"-"+phone,
                message,
                email,
                ['asimiyu@samsinetworks.com'],
                fail_silently=False,
            )
            messages.success(request, " Email hasbeen sent successfully...")

        return redirect('contact')
