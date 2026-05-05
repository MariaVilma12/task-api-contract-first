# Task API (Contract-First)

A **contract-first REST API** for task management built with **FastAPI**, **SQLAlchemy**, and **OpenAPI**.

This project demonstrates how to design and implement APIs starting from an **OpenAPI specification**, ensuring clear API contracts and consistency between implementation and documentation.

---

##  Features

* Contract-first API design using `openapi.yaml`
* FastAPI-based REST endpoints
* SQLAlchemy ORM for database interactions
* CRUD operations for tasks
* Custom OpenAPI schema integration
* Clean and minimal project structure

---

##  Tech Stack

* Python 3.11+
* FastAPI
* SQLAlchemy
* Uvicorn
* PyYAML

---

##  Project Structure

```
.
├── main.py              # FastAPI app
├── openapi.yaml        # API contract (OpenAPI 3.0)
├── backend/
│   ├── models.py       # Database models
│   ├── crud.py         # CRUD operations
│   └── database.py     # DB connection/session
└── requirements.txt
```

---

##  API Contract

The API is defined first in `openapi.yaml`, then implemented in FastAPI.

Key endpoints:

* `GET /tasks` → List all tasks
* `POST /tasks` → Create a task
* `GET /tasks/{taskId}` → Get task by ID
* `DELETE /tasks/{taskId}` → Delete task

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/task-api-contract-first.git
cd task-api-contract-first
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

---

##  API Docs

Since this is contract-first, the OpenAPI schema is loaded from `openapi.yaml`.

Visit:

```
http://127.0.0.1:8000/docs
```

---

##  Key Concept: Contract-First

Instead of generating docs from code, this project:

1. Defines API in OpenAPI (`openapi.yaml`)
2. Loads it into FastAPI
3. Implements endpoints to match the contract

This approach:

* Improves collaboration between frontend & backend
* Prevents breaking API changes
* Makes APIs easier to test and validate

---

##  Future Improvements

* Request/response validation against schema
* Authentication & authorization
* Pagination & filtering
* Docker support
* Automated contract testing

---


