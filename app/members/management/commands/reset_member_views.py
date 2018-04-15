from django.core.management.base import NoArgsCommand

from members.models import Member

class Command(NoArgsCommand):
	help = "Resets the views for members' profiles."

	def handle_noargs(self, **options):
		Member.objects.active().update(views=0)
