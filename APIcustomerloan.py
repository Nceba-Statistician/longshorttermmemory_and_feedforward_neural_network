from fastapi import FastAPI
import pandas
import pyodbc
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import warnings

warnings.filterwarnings("ignore")
def ConnectionString():
    conn = pyodbc.connect(
        "Driver={ODBC Driver 18 for SQL Server};Server=DESKTOP-SLF5UBP;Database=loandatabase;UID=demouser;PWD=roots;TrustServerCertificate=yes;"
    )
    get_query = "select * from customerloan"
    post_query = "insert into customerloan (customer_id, name, age, loan_amount, interest_rate_percent, interest_rate_value, loan_type, loan_term_months, approval_date, repayment_status, branch)"
    put_query = "alter "
    delete_query = ""

    return conn, get_query, post_query, put_query, delete_query

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
    conn, get_query = ConnectionString()
    items = conn.cursor().execute(get_query).fetchall()
    customerloan = [{
        "age": item.age, "loan_amount": item.loan_amount, "interest_rate_percent": item.interest_rate_percent,
        "loan_type": item.loan_type, "loan_term_months": item.loan_term_months, "approval_date": item.approval_date,
        "repayment_status": item.repayment_status
    } for item in items]
    return customerloan

@app.post("/create_customerloan")
async def create_items():
    conn = ConnectionString()
    return ""

@app.put("/update_customerloan")
async def update_items():
    return ""

@app.delete("/delete_customerloan")
async def delete_items():
    return ""

if __name__ == "_main_":
    uvicorn.run("APIcustomerloan:app", host="127.0.0.1", port=8000, reload=True)
    # uvicorn APIcustomerloan:app --host 127.0.0.1 --port 8000
