import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from django_seed import Seed
from store.models import Author, Book

seeder = Seed.seeder()

seeder.add_entity(Author, 20)
seeder.add_entity(Book, 200)

inserted_pks = seeder.execute()
