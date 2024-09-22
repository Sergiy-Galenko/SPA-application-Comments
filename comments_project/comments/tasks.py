from celery import shared_task

@shared_task
def send_email_task():
    # Наприклад, надсилаємо листа у фоновому режимі
    print("Email sent!")
