# あなたが実装します（List/Detail/Search/Published/Unpublished/Toggle）
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Category, Entry

class CategoryList(ListView):
    model = Category
    context_object_name = "category_list"
    template_name = "catalog/category_list.html"

class CategoryDetail(DetailView):
    model = Category
    slug_field = "slug"
    slug_url_kwarg = "slug"
    template_name = "catalog/category_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["entries"] = Entry.objects.filter(category=self.object, is_published=True).order_by("-id")
        return context
    
def entry_search(request):
    q = request.GET.get("q", "")
    entries = Entry.objects.all()
    if q:
        entries = entries.filter(title__icontains=q)
    entries = entries.order_by("-id")
    context = {"q": q, "entries": entries}
    return render(request, "catalog/entry_search.html", context)

class EntryPublishedList(ListView):
    model = Entry
    template_name = "catalog/entry_published_list.html"
    context_object_name = "entries"

    def get_queryset(self):
        return Entry.objects.filter(is_published=True).order_by("-id")
    
class EntryUnpublishedList(ListView):
    model = Entry
    template_name = "catalog/entry_unpublished_list.html"
    context_object_name = "entries"

    def get_queryset(self):
        return Entry.objects.filter(is_published=False).order_by("-id")
    
@require_POST
def entry_toggle(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    entry.is_published = not entry.is_published
    entry.save()
    if entry.is_published:
        return redirect("catalog:entry_published_list")
    else:
        return redirect("catalog:entry_unpublished_list")