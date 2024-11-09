# Ecommerce API

This project is a RESTful API for an Ecommerce platform, built using Django and Django REST Framework. It includes user registration, product management, cart functionality, and order processing.


## Features

- Authentication (Sign Up, Sign In
- Product Management (add product, Update product, Delete Product, Get All Products)
- Cart management (add, update, remove items)
- Order Management (Place Order, Get all orders, Get Orders by Customer ID,

## Installation

### Prerequisites

- Python 
- Django and Django REST Framework
- Postman (for testing API endpoints)

### Setup Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/praveen88p/ecommerce-api.git
    cd ecommerce-api
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Database**

   - Configure your database settings in `settings.py`.
   - Run migrations:

     ```bash
     python manage.py migrate
     ```

5. **Create a Superuser**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

Your API should now be running at `http://127.0.0.1:8000/`.

## Usage

You can use Postman or any API client to interact with the API. The following endpoints are available:

### Authentication

- **`POST /signup/`** - Register a new user
- **`POST /login/`** - Login and obtain an authentication token

### Products

- **`GET /products/`** - List all products
- **`POST /products/`** - Create a new product (Admin only)
- **`PUT /products/{product_id}/`** - Update a product (Admin only)
- **`DELETE /products/{product_id}/`** - Delete a product (Admin only)

### Cart

- **`POST /cart/add/`** - Add an item to the cart
- **`PUT /cart/update/`** - Update item quantity in the cart
- **`DELETE /cart/remove/`** - Remove item from cart
- **`GET /cart/`** - Retrieve all items in the user's cart

### Orders

- **`POST /placeorder/`** - Place an order with items in the cart
- **`GET /orders/customer/{customer_id}/`** - Retrieve all orders by customer ID (Admin only)
- **`GET /getallorders/`** - Retrieve all orders (Admin only)

## API Endpoints

### Authentication

#### Signup User
```http
POST /signup/
