# sellerapp

sellerapp is a web application for managing and participating in auctions. It allows users to create and manage auctions, bid on items, and determine auction winners automatically based on highest bid.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)

## Features

- Auction Management:
  - Create, view, update, and delete auctions from admin panel
  - Define start time, end time, start price, and item name for auctions
  - Automatic determination of auction winners based on the highest bid

- Bidding:
  - Users can place bids on active auctions
  - Real-time tracking of highest bids by admin

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mojnomiya/seller-app.git
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser (admin) account:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the admin panel by visiting `http://localhost:8000/admin/` and logging in with the superuser account.

2. Create auctions using the admin panel, specifying start time, end time, start price, and item name.

3. Users can view and bid on active auctions by visiting `http://localhost:8000/auction/home/`.

4. The application will automatically determine the auction winners at the end of the auction.

5. Simple navigation added at top. Admin authentication part skipped but added an admin views for the auctions.

## Technologies Used

- Django: The web framework for building the application.
- Python: The programming language used for the backend logic.
- HTML/CSS/Bootstrap: Front-end technologies for user interfaces.
- Database: SQLite