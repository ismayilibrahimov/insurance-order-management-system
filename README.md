
# Insurance Order Management System

This project provides an insurance service, allowing users to sign up, log in, browse active products, create orders and check order's status.

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/ismayilibrahimov/insurance-order-management-system.git
```

### Setup Environment

1. Create a `.env` file in the root directory.
2. Add the following variables to the `.env` file:

```bash
POSTGRES_DB=insurance
POSTGRES_USER=postgres
POSTGRES_PASSWORD=root
DB_HOST=db
DB_PORT=5432
```

### Build and Run the Docker Containers

```bash
docker compose up --build
```

### Create a Superuser

Once the containers are up, create a superuser to manage the application:

```bash
docker compose exec web python manage.py createsuperuser
```

### Create Products (at Django admin)

After creating the superuser, you can create products such as:
- Auto Insurance
- Life Insurance

## API Endpoints

### Fetch Active Products
- **Endpoint**: `/api/v1/products/`
- **Method**: `GET`
- **Description**: Fetches a list of active products.

### Signup Endpoint
- **Endpoint**: `/api/v1/signup/`
- **Method**: `POST`
- **Payload**:

```json
{
  "username": "test",
  "email": "test@example.com",
  "password": "test"
}
```

### Login Endpoint
- **Endpoint**: `/api/v1/login/`
- **Method**: `POST`
- **Payload**:
```json
{
  "username": "test",
  "password": "test"
}
```

### Order List Endpoint
- **Endpoint**: `/api/v1/orders/`
- **Method**: `GET`
- **Description**: Fetches a list of the authenticated user's orders.
- **Authorization**: Requires Bearer Token in the `Authorization` header.

### Create Order Endpoint
- **Endpoint**: `/api/v1/order/create/`
- **Method**: `POST`
- **Authorization**: Requires Bearer Token in the `Authorization` header.
- **Payload**:
```json
{
  "product": 1
}
```

### Order Status Endpoint
- **Endpoint**: `/api/v1/order/<int:pk>/status/`
- **Method**: `GET`
- **Description**: Fetches the status of a specific order. The user can only view their own order's status.
- **Authorization**: Requires Bearer Token in the `Authorization` header.


## User Roles
- **Superuser**: Only superuser can change the roles of other users (admin or regular user).
- **Admin User**: Can view and edit products and orders. (via Django admin)
- **Regular User**: Can view and create their own orders. (via API endpoints)

## Running Unit Tests
To run the unit tests in the project, use the following command:
```bash
docker compose exec web python manage.py test
```

---

This project is set up using Docker and includes a PostgreSQL database. Make sure your `.env` file contains the correct database connection details before running the application.
