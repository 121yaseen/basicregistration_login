from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, RedirectView
from registration.forms import *
from registration.models import User


class Register(CreateView):
    model = User
    form_class = Registration
    template_name = 'registration/registration.html'
    success_url = '/'

    extra_context = {
        'title': 'Register'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            return redirect('registration:login')
        else:
            return render(request, 'registration/registration.html', {'form': form})
