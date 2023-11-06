from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Hack
from .forms import HackForm


class AddHack(LoginRequiredMixin, CreateView):
    """Add hack view"""

    template_name = "hacks/add_hack.html"
    model = Hack
    form_class = HackForm
    success_url = "/hacks/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddHack, self).form_valid(form)


class Hacks(ListView):
    """View all hacks"""

    template_name = "hacks/hacks.html"
    model = Hack
    context_object_name = "hacks"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get("q")
        if query:
            hacks = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(content__icontains=query) |
                Q(hack_type__icontains=query)
            )
        else:
            hacks = self.model.objects.all()
        return hacks


class HackDetail(DetailView):
    """View a single health hack"""

    template_name = "hacks/hack_detail.html"
    model = Hack
    context_object_name = "hack"


class DeleteHack(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a health hack"""
    model = Hack
    success_url = '/hacks/'

    def test_func(self):
        return self.request.user == self.get_object().user


class EditHack(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a health hack"""
    template_name = 'hacks/edit_hack.html'
    model = Hack
    form_class = HackForm
    success_url = '/hacks/'

    def test_func(self):
        return self.request.user == self.get_object().user
