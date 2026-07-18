from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Paragraph, MediaAttachment
from .forms import ArticleForm, ParagraphFormSet, MediaFormSet


def landing(request):
    articles = Article.objects.filter(is_published=True)
    newest = articles.first()
    rest = articles[1:]
    return render(request, 'blog/landing.html', {
        'newest': newest,
        'articles': rest,
    })


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, is_published=True)
    return render(request, 'blog/article_detail.html', {'article': article})


@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        paragraph_formset = ParagraphFormSet(request.POST, request.FILES)
        media_formset = MediaFormSet(request.POST, request.FILES)
        if form.is_valid() and paragraph_formset.is_valid() and media_formset.is_valid():
            article = form.save()
            paragraph_formset.instance = article
            paragraph_formset.save()
            media_formset.instance = article
            media_formset.save()
            return redirect('blog:article_detail', pk=article.pk)
    else:
        form = ArticleForm()
        paragraph_formset = ParagraphFormSet()
        media_formset = MediaFormSet()
    return render(request, 'blog/create_article.html', {
        'form': form,
        'paragraph_formset': paragraph_formset,
        'media_formset': media_formset,
    })
