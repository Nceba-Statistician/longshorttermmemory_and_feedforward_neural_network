from fastapi import FastAPI
import pandas
import pyodbc
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import warnings
from faker import Faker
from datetime import date

warnings.filterwarnings("ignore")
def ConnectionString():
    conn = pyodbc.connect(
        "Driver={ODBC Driver 18 for SQL Server};Server=DESKTOP-SLF5UBP;Database=loandatabase;UID=demouser;PWD=roots;TrustServerCertificate=yes;"
    )
    return conn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def route():
    return "string"

@app.get("/get_customerloan")
async def read_items():
    conn = ConnectionString()
    items = conn.cursor().execute("select * from customerloan").fetchall()
    customerloan = [{
        "customer_id": item.customer_id, "name": item.name, "age": item.age,
        "loan_amount": item.loan_amount, "interest_rate_percent": item.interest_rate_percent,
        "loan_type": item.loan_type, "loan_term_ months": item.loan_term_months,
        "approval_date": item.approval_date, "repayment_status": item.repayment_status, "branch": item.branch
    } for item in items]
    return customerloan

@app.post("/create_customerloan")
async def create_items(
    name: str, age: int, loan_amount: float, interest_rate_percent: float,
    loan_type: str, loan_term_months: int, 
    approval_date: date, repayment_status: str, branch: str
):         
    conn = ConnectionString()
    conn.cursor().execute("insert into customerloan (customer_id, name, age, loan_amount, interest_rate_percent, loan_type, loan_term_months, approval_date, repayment_status, branch) values (lower(newid()),?,?,?,?,?,?,?,?,?)",

        (
            name, age, loan_amount, interest_rate_percent, loan_type,
            loan_term_months, approval_date, repayment_status, branch
        )
    )
    conn.commit()
    return [{
        "name": name, "age": age, "loan_amount": loan_amount, "interest_rate_percent": interest_rate_percent,
        "loan_type": loan_type, "loan_term_ months": loan_term_months, "approval_date": approval_date,
        "repayment_status": repayment_status, "branch": branch 
    }]

@app.put("/update_customerloan")
async def update_items(
    customer_id: str, name: str, age: int, loan_amount: float, interest_rate_percent: float,
    loan_type: str, loan_term_months: int, approval_date: date, repayment_status: str, branch: str
):
    conn = ConnectionString()
    conn.cursor().execute(
        """
update customerloan
set name = ?, age = ?, loan_amount = ?, interest_rate_percent = ?, loan_type = ?,
loan_term_months = ?, approval_date = ?, repayment_status = ?, branch = ?
where customer_id = ? 
        """,
        (
            name, age, loan_amount, interest_rate_percent, loan_type,
            loan_term_months, approval_date, repayment_status, branch, customer_id
        )
    )
    conn.commit()
    return {f"message: The records for customer id {customer_id} were successfully updated"}

@app.delete("/delete_customerloan")
async def delete_items(customer_id: str):
    conn = ConnectionString()
    conn.cursor().execute("delete from customerloan where customer_id = ?", (customer_id))
    conn.commit()
    return {f"message: The records for customer id {customer_id} were successfully deleted"}

if __name__ == "_main_":
    uvicorn.run("APIcustomerloan:app", host="127.0.0.1", port=8000, reload=True)
    # uvicorn APIconfigCustomerloan:app --host 127.0.0.1 --port 8000 
