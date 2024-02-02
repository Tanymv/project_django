from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from article.models import Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'body',)
    success_url =reverse_lazy('article:list')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body',)
    # success_url =reverse_lazy('article:list')


    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article:view', args=[self.kwargs.get('pk')])


class  ArticleListView(ListView):
    model = Article

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset



class  ArticleDetailView(DetailView):
    model = Article


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article:list')



def published(request, pk):
    article_item = get_object_or_404(Article, pk=pk)
    if article_item.is_published:
        article_item.is_published = False
    else:
        article_item.is_published = True
    article_item.save()
    return redirect(reverse('article:list'))
