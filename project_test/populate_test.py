import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project_test.settings')

import django
django.setup()

import random
from faker import Faker
from app_project_test.models import Category, Brand, Webpage, AccessRecord, Employee
 
# django setup

 
# Fake Pop Script
fakegen = Faker()
 
# Random Category
random_category = ['Amazon', 'Alibaba', 'Udemy', 'Security', 'Linkedin']
 
# Random Brand
random_brand = ['Apple', 'Nokia', 'OnePlus', 'RealMe', 'Vivo', 'OppoE']
 
# Call Category Model
def add_category():
    cate = Category.objects.get_or_create(topic=random.choice(random_category))[0]
    cate.save()
    return cate
 
# Call Brand Model
def add_brand():
    bran = Brand.objects.get_or_create(brand=random.choice(random_brand))[0]
    bran.save()
    return bran
 
# Rest of Models
def populate(N=5):
    for entry in range(N):
        print("inside for loop")

        # Call add_category function
        cat = add_category()
 
        # Call add_brand function
        bra = add_brand()
 
        # Add Fake Data for each Models
        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()
        #fake_person = fakegen.person()
        print("printing generated fake data")
        print(fake_url)
        print(fake_date)
        print(fake_name)
 
        # Fake Script for Webpage Model
        webpg = Webpage.objects.get_or_create(
            category=cat, brand=bra, name=fake_name, url=fake_url)[0]
 
        # Fake Script for Access Record
        acc_rec = AccessRecord.objects.get_or_create(
            name=webpg, brand=bra, date=fake_date)[0]
        print("succesfully created records")

 
 
# Initialize the main file
if __name__ == '__main__':
    print('Run Script')
    populate(20)
    print('Script run Successfully')