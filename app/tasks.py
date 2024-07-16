import os
import smtplib
import ssl
import time

from celery import Celery

from app.models import Post, User

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


def send_email(reciever_email, text):
    from dotenv import load_dotenv
    load_dotenv()
    port = 465  # For SSL

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        email = os.getenv("USER_EMAIL")
        password = os.getenv("USER_PASSWORD")
        server.login(email, password)
        server.sendmail(email, [reciever_email, ], text)


@celery.task(name="like_post")
def send_notification_author(title, email):
    text = f"""
        {email} user like to post: {title}
    """
    send_email(reciever_email=email, text=text)
    return True

