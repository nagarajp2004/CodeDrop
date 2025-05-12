from django.http import HttpResponse
from .tasks import send_daily_snippets

def trigger_snippet_email(request):
    send_daily_snippets()
    return HttpResponse("Snippet emails sent successfully!")
