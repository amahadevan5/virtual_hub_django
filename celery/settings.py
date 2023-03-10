from celery import Celery
from datetime import timedelta
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'mydatabase'),
        'USER': os.environ.get('POSTGRES_USER', 'mydatabaseuser'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'mypassword'),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}


# Create a celery instance
app = Celery('virtual_hub_django')


# Set up the broker and backend settings
app.conf.update(
    broker_url='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/1'
)

# Set up the schedule for periodic tasks
app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'celery_app.tasks.add_numbers',
        'schedule': timedelta(seconds=10), 
        'args': (1, 2)
    }
}

# Set up the task routes
app.conf.task_routes = {
    'celery_app.tasks.add_numbers': {'queue': 'addition_queue'},
    'celery_app.tasks.multiply_numbers': {'queue': 'multiplication_queue'}
}

# Set up the result expiration time
app.conf.result_expires = 3600  # 1 hour (in seconds)
