import os
import django
from faker import Faker

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pagination.settings")  # Corrected here
django.setup()

from myapp.models import BlogPost

fake = Faker()

for i in range(100):  # Create 100 dummy blog posts
    BlogPost.objects.create(
        title=fake.sentence(),
        content=fake.paragraph(),
    )
print("Successfully populated the database with 100 blog posts")