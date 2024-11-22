from faker import Faker
import pandas
import random
import pyodbc
import warnings
warnings.filterwarnings("ignore")

def loancustomerfun():
    customerloan = []
    for _ in range(500):
        loan_amount = round(random.uniform(1000, 50000), 2)
        interest_rate_percent = round(random.uniform(3, 15), 2)
        interest_rate_value  = round((interest_rate_percent/100) * loan_amount, 2)
        customer = {
            "customer_id": Faker().uuid4(), "name": Faker().name(), "age": random.randint(18, 65),
            "loan_amount": loan_amount, "interest_rate_percent": interest_rate_percent, "interest_rate_value": interest_rate_value,
            "loan_type": random.choice(["Personal", "Home", "Car", "Education", "Business"]), "loan_term_months": random.randint(12, 72),
            "approval_date": Faker().date_between(start_date=-5, end_date="today"), "repayment_status": random.choice(["On_track", "Delayed", "Defaulted"]),
            "branch": Faker().city()
        }
        customerloan.append(customer)    
    return pandas.DataFrame(customerloan)

def pushcustomerloansqlfun(records):
    try:
        conn = pyodbc.connect(
            "Driver={ODBC Driver 18 for SQL Server};Server=DESKTOP-SLF5UBP;Database=loandatabase;UID=demouser;PWD=roots;TrustServerCertificate=yes;"
        )
        for index, row in records.iterrows():
            conn.cursor().execute(
                "insert into customerloan(customer_id, name, age, loan_amount, interest_rate_percent, interest_rate_value, loan_type, loan_term_months, approval_date, repayment_status, branch)"
                "values(?,?,?,?,?,?,?,?,?,?,?)", tuple(row)
                )
            conn.commit()
        print("customer loan records have been pushed to SQL Server.")
    except Exception as e:
        print(f"Transfare records to sql server failed: {e}")              
pushcustomerloansqlfun(loancustomerfun())

