from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse_lazy
from django.views import generic
from .models import FitnessPlan

def home(request):
    plans = FitnessPlan.objects
    return render(request, 'plans/home.html', {'plans':plans})

def plan(request,pk):
    plan = get_object_or_404(FitnessPlan, pk=pk)
    if plan.premium :
        return redirect('join')
    else:
        return render(request, 'plans/plan.html', {'plan':plan})



    

    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid
