from fastapi import FastAPI
from db_init import init_database

app = FastAPI()

init_database()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/customers/by-country/{country}")
def customers_by_country(country: str):
    pass

@app.get("/orders/by-customer/{customer_number}")
def orders_by_customer(customer_number: int):
    pass

@app.get("/products/{product_code}")
def product_details(product_code: str):
    pass

@app.get("/employees/by-office/{office_code}")
def employees_by_office(office_code: str):
    pass

@app.get("/payments/by-customer/{customer_number}")
def payments_by_customer(customer_number: int):
    pass

@app.get("/orders/{order_number}/details")
def order_details(order_number: int):
    pass

@app.get("/customers/top/{limit}")
def top_customers(limit: int):
    pass

@app.get("/products/in-stock")
def products_in_stock():
    pass
