""""
Celery menu task to send employees today menu
"""
import datetime

from celery.schedules import crontab
from celery.utils.log import get_task_logger
from django.conf import settings
from pytz import timezone

from lunch.models import Menu
from lunch.utils import slack
from backend_test.celery import app

logger = get_task_logger(__name__)


EMPLOYEES_TIME_ZONE = getattr(settings, "EMPLOYEES_TIME_ZONE",
                              "America/Santiago")
LOCAL_SITE = getattr(settings, "LOCAL_SITE")
SEND_HOUR = getattr(settings, "MENU_CREATE_HOUR")

app.conf.update(timezone=EMPLOYEES_TIME_ZONE)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    Executes every Monday morning at 11:00 a.m. Santiago Chile TimeZone
    :param sender:
    """
    sender.add_periodic_task(
        crontab(hour=SEND_HOUR, minute=00, day_of_week=7),
        send_menu_employees().s(True),
    )


@app.task(autoretry_for=(Exception,), retry_backoff=2)
def send_menu_employees(resend=False):
    """
    Send messages to employees at conf hour by celery
    :return:
    """
    menu_date = datetime.datetime.now(timezone(EMPLOYEES_TIME_ZONE)).today()
    if not Menu.objects.filter(date=menu_date, active=True,
                               sent=resend).exists():
        logger.info('No hay menu para el dia de hoy para enviar')
        return False
    menu = Menu.objects.get(date=menu_date, active=True, sent=False)
    url = '{}{}/'.format(LOCAL_SITE, menu.unique_id)
    message = f""" {menu.message} : {url} """
    slack.send_message_slack(message)
    menu.sent = True
    menu.save()
    return True
