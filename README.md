# Microservices Backend Documentation

This repository contains the backend code for a microservices architecture designed to manage user and property listings.

## Table of Contents

- [Clone Repository](#clone-repository)
- [Setup](#setup)
- [Running the Service](#running-the-service)

## Clone Repository

To clone this repository, run the following command in your terminal:

```bash
git clone <repository-url>
```

## Setup

1. **Set Up Virtual Environment**: Navigate to the project directory and create a virtual environment using Python's built-in venv module:

   ```bash
   python3 -m venv env
   ```

2. **Activate the Virtual Environment**: Activate the virtual environment:

   On Windows:

   ```bash
   .\env\Scripts\activate
   ```

   On Unix or MacOS:

   ```bash
   source env/bin/activate
   ```

3. **Install Dependencies**: Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize Databases**: If the project involves databases, initialize them by running database migrations or setting up the database schema.

## Running the Service

Once the setup is complete, you can run the service using the provided scripts or by executing the main application file.

### Running the Listing Service

1. Navigate to the listing service directory:

   ```bash
   cd listing_service
   ```

2. Run the listing service:

   ```bash
   python app.py
   ```

### Running the User Service

1. Navigate to the user service directory:

   ```bash
   cd user_service
   ```

2. Run the user service:

   ```bash
   python app.py
   ```

### Running the Public API Layer

1. Navigate to the public API layer directory:

   ```bash
   cd public_api
   ```

2. Run the public API layer:

   ```bash
   python app.py
   ```

### Accessing the Service

Once the services are running, you can access them using the provided APIs. Make requests to the appropriate endpoints as documented in the code or API documentation.

### Listing Service

#### Get all listings

```bash
curl localhost:6000/listings
```

Example Response:

```json
{
  "result": true,
  "listings": [
    {
      "id": 1,
      "user_id": 1,
      "listing_type": "rent",
      "price": 6000,
      "created_at": "2024-03-15T12:00:00",
      "updated_at": "2024-03-15T12:00:00"
    },
    {
      "id": 2,
      "user_id": 2,
      "listing_type": "sale",
      "price": 150000,
      "created_at": "2024-03-15T12:00:00",
      "updated_at": "2024-03-15T12:00:00"
    }
  ]
}
```

#### Create listing

```bash
curl -X POST localhost:6000/listings \
     -d "user_id=1" \
     -d "listing_type=rent" \
     -d "price=6000"
```

Example Response:

```json
{
  "result": true,
  "listing": {
    "id": 3,
    "user_id": 1,
    "listing_type": "rent",
    "price": 6000,
    "created_at": "2024-03-15T12:00:00",
    "updated_at": "2024-03-15T12:00:00"
  }
}
```

### User Service

#### Get all users

```bash
curl localhost:6001/users
```

Example Response:

```json
{
  "result": true,
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "created_at": "2024-03-15T12:00:00",
      "updated_at": "2024-03-15T12:00:00"
    },
    {
      "id": 2,
      "name": "Jane Smith",
      "created_at": "2024-03-15T12:00:00",
      "updated_at": "2024-03-15T12:00:00"
    }
  ]
}
```

#### Create user

```bash
curl -X POST localhost:6001/users \
     -d "name=John Doe"
```

Example Response:

```json
{
  "result": true,
  "user": {
    "id": 3,
    "name": "John Doe",
    "created_at": "2024-03-15T12:00:00",
    "updated_at": "2024-03-15T12:00:00"
  }
}
```

### Public API Layer

#### Get listings

```bash
curl localhost:6002/public-api/listings
```

Example Response:

```json
{
  "result": true,
  "listings": [
    {
      "id": 1,
      "listing_type": "rent",
      "price": 6000,
      "created_at": "2024-03-15T12:00:00",
      "updated_at": "2024-03-15T12:00:00",
      "user": {
        "id": 1,
        "name": "John Doe",
        "created_at": "2024-03-15T12:00:00",
        "updated_at": "2024-03-15T12:00:00"
      }
    },
    {
      "id": 2,
      "listing_type": "sale",
      "price": 150000,
      "created_at": "2024-03-15T12:00:00",
      "updated_at": "2024-03-15T12:00:00",
      "user": {
        "id": 2,
        "name": "Jane Smith",
        "created_at": "2024-03-15T12:00:00",
        "updated_at": "2024-03-15T12:00:00"
      }
    }
  ]
}
```

#### Create user

```bash
curl -X POST localhost:6002/public-api/users \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe"}'
```

Example Response:

```json
{
  "result": true,
  "user": {
    "id": 3,
    "name": "John Doe",
    "created_at": "2024-03-15T12:00:00",
    "updated_at": "2024-03-15T12:00:00"
  }
}
```

#### Create listing

```bash
curl -X POST localhost:6002/public-api/listings \
     -H "Content-Type: application/json" \
     -d '{"user_id": 1, "listing_type": "rent", "price": 6000}'
```

Example Response:

```json
{
  "result": true,
  "listing": {
    "id": 3,
    "user_id": 1,
    "listing_type": "rent",
    "price": 6000,
    "created_at": "2024-03-15T12:00:00",
    "updated_at": "2024-03-15T12:00:00"
  }
}
```
