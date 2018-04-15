from django.core.management.base import NoArgsCommand

from courses.models import Course

class Command(NoArgsCommand):
	help = "Resets the views for courses."

	def handle_noargs(self, **options):
		Course.objects.all().filter(public=True).update(views=0)
