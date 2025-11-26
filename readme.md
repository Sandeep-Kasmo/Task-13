FastAPI CRUD Application with SQL Server

This project demonstrates how to build a full CRUD (Create, Read, Update, Delete) API using FastAPI, Pydantic, and SQL Server via pyodbc.
The API manages employee records stored in a SQL Server table named Employee.

🚀 Features

Connect to SQL Server using pyodbc

Create a new employee

Retrieve all employees

Retrieve a specific employee by ID

Update an existing employee

Delete an employee

Proper error handling with FastAPI exceptions

Pydantic models for validation

🛠 Tech Stack

Python 3.x

FastAPI

UVicorn

pyodbc

Pydantic

SQL Server

📂 Project Structure

        project/
        
        │── main.py
        
        │── README.md

⚙️ Prerequisites

Before running this project, ensure you have:

Python 3.8+

SQL Server (Express or Standard)

ODBC Driver 17 for SQL Server

A database named PythonLearningDB

A table named Employee

SQL Table Structure
            CREATE TABLE Employee (
                EmpId INT PRIMARY KEY,
                Name VARCHAR(100),
                Address VARCHAR(255),
                Phone BIGINT
            );

How to Run the Project

1.Install Dependencies
        pip install fastapi uvicorn pyodbc pandas

2.Start the Server
         python main.py
    

Or using uvicorn manually:

            uvicorn main:app --reload

3️.Access the API Documentation

FastAPI provides automatic Swagger documentation:

👉 http://127.0.0.1:8000/docs

You can test all endpoints from there.

📌 API Endpoints

1. Get all users
        GET /users/

2. Get a user by ID
        GET /users/{id}

3. Create a new user
        POST /users/
    
    Request Body
            {
              "empId": 1,
              "name": "John",
              "address": "Hyderabad",
              "phone": 9876543210
            }

4. Update an existing user
        PUT /users/{id}

5. Delete a user
        DELETE /users/{id}

🔌 Database Connection

The connection uses Windows Authentication:
        
                conn=pyodbc.connect(f"""
        Driver={{{driver}}};
        SERVER={server};
        DATABASE={database};
        Trusted_Connection=Yes;
                """)

🧪 Testing Tools

You can test API using:

Swagger UI (/docs)

Postman

Thunder Client (VS Code)

🙌 Author

Developed by Sandeep Reddy

FastAPI + SQL Server CRUD Learning Project




