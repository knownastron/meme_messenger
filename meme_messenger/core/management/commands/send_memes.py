from django.core.management.base import BaseCommand
from core.models import PhoneNumber
from core.utils.imgur import imgurObject
# from core.utils.twilio import twilioObject
import random

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        all_nums = PhoneNumber.objects.all() #gets all registered phone numbers in the db
        meme_urls = imgurObject().getURLs() #gets all the urls from imgur album
        print(type(meme_urls[0]))
        image_num = random.randint(0, len(meme_urls) - 1) #picks a random URL from the meme_urls
        twilioObj = twilioObject()

        for num in all_nums:
            twilioObj.send_meme(num, meme_urls[image_num].link)
