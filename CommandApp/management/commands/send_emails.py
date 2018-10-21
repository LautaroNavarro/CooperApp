from django.core.management.base import BaseCommand, CommandError
from CooperApp.models import NewsLetterSubscribed
from CooperApp.utils import get_api_launches
from CommandApp.utils import list_of_launches_this_week
from CooperApp.models import NewsLetterSubscribed


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            launches = get_api_launches("", "")
            launches_this_week = list_of_launches_this_week(launches)
            if launches_this_week:
                message = "Launches of this weak:\n"
                for launch in launches_this_week:
                    message += "* " + launch.rocket.name + "\n"
                NewsLetterSubscribed.send_email("This weak launches", message)

        except Exception as e:
            raise CommandError(repr(e))
