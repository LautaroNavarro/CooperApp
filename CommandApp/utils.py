from CooperApp.models import *
from datetime import datetime


def list_of_launches_this_week(launches):
    launches_of_week = []
    for launche in launches:
        date_start = datetime.strptime(
            launche.date_start, '%B %d, %Y %H:%M:%S UTC')
        time = date_start - datetime.now()
        if time.days <= 7:
            launches_of_week.append(launche)
    return launches_of_week
