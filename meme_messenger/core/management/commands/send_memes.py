from django.core.management.base import BaseCommand
from frontend.models import PhoneNumber

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        all_nums = PhoneNumber.objects.all()
        for num in all_nums:
            print(num)