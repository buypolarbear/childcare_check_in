from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm, User
from django.urls import reverse_lazy

from childcare_app.models import Child, Profile



class IndexView(TemplateView):
    template_name = "index.html"


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("index_view")


class ChildCreateView(CreateView):
    model = Child
    success_url = reverse_lazy("index_view")
    fields = ('first_name', 'last_name', 'parent')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        
