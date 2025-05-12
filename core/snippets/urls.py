from django.urls import path
from .views import trigger_snippet_email

urlpatterns = [
    path('send-snippets/', trigger_snippet_email, name='send_snippets'),
]
