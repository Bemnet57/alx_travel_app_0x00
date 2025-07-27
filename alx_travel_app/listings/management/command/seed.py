from django.core.management.base import BaseCommand
from listings.models import Listing
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listing data'

    def handle(self, *args, **kwargs):
        titles = [
            "Cozy Cottage", "Modern Apartment", "Beachfront Bungalow",
            "Mountain Cabin", "City Loft"
        ]

        for i in range(10):
            Listing.objects.create(
                title=random.choice(titles) + f" #{i}",
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                location="Addis Ababa",
                price_per_night=random.randint(50, 200),
                created_at=timezone.now()
            )
        self.stdout.write(self.style.SUCCESS("Database seeded with sample listings."))
