from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
import pyodbc
import pandas as pd

# App setup
app=FastAPI()


#connection setup
def establish_conn():
    try:
        conn=pyodbc.connect(
            'Driver={ODBC Driver 17 for SQL Server};'
            r'server=SANDY\SQLEXPRESS;'
            'database=PythonLearningDB;'
            'Trusted_connection=yes;'
        )
        return conn
    except Exception as e:
        print(f'Error connection:{e}')
        return None

# Pydantic model
class User(BaseModel):
    empId: int
    name: str
    address: str
    phone: int

# get all users details
@app.get("/users/")
def read_all_user():
    conn = establish_conn()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    cursor = conn.cursor()
    cursor.execute("SELECT EmpId, name, Address, phone FROM Employee")
    rows = cursor.fetchall()
    conn.close()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in rows]

# get specific user details
@app.get("/users/{id}")
def read_user(id: int = Path(..., description="The ID of the user to retrieve")):
    conn = establish_conn()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    cursor = conn.cursor()
    cursor.execute(f"SELECT EmpId, name, Address, phone FROM Employee WHERE EmpId = {id}")
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(zip([column[0] for column in cursor.description], row))
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
# Create a New User
@app.post("/users/")
def create_user(user: User):
    conn = establish_conn()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Employee (EmpID, name, Address, phone) VALUES (?, ?, ?, ?)",
        (user.empId, user.name, user.address, user.phone)
    )
    conn.commit()
    conn.close()
    return {"message": "User created successfully"}

# Update an Existing User Based on EmpId
@app.put("/users/{id}")
def update_user(id: int, user: User):
    conn = establish_conn()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Employee SET name = ?, Address = ?, phone = ? WHERE EmpId = ? ",
        (user.name, user.address, user.phone, id)
    )
    conn.commit()
    conn.close()
    return {"message": "User updated successfully"}

# Delete an Existing User on EmpId
@app.delete("/users/{id}")
def delete_user(id: int):
    conn = establish_conn()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Employee WHERE EmpId = ?", id)
    conn.commit()
    conn.close()
    return {"message": "User deleted successfully"}

# Define a port
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

