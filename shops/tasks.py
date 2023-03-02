from django.core.mail import EmailMessage
from celery import shared_task
from django.contrib.auth import get_user_model
@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
        print('Mikke')

    return 'Done'

