# Database Management System
=====================================
## Setup
------------

### Environment Variables

The environment variables are stored in a `.env` file. The key assigning format for the `.env` file is as follows:

```makefile
# Key format: KEY="value"
# Example:
HOST="localhost"
USER="root"
PASSWORD="password"
DATABASE="database_name"
```

In this format:

*   `KEY` is the name of the environment variable.
*   `value` is the value assigned to the environment variable.
*   The key and value are separated by an equals sign (`=`).
*   The value is enclosed in double quotes (`" "`).

Table of Contents
-----------------

1.  [Introduction](#introduction)
2.  [Program Structure](#program-structure)
3.  [Importing Libraries](#importing-libraries)
4.  [Database Connection](#database-connection)
5.  [View Database](#view-database)
6.  [Insert Data](#insert-data)
7.  [Update Data](#update-data)
8.  [Delete Data](#delete-data)
9.  [Edit Database](#edit-database)
10. [Main Function](#main-function)
11. [Setup](#setup)

## Introduction
---------------

This program is a simple database management system. It allows users to view, insert, update, and delete customer data from a MySQL database.

## Program Structure
--------------------

The program is structured into several functions, each responsible for a specific task:

*   `view_database`: Displays all customer data in the database.
*   `insert_data`: Inserts new customer data into the database.
*   `update_data`: Updates existing customer data in the database.
*   `delete_data`: Deletes customer data from the database.
*   `edit_database`: Provides a menu for users to choose which operation to perform.
*   `main`: The main function that initializes the program and handles user input.

## Importing Libraries
----------------------

```python
import os
import dotenv
import mysql.connector
import decimal
import colorama
```

*   `os`: For interacting with the operating system.
*   `dotenv`: For loading environment variables from a `.env` file.
*   `mysql.connector`: For connecting to a MySQL database.
*   `decimal`: For handling decimal numbers.
*   `colorama`: For printing colored text to the console.

## Database Connection
----------------------

```python
dotenv.load_dotenv()

host = os.getenv("HOST")
pass_word = os.getenv("PASSWORD")
db = os.getenv("DATABASE")

database_connection = mysql.connector.connect(
    host=host,
    user="root",
    password=pass_word,
    database=db
)
```

*   Loads environment variables from a `.env` file using `dotenv`.
*   Establishes a connection to the MySQL database using `mysql.connector`.

## View Database
-----------------

```python
def view_database(database_connection):
    selected_table = "customer_details"
    cursor_view = database_connection.cursor()
    colorama.init(autoreset=True)
    print(colorama.Fore.CYAN + "-----------------------------")
    print(colorama.Fore.CYAN + f"{selected_table} : ")
    print(colorama.Fore.CYAN + "-----------------------------")
    cursor_view.execute("""select * from customer_details """)
    records = cursor_view.fetchall()
    for row in records:
        print(row, end="\n")
    database_connection.commit()
    cursor_view.close()
    print(colorama.Fore.CYAN + "-----------------------------")
```

*   Defines a function `view_database` that takes a database connection as an argument.
*   Executes a SQL query to select all data from the `customer_details` table.
*   Fetches and prints all records from the table.

## Insert Data
----------------

```python
def insert_data(database_connection):
    print(colorama.Fore.CYAN + "insert function ")
    selected_table = "customer_details"
    is_run = True
    while is_run:
        customer_id = input("enter your customer id : ")
        while customer_id == "" or str(customer_id).isalpha():
            print(colorama.Fore.RED + "Invalid customer id. Please enter a customer id")
            customer_id = input("enter your customer id : ")
        if (int(customer_id) > 100) or (int(customer_id) < 1):
            print(colorama.Fore.RED + "Id cannot be less than 1 and greater than 100")
            customer_id = input("enter your customer id : ")
        else:
            product_name = input("enter your product name : ")
            while (product_name == "") or product_name.isdigit():
                print(colorama.Fore.RED + "Invalid product name. Please enter a product name without any numbers")
                product_name = input("enter your product name : ")
            if len(product_name) > 50:
                print(colorama.Fore.RED + "Please enter a product name with maximum length of 50 characters")
                product_name = input("enter your product name : ")
            else:
                price = input("enter your product price : ")
                while price == "" or str(price).isalpha():
                    print(colorama.Fore.RED + "Please enter a price")
                    price = input("enter your product price : ")
                if int(price) <= 0:
                    print(colorama.Fore.RED + "Invalid product price. Please enter a product price greater than 0")
                    price = input("enter your product price : ")
                else:
                    print(colorama.Fore.GREEN + "Insertion Initiated..")
                    is_run = False
    confirm = input(f"""Confirm to add this data({customer_id},{product_name},{price}) to {selected_table} , type yes : """)
    if not confirm.lower() == "yes":
        print("Operation cancelled")
    else:
        cursor_insert = database_connection.cursor()
        query = f""" insert into {selected_table} values
        ({customer_id},"{product_name}",{price})"""
        cursor_insert.execute(query)
        database_connection.commit()
        print(f""" ({customer_id},"{product_name}",{price}) is inserted successfully """)
```

*   Defines a function `insert_data` that takes a database connection as an argument.
*   Prompts the user to enter customer data (id, product name, and price).
*   Validates user input to ensure it meets the required criteria.
*   Inserts the data into the `customer_details` table.

## Update Data
----------------

```python
def update_data(database_connection):
    print("update function ")
    select_table = "customer_details"
    update_what = input(colorama.Fore.CYAN + """
    -----------------------------
    what do you want update : 
    -----------------------------
    1.update product_name
    2.update product_price
    -----------------------------
    >>> """)
    if int(update_what) == 1:
        cus_id = input(colorama.Fore.CYAN + "enter the customer_id of the product_name to be updated : ")
        while cus_id == "" or cus_id.isalpha():
            print(colorama.Fore.RED + "Invalid customer id. Please enter a customer id")
            cus_id = input(colorama.Fore.CYAN + "enter the customer_id of the product_name to be updated : ")
        cursor_update = database_connection.cursor()
        Query = f"""select * from {select_table} ;"""
        cursor_update.execute(Query)
        records = cursor_update.fetchall()
        record_list1 = []
        for record in records:
            record_list1.append(record[0])
        while int(cus_id) not in record_list1:
            print(colorama.Fore.RED + f"{cus_id} is not in the table {select_table}")
            cus_id = input(colorama.Fore.CYAN + """
            enter the customer_id of the product_name to be updated : 
            (enter 'Q' to cancel) >>> """)
        if not cus_id.lower() == "q":
            update_product_name = input(colorama.Fore.CYAN + "enter the product name to be updated : ")
            Query2 = f""" select * from {select_table} ;"""
            cursor_update.execute(Query2)
            records2 = cursor_update.fetchall()
            record_list2 = []
            for row in records2:
                record_list2.append(row[1])
            if update_product_name in record_list2:
                print(colorama.Fore.CYAN + f"{update_product_name} is in the record ")
                new_product_name = input(colorama.Fore.CYAN + "enter the new product name : ")
                while len(new_product_name) > 50 or new_product_name == "" or new_product_name.isalpha() == False:
                    print(colorama.Fore.RED + "Invalid product name. Please enter a product name without any numbers and less than 50 characters")
                    new_product_name = input(colorama.Fore.CYAN + "enter the product name to be updated : ")
                new_product_query = f"""update {select_table} 
                set product_name="{new_product_name}"
                where customer_id={cus_id};
                """
                cursor_update.execute(new_product_query)
                database_connection.commit()
                cursor_update.close()
                print(colorama.Fore.GREEN + "Customer details updated successfully")
                to_view = input(""""enter '0' to view 
                              ('q' to exit): """)
                while not to_view.lower() == "q" and not int(to_view) == 0:
                    print(colorama.Fore.RED + "Invalid input. Please enter '0' to view or 'q' to exit")
                    to_view = input(""""enter '0' to view 
                              ('q' to exit): """)
                if int(to_view) == 0:
                    view_database(database_connection)
                else:
                    print("Operation cancelled")
            else:
                print(colorama.Fore.RED + f"{update_product_name} is not in the record ")
        print(colorama.Fore.CYAN + "program ended ")
```

*   Defines a function `update_data` that takes a database connection as an argument.
*   Prompts the user to choose which field to update (product name or price).
*   Updates the selected field in the `customer_details` table.

## Delete Data
----------------

```python
def delete_data(database_connection):
    select_table = "customer_details"
    cursor_delete = database_connection.cursor()
    query_select = f"""select * from {select_table}"""
    cursor_delete.execute(query_select)
    records = cursor_delete.fetchall()
    print("All records from ", select_table)
   