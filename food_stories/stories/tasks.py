import time
from celery import shared_task

@shared_task
def dump_database():
    print('ise dusdu')
    time.sleep(100)
    print('dayandi')
    return True
