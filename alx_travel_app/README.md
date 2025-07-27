# ALX Travel App 0x00

This project is part of the ALX Backend program and focuses on setting up core database models, serializers, and a custom database seeding command for a travel booking application.

## 📁 Project Structure

This app includes:

- `Listing` model: Represents properties available for booking.
- `Booking` model: Represents a user's booking of a listing.
- `Review` model: Allows users to rate and review listings.
- Serializers for API data transformation using Django REST Framework.
- A custom management command to populate the database with sample data.

## ⚙️ Features Implemented

- **Models**:
  - `Listing`: Fields include title, description, location, and price.
  - `Booking`: Tracks booking dates, associated user, and listing.
  - `Review`: Stores user reviews and ratings on listings.

- **Serializers**:
  - `ListingSerializer` and `BookingSerializer` created for REST API endpoints.

- **Seeder Command**:
  - Run `python manage.py seed` to populate the database with 10 sample listings.

## 🧪 How to Use

1. Clone the repo or duplicate `alx_travel_app` to `alx_travel_app_0x00`.
2. Install dependencies and configure your environment.
3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
