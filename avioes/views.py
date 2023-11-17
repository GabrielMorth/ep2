from django.db.models import fields
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls.base import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Comment, Post, Category
from .forms import CreateAviaoForm, UpdateAviaoForm, CommentForm


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



class CategoriesListView(generic.ListView):
    model = Category
    template_name = 'avioes/categories.html'


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'avioes/category.html'

    
@login_required
def create_comment(request, aviao_id):
    aviao = get_object_or_404(Post, pk=aviao_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # comment_author = form.cleaned_data['autor']
            comment_author = request.user
            comment_text = form.cleaned_data['text']
            comment = Comment(autor=comment_author,
                            text=comment_text,
                            post=aviao)
            comment.save()
            return HttpResponseRedirect(
                reverse('avioes:detail', args=(aviao_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'aviao': aviao}
    return render(request, 'avioes/comment.html', context)


def criar_aviao(request):
    if request.method == 'POST':
        # Obtém os dados do POST (sem validação)
        nome = request.POST.get('nome')
        descricao = request.POST.get('caption')

        # Cria um novo objeto Aviao (sem validação)
        aviao = aviao.objects.create(nome=nome, descricao=descricao)

        # Redireciona para a página de detalhes do novo avião
        return redirect('avioes:detail', aviao_id=aviao.id)
    else:
        return render(request, 'avioes/create.html')