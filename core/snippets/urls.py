from django.urls import path
from . import views

urlpatterns = [
    path('create_snippet/', views.create_snippet),
    path('list_snippets/', views.list_snippets),
    path('delete_snippet/<int:snippet_id>/', views.delete_snippet),
]
