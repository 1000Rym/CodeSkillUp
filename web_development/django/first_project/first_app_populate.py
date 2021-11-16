
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fake_gen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def add_webpage(N=5):
    for entry in range(N):
        # get the topioc for the entry.
        topic = add_topic()

        # create the fake data for the entry.
        fake_url = fake_gen.url()
        fake_company_name = fake_gen.company()
        webpage = Webpage.objects.get_or_create(topic = topic, url = fake_url, name = fake_company_name)[0]


        # create fake acess record
        fake_date = fake_gen.date()
        access_record = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]

if __name__ == '__main__':
    print("populating script!")
    add_webpage(20)
    print("populating done!")
