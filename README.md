# Product Management API

A RESTful API built with Python and FastAPI to manage products. This project provides endpoints to create, list, update, and delete products.

## Technologies

- **Python** — Programming language
- **FastAPI** — Web framework for building APIs
- **Pydantic** — Data validation and serialization
- **Uvicorn** — ASGI server

## Features

- List all products
- Retrieve a product by ID
- Create a new product
- Update an existing product
- Delete a product
- Validate product data using Pydantic

## Project Structure

```text
api_chupchupcremosao/
├── .venv/
├── main.py
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd api_chupchupcremosao
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn
```

## Running the API

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

- **API:** http://127.0.0.1:8000
- **Interactive documentation:** http://127.0.0.1:8000/docs
- **Alternative documentation:** http://127.0.0.1:8000/redoc

## Product Data

A product can contain the following fields:

| Field | Type | Description |
|---|---|---|
| `id` | Integer | Unique product identifier |
| `nome` | String | Product name |
| `descricao` | String | Product description |
| `preco` | Float | Product price |
| `qtd` | Integer | Available quantity |

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/produtos` | List all products |
| `GET` | `/produtos/{id}` | Retrieve a product |
| `POST` | `/produtos` | Create a product |
| `PUT` | `/produtos/{id}` | Update a product |
| `DELETE` | `/produtos/{id}` | Delete a product |

*Note: These endpoints describe the intended CRUD interface. Adjust them to match the routes implemented in `main.py`.*

## Example Request

Create a product using `POST /produtos`:

```json
{
  "nome": "Chocolate Ice Cream",
  "descricao": "Creamy chocolate ice cream",
  "preco": 12.5,
  "qtd": 20
}
```

## Learning Goals

This project is designed to practice:

- Building REST APIs with FastAPI
- Using HTTP methods
- Validating request data with Pydantic
- Implementing CRUD operations
- Organizing a Python project
- Testing endpoints through Swagger UI

## Future Improvements

- Integrate a database such as PostgreSQL
- Add authentication using JWT
- Implement pagination and filtering
- Add automated tests with Pytest
- Add Docker support

## Author

**William Roque**

GitHub: [william-grassis67](https://github.com/william-grassis67)

---

This project is part of my journey to improve my Python backend development skills.
