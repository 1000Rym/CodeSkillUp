import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

from AppTwo.models import User

from faker import Faker
faker_gen = Faker()

def add_user(N=5):
    for entry in range(N):
        fake_fname = faker_gen.first_name()
        fake_lname = faker_gen.last_name()
        fake_email = faker_gen.email()

        user = User.objects.get_or_create(first_name = fake_fname,\
                                   last_name = fake_lname,\
                                   email = fake_email)[0]

        print("New User:"+str(user))


if __name__ == '__main__':
    print("Start add users.")
    add_user(10)
    print("Users are added.")
