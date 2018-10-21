from django.core.management.base import BaseCommand, CommandError
from CooperApp.models import NewsLetterSubscribed
from CooperApp.utils import get_api_launches
from CommandApp.utils import list_of_launches_this_week
from CooperApp.models import NewsLetterSubscribed
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            start_date = datetime.now().strftime("%Y-%m-%d")
            end_date = (datetime.now() + timedelta(days=7)
                        ).strftime("%Y-%m-%d")
            launches = get_api_launches(start_date, end_date)
            launches_this_week = list_of_launches_this_week(launches)
            if launches_this_week:
                message = ("Hi! We have <strong>Great newses</strong> for you!<br>" +
                           "We have something we think you can be interested in.<br><hr>" +
                           "<h3 style='color:purple;'>Launches of this weak:</h3>" +
                           "<ul>")
                for launch in launches_this_week:
                    message += "<li>" + launch.rocket.name + "</li>"
                message += "</ul><br><hr>"
                for launch in launches_this_week:
                    message += "<h3 style='color:purple;'>" + launch.rocket.name + "</h3>"
                    if launch.rocket.agency != "Unknown":
                        for agency in launch.rocket.agency:
                            message += "<h4>Agency: " + agency.name + "</h4>"
                    else:
                        message += "<h4>Agency: Unknown</h4>"
                    message += "<p>Date: " + launch.date_start + "</p>"
                    if launch.location_name[0]:
                        message += "<p>Location: <strong>" + \
                            launch.location_name[0] + "</strong></p>"
                    else:
                        message += "<p>Location: Unknown</p>"
                    if launch.location_map[0]:
                        message += "<a href=" + \
                            launch.location_map[0] + \
                            ">View location in map</a>"
                    else:
                        message += "<p>Location: Unknown</p>"
                    message += "</ul><br><hr>"
                message += "<h2 style='color:purple;'>The cooper Team <a href='https://cooperappnasa.herokuapp.com/'><img src='https://preview.ibb.co/n82orL/logo-cooper.png' alt='logo-cooper' border='0' height='42' width='42'></a></h2>"
                NewsLetterSubscribed.send_email("This weak launches", message)

        except Exception as e:
            raise CommandError(repr(e))
