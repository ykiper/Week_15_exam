from typing import List, Dict, Any
from db import get_db_connection
import json


def get_customers_by_credit_limit_range():
    """Return customers with credit limits outside the normal range."""
    query = """SELECT customerName, creditLimit FROM customers 
        WHERE creditLimit < 10000 or creditLimit > 100000;"""
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    con.commit()
    return results



def get_orders_with_null_comments():
    """Return orders that have null comments."""
    query = """SELECT orderNumber, comments 
    FROM orders WHERE comments 
    is NULL order by orderDate;"""
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    con.commit()
    return results

def get_first_5_customers():
    """Return the first 5 customers."""
    query = """SELECT customerName, contactLastName, contactFirstName 
    FROM customers order by contactLastName limit 5;"""
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    con.commit()
    return results

def get_payments_total_and_average():
    """Return total and average payment amounts."""
    query = """SELECT sum(amount) as "total payments", avg(amount),
     min(amount), max(amount) FROM payments;"""
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    con.commit()
    return results

def get_employees_with_office_phone():
    """Return employees with their office phone numbers."""
    query = """select employees.firstName, employees.lastName,
     offices.phone from employees join offices on 
    employees.officeCode = offices.officeCode;"""
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    con.commit()
    return results

def get_customers_with_shipping_dates():
    """Return customers with their order shipping dates."""
    query = """select customers.customerName, orders.orderDate from customers left 
    join orders on customers.customerNumber = orders.customerNumber;"""
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    con.commit()
    return results

def get_customer_quantity_per_order():
    """Return customer name and quantity for each order."""
    query = """select customers.customerName, orderdetails.quantityOrdered from customers 
    join orders on customers.customerNumber = orders.customerNumber 
    join orderdetails on orders.orderNumber = orderdetails.orderNumber 
    order by customers.customerName;"""
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    con.commit()
    return results

def get_customers_payments_by_lastname_pattern():
    """Return customers and payments for last names matching pattern."""
    query = """select customers.customerName, employees.firstName, employees.lastName,
     sum(payments.amount) as "sum total" from customers join employees on customers.salesRepEmployeeNumber
      = employees.employeeNumber join payments on customers.customerNumber = payments.customerNumber 
      group by customers.customerNumber having employees.firstName LIKE '%ly%' or
       employees.firstName LIKE '%Mu%' order by "sum total" desc;"""
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    con.commit()
    return results

