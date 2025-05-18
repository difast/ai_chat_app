from celery import Celery
from app.services.ai_moderation import AIModerator
import os

celery = Celery(__name__)
celery.conf.broker_url = os.getenv("CELERY_BROKER_URL")

@celery.task
def process_message_async(message_id: int):
    pass