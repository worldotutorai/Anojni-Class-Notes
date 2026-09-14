# FastAPI Beginner API Project

A beginner-friendly FastAPI project demonstrating how to create REST APIs using Python and FastAPI. The project includes basic APIs for student information, courses, skills, mathematical operations, age classification, multiplication tables, profiles, and number analysis.

## Technologies Used

* Python
* FastAPI 0.141.1
* Uvicorn 0.52.4

## Project Structure

```text
FASTAPI/
│
├── part1_get.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Check Python Installation

Make sure Python is installed on your system.

```bash
python --version
```

If the above command does not work, try:

```bash
python3 --version
```

### 2. Install FastAPI

```bash
pip install fastapi==0.141.1
```

### 3. Install Uvicorn

Uvicorn is an ASGI server used to run the FastAPI application.

```bash
pip install uvicorn==0.52.4
```

You can also install both packages together:

```bash
pip install fastapi==0.141.1 uvicorn==0.52.4
```

## requirements.txt

Create a file named `requirements.txt` and add:

```text
fastapi==0.141.1
uvicorn==0.52.4
```

Install the dependencies using:

```bash
pip install -r requirements.txt
```

## Running the Application

Make sure you are inside the project directory containing `main.py`.

Run the application using:

```bash
uvicorn main:app --reload
```

### Understanding the Command

```text
uvicorn main:app --reload
```

* `uvicorn` - Starts the Uvicorn server.
* `main` - Refers to the `main.py` file.
* `app` - Refers to the FastAPI application object:

```python
app = FastAPI()
```

* `--reload` - Automatically reloads the server whenever code changes are detected.

After starting the server, you should see:

```text
Uvicorn running on http://127.0.0.1:8000
```

## Accessing the Application

Open the following URL in your browser:

```text
http://127.0.0.1:8000
```

The response will be:

```json
{
    "message": "welcome to super30 FASTAPI"
}
```

## API Endpoints

| No. | Endpoint                  | Method | Description                            |
| --- | ------------------------- | ------ | -------------------------------------- |
| 1   | `/`                       | GET    | Home API                               |
| 2   | `/student`                | GET    | Returns student information            |
| 3   | `/course`                 | GET    | Returns course information             |
| 4   | `/skills`                 | GET    | Returns available skills               |
| 5   | `/add/{num1}/{num2}`      | GET    | Adds two numbers                       |
| 6   | `/multiply/{num1}/{num2}` | GET    | Multiplies two numbers                 |
| 7   | `/square/{sides}`         | GET    | Calculates the square of a number      |
| 8   | `/check?num=`             | GET    | Checks whether a number is even or odd |
| 9   | `/age/{age}`              | GET    | Classifies a person based on age       |
| 10  | `/table/{num}`            | GET    | Generates a multiplication table       |
| 11  | `/profile/{name}/{age}`   | GET    | Returns profile information            |
| 12  | `/number/{number}`        | GET    | Performs basic number analysis         |

## API Examples

### 1. Home API

Endpoint:

```text
GET /
```

URL:

```text
http://127.0.0.1:8000/
```

Response:

```json
{
    "message": "welcome to super30 FASTAPI"
}
```

### 2. Student API

Endpoint:

```text
GET /student
```

URL:

```text
http://127.0.0.1:8000/student
```

Response:

```json
{
    "name": "yamuna",
    "role": "student",
    "course": [
        "python",
        "datascience"
    ]
}
```

### 3. Course API

Endpoint:

```text
GET /course
```

URL:

```text
http://127.0.0.1:8000/course
```

Response:

```json
{
    "course_name": "System Design",
    "mentor": "yamuna",
    "duration": "3 months",
    "topics": [
        "low level and high level design",
        "softaware development"
    ]
}
```

### 4. Skills API

Endpoint:

```text
GET /skills
```

URL:

```text
http://127.0.0.1:8000/skills
```

Response:

```json
{
    "skills": [
        "python",
        "sql",
        "AWS",
        "Docker",
        "AI Automation"
    ]
}
```

### 5. Addition API

This API accepts two integers as path parameters.

Endpoint:

```text
GET /add/{num1}/{num2}
```

Example:

```text
http://127.0.0.1:8000/add/10/20
```

Response:

```json
{
    "result": 30
}
```

### 6. Multiplication API

Endpoint:

```text
GET /multiply/{num1}/{num2}
```

Example:

```text
http://127.0.0.1:8000/multiply/5/10
```

Response:

```json
{
    "result": 50
}
```

### 7. Square API

Endpoint:

```text
GET /square/{sides}
```

Example:

```text
http://127.0.0.1:8000/square/5
```

Response:

```json
{
    "number": 5,
    "square": 25
}
```

### 8. Even/Odd API

This API uses a query parameter.

Endpoint:

```text
GET /check
```

Example:

```text
http://127.0.0.1:8000/check?num=10
```

Response:

```json
{
    "number": 10,
    "type": "even"
}
```

For an odd number:

```text
http://127.0.0.1:8000/check?num=7
```

Response:

```json
{
    "number": 7,
    "type": "odd"
}
```

## 9. Age API

This API categorizes a person based on their age.

Endpoint:

```text
GET /age/{age}
```

Example:

```text
http://127.0.0.1:8000/age/25
```

Response:

```json
{
    "age": 25,
    "message": "your are an adult"
}
```

### Age Categories

| Age       | Category       |
| --------- | -------------- |
| `<= 0`    | Invalid age    |
| `1 - 12`  | Child          |
| `13 - 17` | Teenager       |
| `18 - 39` | Adult          |
| `40 - 59` | Middle aged    |
| `60+`     | Senior citizen |

## 10. Multiplication Table API

Generates the multiplication table from 1 to 10.

Endpoint:

```text
GET /table/{num}
```

Example:

```text
http://127.0.0.1:8000/table/5
```

Response:

```json
{
    "number": 5,
    "table": [
        "5 x 1 = 5",
        "5 x 2 = 10",
        "5 x 3 = 15",
        "5 x 4 = 20",
        "5 x 5 = 25",
        "5 x 6 = 30",
        "5 x 7 = 35",
        "5 x 8 = 40",
        "5 x 9 = 45",
        "5 x 10 = 50"
    ]
}
```

## 11. Profile API

Accepts a name and age as path parameters.

Endpoint:

```text
GET /profile/{name}/{age}
```

Example:

```text
http://127.0.0.1:8000/profile/yamuna/25
```

Response:

```json
{
    "name": "yamuna",
    "age": 25
}
```

## 12. Number Analysis API

This API performs basic analysis of a number.

It returns:

* The original number
* Square of the number
* Cube of the number
* Whether the number is even

Endpoint:

```text
GET /number/{number}
```

Example:

```text
http://127.0.0.1:8000/number/4
```

Response:

```json
{
    "number": 4,
    "square": 16,
    "cube": 64,
    "even": true
}
```

For an odd number:

```text
http://127.0.0.1:8000/number/5
```

Response:

```json
{
    "number": 5,
    "square": 25,
    "cube": 125,
    "even": false
}
```

## Interactive API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to:

* View all available APIs
* View API parameters
* Execute API requests
* Test different inputs
* View API responses

### ReDoc

FastAPI also provides ReDoc documentation.

Open:

```text
http://127.0.0.1:8000/redoc
```

## Concepts Covered

This project demonstrates the following FastAPI and Python concepts:

### FastAPI Application

```python
from fastapi import FastAPI

app = FastAPI()
```

### GET Request

```python
@app.get("/")
def home_api():
    return {
        "message": "welcome to super30 FASTAPI"
    }
```

### Path Parameters

```python
@app.get("/add/{num1}/{num2}")
def addition(num1: int, num2: int):
    return {
        "result": num1 + num2
    }
```

### Query Parameters

```python
@app.get("/check")
def check(num: int):
    ...
```

The API can be called using:

```text
/check?num=10
```

### Type Validation

```python
num1: int
num2: int
```

FastAPI uses the type annotations to validate incoming request data.

### Conditional Statements

The project uses `if`, `elif`, and `else` for operations such as:

* Even/odd checking
* Age classification
* Number analysis

### Loops

The multiplication table API uses a `for` loop to generate values from 1 to 10.

## Stopping the Server

To stop the FastAPI server, press:

```text
CTRL + C
```

## Quick Start

Install the required packages:

```bash
pip install fastapi==0.141.1 uvicorn==0.52.4
```

Run the application:

```bash
uvicorn main:app --reload
```

Open the application:

```text
http://127.0.0.1:8000
```

Open the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```
This project is created for learning and practicing Python, FastAPI, REST APIs, path parameters, query parameters, conditional statements, and loops.

