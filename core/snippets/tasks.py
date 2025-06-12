from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import CodeSnippet, SnippetTracker

@shared_task
def send_next_snippet_email(user_id):
    try:
        user = User.objects.get(id=user_id)
        snippets = CodeSnippet.objects.filter(user=user).order_by('created_at')
        tracker, _ = SnippetTracker.objects.get_or_create(user=user)

        if not snippets:
            return

        next_index = (tracker.last_sent_index + 1) % len(snippets)
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
    except Exception as e:
        print(f"Error sending snippet email: {e}")

@shared_task
def send_next_snippet_email_to_all_users():
    for user in User.objects.all():
        send_next_snippet_email.delay(user.id)
