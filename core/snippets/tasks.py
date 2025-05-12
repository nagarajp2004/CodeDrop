from django.core.mail import send_mail
from .models import CodeSnippet, SnippetTracker
from django.contrib.auth.models import User

def send_daily_snippets():
    for user in User.objects.all():
        snippets = CodeSnippet.objects.filter(user=user).order_by('created_at')
        if not snippets.exists():
            continue

        tracker, _ = SnippetTracker.objects.get_or_create(user=user)
        next_index = (tracker.last_sent_index + 1) % snippets.count()
        snippet = snippets[next_index]

        send_mail(
            subject='Your Daily C++ Snippet',
            message=snippet.code,
            from_email='acharnagaraj01@gmail.com',  # Make sure this is verified with SendGrid
            recipient_list=[user.email],
            fail_silently=False,
        )

        tracker.last_sent_index = next_index
        tracker.save()
