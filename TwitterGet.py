#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 13.10.2018 21:29
:Licence GNUv3
Part of DataScienceProject

"""

from TwitterSearch import *
from Config import config


def get_from_twitter(keywords, language, count=100, longitude=None, latitude=None, radius=None):
    tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
    tso.set_keywords(keywords)  # let's define all words we would like to have a look for
    tso.set_language(language)  # we want to see English tweets only
    tso.set_include_entities(False)  # and don't give us all those entity information
    if longitude is not None and latitude is not None and radius is not None:
        tso.set_geocode(latitude, longitude, radius)

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key=config['Twitter']['consumer_key'],
        consumer_secret=config['Twitter']['consumer_secret'],
        access_token=config['Twitter']['access_token'],
        access_token_secret=config['Twitter']['access_token_secret'],
     )

    # this is where the fun actually starts :)
    i = 0
    for tweet in ts.search_tweets_iterable(tso):
        yield tweet['text']
        i += 1
        if i == count:
            break
