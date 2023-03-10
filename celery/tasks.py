from celery import shared_task
from time import sleep

@shared_task
def add(x, y):
    sleep(5)
    return x + y

##
# this is a placeholder to be changed later. above is an example of what a task function looks like
#