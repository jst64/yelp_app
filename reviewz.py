from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

auth = Oauth1Authenticator(
    consumer_key=os.environ['yconsumer_key'],
    consumer_secret=os.environ['yconsumer_secret'],
    token=os.environ['ytoken'],
    token_secret=os.environ['ytoken_secret']
)

client = Client(auth)

def lookup(search_term,city):
    auth = Oauth1Authenticator(
        consumer_key=os.environ['yconsumer_key'],
        consumer_secret=os.environ['yconsumer_secret'],
        token=os.environ['ytoken'],
        token_secret=os.environ['ytoken_secret']
    )

    client = Client(auth)
    params = {
    'term': search_term,
    'lang': 'en'}
    response=client.search(city, **params)
    businesses = []
    for business in response.businesses:  
        #print([business.name, business.rating, business.phone])
        businesses.append({"name":business.name, 
            "rating": business.rating,
            "phone": business.phone})
    return businesses


