from django.db.models import fields
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse_lazy
from django.views import generic

class AviaoDetailView(generic.DetailView):
    model = Post
    template_name = 'avioes/detail.html'


class AviaoListView(generic.ListView):
    model = Post
    template_name = 'avioes/index.html'


class AviaoCreateView(generic.CreateView):
    model = Post
    fields = '__all__'
    template_name = 'avioes/create.html'
    def get_success_url(self):
        return reverse('avioes:detail', args=( self.object.id,))


class AviaoUpdateView(generic.UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'avioes/update.html'
    def get_success_url(self):
        return reverse('avioes:detail', args=( self.object.id,))


class AviaoDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('avioes:index')
    template_name = 'avioes/delete.html'