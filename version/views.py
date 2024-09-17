from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from version.forms import Version, VersionForm


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm


class VersionListView(ListView):
    model = Version

    def get_context_data(*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_active'] = "Version active"
        return context

# class VersionDetailView(DetailView):
#     model = Version
#
#
# class VersionUpdateView(UpdateView):
#     model = Version
#     fields = "__all__"
#
#
# class VersionDeleteView(DeleteView):
#     model = Version
