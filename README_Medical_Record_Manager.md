
# Medical Record Manager API

This project is a simple and extensible backend API built with **FastAPI** and **SQLite** for managing electronic health records (EHR). It is suitable for hospital or clinic systems.

## Features

- Add, edit, delete, and list patient records
- RESTful API with full documentation via Swagger UI
- Lightweight SQLite database
- Easily extendable for future health modules

## Technologies Used

- Python 3.10+
- FastAPI
- SQLite
- Swagger / OpenAPI

## How to Run

1. Install dependencies:

```bash
pip install fastapi uvicorn
```

2. Run the server:

```bash
python -m uvicorn main:app --reload
```

3. Visit the interactive docs at:

```
http://127.0.0.1:8000/docs
```

## Author

Farshad | [GitHub Profile](https://github.com/farshad-dev)
