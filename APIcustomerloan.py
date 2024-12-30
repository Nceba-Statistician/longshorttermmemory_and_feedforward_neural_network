import pyodbc
import pandas
import warnings
warnings.filterwarnings("ignore")

conn = pyodbc.connect(
    "Driver={ODBC Driver 18 for SQL Server};Server=DESKTOP-SLF5UBP;Database=loandatabase;UID=demouser;PWD=roots;TrustServerCertificate=yes;"
)
customerloan = pandas.read_sql_query("select * from customerloan", conn)
customerloan = customerloan[[
    "age", "loan_amount", "interest_rate_percent", "loan_type",
    "loan_term_months", "approval_date", "repayment_status"]]
customerloan["loan_type"] = customerloan["loan_type"].map({
    "Personal": 0, "Home": 1, "Car": 2, "Education": 3, "Business": 4
})
customerloan["repayment_status"] = customerloan["repayment_status"].map({
    "On_track": 0, "Delayed": 1, "Defaulted": 2
})
# print(customerloan.head()) APIcustomerloan