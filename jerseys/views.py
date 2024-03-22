from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Jersey

def index(request):
    return render(request, 'index.html')

class JerseyListView(ListView):
    model = Jersey
    template_name = 'jersey_list.html'

class JerseyDetailView(DetailView):
    model = Jersey
    template_name = 'jersey_detail.html'

class JerseyCreateView(CreateView):
    model = Jersey 
    template_name = 'jersey_form.html'
    fields = ['name', 'description', 'price', 'image']

class JerseyUpdateView(UpdateView):
    model = Jersey 
    template_name = 'jersey_form.html'
    fields = ['name', 'description', 'price', 'image']

class JerseyDeleteView(DeleteView):
    model = Jersey
    template_name = 'jersey_confirm_delete.html'
    success_url = reverse_lazy('jersey_list') 
