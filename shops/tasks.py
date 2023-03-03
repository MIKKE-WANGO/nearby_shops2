from django.core.mail import EmailMessage
from celery import shared_task
from django.contrib.auth import get_user_model
@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
        print('Mikke')

    return 'Done'


@shared_task(bind=True, name='send-mail')
def send_mail_func(self):
    send_mail_func.delay()
    message = EmailMessage(
        'New quotation',
        'Client details are in the pdf.\nOpen the csv file with excel to easily make changes.',
        'mikemundati@gmail.com',
        ['mikemundati@gmail.com'],
    )
    
    message.send(fail_silently=False)

    return 'Done'