from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, User
from django.urls import reverse_lazy, reverse
from random import choice
from string import digits
from django.http import HttpResponseRedirect
from datetime import datetime


from childcare_app.models import Child, Profile


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_codes"] = Child.objects.all()
        return context

    def post(self, request):
        code = request.POST["code"]
        child = Child.objects.get(code=code)
        return HttpResponseRedirect(reverse("child_update_view", args=[child.id]))


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
        instance.code = ""
        for i in range(4):
            instance.code += choice(digits)
        return super().form_valid(form)


class ChildUpdateView(UpdateView):
    model = Child
    fields = ('on_site',)
    success_url = reverse_lazy("index_view")

    def form_valid(self, form):
        instance = form.save(commit=False)
        if instance.on_site:
            instance.check_in = datetime.now()
        else:
            instance.check_out = datetime.now()
        return super().form_valid(form)
