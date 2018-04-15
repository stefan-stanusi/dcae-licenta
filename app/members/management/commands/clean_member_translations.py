from django.core.management.base import NoArgsCommand
from django.db.models import Q

from datatrans.utils import find_obsoletes, get_default_language

class Command(NoArgsCommand):
	help = "Deletes obsolete translations."

	def handle_noargs(self, **options):
		all_obsoletes = find_obsoletes().order_by('digest')
		obsoletes = all_obsoletes.filter(Q(edited=True) | Q(language=get_default_language))

		obsoletes.delete()
