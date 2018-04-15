from django.core.management.base import NoArgsCommand

from labs.models import Laboratory

class Command(NoArgsCommand):
	help = "Resets the views for laboratories."

	def handle_noargs(self, **options):
		Laboratory.objects.all().filter(public=True).update(views=0)
