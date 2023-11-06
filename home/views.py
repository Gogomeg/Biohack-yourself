from django.views.generic import ListView
from hacks.models import Hack


class Index(ListView):
    template_name = 'home/index.html'
    model = Hack
    context_object_name = 'hacks'

    def get_queryset(self):
        return self.model.objects.all()[:3]
