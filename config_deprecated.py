RPC_SERVER = {
    'HOST': 'localhost',
    'PORT': 4040
}

RECOMMEND_SERVER = {
    'HOST': 'localhost',
    'PORT': 5050
}

NEWS_CLASSIFIER_SERVER = {
    'HOST': 'localhost',
    'PORT': 6060
}

MONGO = {
    'HOST': 'localhost',
    'PORT': '27017',
    'FIND_AMOUNT': 100,
    'NEWS_DB': 'test',
    'NEWS_COLLECTION': 'news',
    'USER_DB': 'user',
    'USER_PREFERENCES': 'preferences'
}

NEWSAPI = {
    'KEY': '4ed99fbbbee04fdb9b1a8426882682cc',
    'API_BASE': 'https://newsapi.org/v1/articles',
    'DEFAULT_SOURCES': [
        'bbc-news',
        'bbc-sport',
        'bloomberg',
        'business-insider',
        'buzzfeed',
        'cnn',
        'engadget',
        'entertainment-weekly',
        'google-news',
        'ign',
        'the-economist',
        'the-wall-street-journal',
        'the-washington-post',
        'the-verge',
        'the-new-york-times'
    ],
    'DEFUALT_SORT': 'top'
}

QUE_MONITOR_SCRAPER = {
    'URI': 'amqp://uneggxcr:eElS-gADqt1sv8niqv6uzKaiCKT2mnhP@donkey.rmq.cloudamqp.com/uneggxcr',
    'NAME': 'monitor_scraper'
}

QUE_SCRAPER_DEDUPER = {
    'URI': 'amqp://llkcvaiq:98buUaysrg1umBoqAdVRfb9nAngHtsxq@donkey.rmq.cloudamqp.com/llkcvaiq',
    'NAME': 'scraper_deduper'
}

QUE_LOGGER = {
    'URI': 'amqp://siodttgr:2oPzhSjBUG0nZSz9hJnSg5a1b1TUIZN0@donkey.rmq.cloudamqp.com/siodttgr',
    'NAME': 'logger'
}

SLEEP = {
    'MONITOR': 60.0,
    'MONITOR_INCREASE_RATE': 1.5,
    'MONITOR_DECREASE_RATE': 0.5,
    'SCRAPER': 5.0,
    'SCRAPER_INCREASE_RATE': 1.5,
    'SCRAPER_DECREASE_RATE': 0.5,
    'DEDUPER': 5.0,
    'DEDUPER_INCREASE_RATE': 1.5,
    'DEDUPER_DECREASE_RATE': 0.5,
    'LOGGER' : 1.0,
    'LOGGER_INCREASE_RATE': 1.5,
    'LOGGER_DECREASE_RATE': 0.5,
    'MIN': 0.05,
    'MAX': 60.0*30.0
}

PAGINATION = 10

REDIS = {
    'HOST': 'localhost',
    'PORT': 6379,
    'NEWS_EXPIRATION': 3600*24,
    'DIGEST_EXPIRATION': 600
}

TFIDF = {
    'SAME_NEWS_SIMILARITY_THRESHOLD': 0.85
}

TIME_DECAY_MODEL = {
    'ALPHA' : 0.1
}

NEWSCLASSES = {
    "list" : [
        "Colleges & Schools",
        "Environmental",
        "World",
        "Entertainment",
        "Media",
        "Politics & Government",
        "Regional News",
        "Religion",
        "Sports",
        "Technology",
        "Traffic",
        "Weather",
        "Economic & Corp",
        "Advertisements",
        "Crime",
        "Other",
        "Magazine"
    ],
    "map" : {
        '1' : 'Colleges & Schools',
        '2' : 'Environmental',
        '3' : 'World',
        '4' : 'Entertainment',
        '5' : 'Media',
        '6' : 'Politics & Government',
        '7' : 'Regional News',
        '8' : 'Religion',
        '9' : 'Sports',
        '10' : 'Technology',
        '11' : 'Traffic',
        '12' : 'Weather',
        '13' : 'Economic & Corp',
        '14' : 'Advertisements',
        '15' : 'Crime',
        '16' : 'Other',
        '17' : 'Magazine'
    }
}