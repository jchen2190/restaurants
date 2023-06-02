from django.core.management.base import BaseCommand, CommandError
from yelp.models import Restaurant
import requests
from decouple import config

API_KEY = config("API_KEY")

def callAPI():
    headers = {'Authorization': f'Bearer {API_KEY}'}
    params = {'term': 'restaurant',
                'location': 'New York City',
                'limit' : 50
            }
    URL = 'https://api.yelp.com/v3/businesses/search'
    res = requests.get(URL, params=params, headers=headers)
    data = res.json()
    data = data['businesses']
    return data

class Command(BaseCommand):
    help = "Get data from Yelp API"

    def handle(self, *args, **kwargs):
        d = callAPI()
        for business in d:
            obj, created = Restaurant.objects.get_or_create(
                    name = business.get('name', 'No info'),
                    address1 = business.get('location', 'No info')['address1'],
                    address2 = business.get('location',"")['address2'],
                    address3 = business.get('location',"")['address3'],
                    city = business.get('location', 'No info')['city'],
                    zip_code = business.get('location', 'No info')['zip_code'],
                    country = business.get('location', 'No info')['country'],
                    state = business.get('location', 'No info')['state'],
                    image_url = business.get('image_url'),
                    category = business.get('categories', 'No Category')[0]['alias'],
                    review_count =  business.get('review_count', 'No reviews'),
                    price = business.get('price', 'No info'),
                    rating = float(business.get('rating')),
                    phone = business.get('phone', 'No info')
                )
            print(obj, created) # obj = name of restaurant (str from model),  created = true/false