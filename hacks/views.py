from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView
)

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

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

