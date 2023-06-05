from django.core.management.base import BaseCommand, CommandError
from yelp.models import Restaurant, Tag

# def get_right_tag(price):
#     if len(price) == 1:
#         tag = "cheap"
#     elif len(price) == 2:
#         tag = "moderate"
#     elif len(price) == 3:
#         tag = "expensive"
#     elif price == "No info":
#         tag = ""
#     return tag

class Command(BaseCommand):
    help = "Get data from Yelp API"

    def handle(self, *args, **kwargs):
        objects = Restaurant.objects.all()
        categories = set([r.category for r in objects])
        prices = set([r.price for r in objects])

        for cat in categories:
            obj, created = Tag.objects.get_or_create(
                tag_field = cat
            )
            print(obj, created)
        
        # for price in prices:
        #     tag = get_right_tag(price)
        #     obj, created = Tag.objects.get_or_create(
        #         tag_field = tag
        #     )