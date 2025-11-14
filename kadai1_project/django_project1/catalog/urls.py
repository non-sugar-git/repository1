# あなたが実装します（catalog 用 URL を定義）
from django.urls import path
from .views import (
    CategoryList,
    CategoryDetail,
    entry_search,
    EntryPublishedList,
    EntryUnpublishedList,
    entry_toggle,
)

app_name = "catalog"

urlpatterns = [
    path("categories/", CategoryList.as_view(), name="category_list"),
    path("categories/<slug:slug>/", CategoryDetail.as_view(), name="category_detail"),
    path("entries/search/", entry_search, name="entry_search"),
    path("entries/published/", EntryPublishedList.as_view(), name="entry_published_list"),
    path("entries/unpublished/", EntryUnpublishedList.as_view(), name="entry_unpublished_list"),
    path("entries/<int:pk>/toggle/", entry_toggle, name="entry_toggle"),
]