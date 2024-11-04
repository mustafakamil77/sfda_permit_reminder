#tasks.py
from celery import shared_task
from django.core.mail import send_mail
from project import settings
from datetime import datetime
from .models import SdfaPermit
from django.utils import timezone



@shared_task(bind=True)

def check_permit_expiry(self):
    permits = SdfaPermit.objects.all()
    for permit in permits:
        expiry_date = permit.expiry_date
        tz = timezone.get_default_timezone()
        expiry_date = expiry_date.astimezone(tz).replace(tzinfo=None)
        today = datetime.now()
        days_until_expiry = (expiry_date - today).days
        if days_until_expiry < 20 and permit.notify != '1':
            subject = f'{permit.company_name} Permit Expiring Soon'
            message = f'Your permit for {permit.company_name} is expiring in 20 days.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['mustafakamil.77@gmail.com','waleed@fitkar.com.sa']
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            permit.notify = '1'
            permit.save()


