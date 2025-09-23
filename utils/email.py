
from django.core.mail import send_mail
from django.conf import settings

def send_email(subject, message, from_email=None, to_email=None):
    if from_email is None:
        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', None)
    to_email = to_email if isinstance(to_email, (list,tuple)) else [to_email,]
    send_mail(subject, message, from_email, to_email)
