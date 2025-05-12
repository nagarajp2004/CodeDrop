from django.core.mail import send_mail
from django.http import HttpResponse

# Define a view to test sending the email
def test_send_email(request):
    send_mail(
        'Test Subject',
        'This is a test email sent from Django using SendGrid.',
        'acharnagaraj01@gmail.com',  # From email (your verified SendGrid email)
        ['1rn22ad026.namavenkatatharun@rnsit.ac.in'],  # To email
        fail_silently=False,
    )
    return HttpResponse("Test email sent successfully!")



