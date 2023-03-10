from .settings import *

# Override the broker URL for local development
CELERY_BROKER_URL = 'pyamqp://your_database_username:your_database_password@localhost:5432/your_database_name'

# Add any custom task modules
CELERY_IMPORTS = ('celery.tasks',)

# Configure the task result backend
CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'

# Set the time zone for task scheduling
CELERY_TIMEZONE = 'America/New_York'

# Disable task eager mode for production environment
CELERY_TASK_ALWAYS_EAGER = False

# Set task concurrency settings
CELERYD_CONCURRENCY = 4
CELERYD_MAX_TASKS_PER_CHILD = 10
