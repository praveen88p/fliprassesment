# Ecommerce API

This project is a RESTful API for an Ecommerce platform, built using Django and Django REST Framework. It includes user registration, product management, cart functionality, and order processing.


## Features

- Authentication (Sign Up, Sign In)
- Product Management (add product, Update product, Delete Product, Get All Products)
- Cart management (add, update, remove items)
- Order Management (Place Order, Get all orders, Get Orders by Customer ID)

## Installation

### Prerequisites

- Python 3.12.4
- Django and Django REST Framework
- Postman (for testing API endpoints)

### Setup Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/praveen88p/fliprassesment.git
    cd ecommerce_project
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

- **`POST api/signup/`** - Register a new user
- **`POST api/signin/`** - Login and obtain an authentication token

### Products

- **`Post /api/addproduct`** - Create a new product
- **`PUT /api/updateproduct/{product_id}/`** - Update a produc
- **`DELETE api/deleteproduct/{product_id}/`** - Delete a product
- **`GET /api/products/`** - List all products

### Cart

- **`POST /api/cart/add** - Add an item to the cart ( After login)
- **`PUT /api/cart/update`** - Update item quantity in the cart
- **`DELETE /api/cart/delete`** - Remove item from cart
- **`GET /api/cart`** - Retrieve all items in the user's cart

### Orders

- **`POST /api/placeorder`** - Place an order with items in the cart
- **`GET /api/getallorders`** - Retrieve all orders 
- **`GET /api/orders/customer/{customer_id}`** - Retrieve all orders by customer ID

## API documentation Publishing Link
[API documentation](https://documenter.getpostman.com/view/39581971/2sAY52bzA4)
