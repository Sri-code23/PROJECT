import os
import dotenv 
import mysql.connector
import decimal
# ? dotenv- to load environment variables from .env file
# ? mysql.connector- to connect to mysql database
# ? decimal- to handle decimal numbers
import colorama


# TODO // method to view the entire table in the selected database
def view_database(database_connection):
    selected_table="customer_details"
    cursor_view=database_connection.cursor()
    colorama.init(autoreset=True)
    print(colorama.Fore.CYAN + "-----------------------------")
    print(colorama.Fore.CYAN + f"{selected_table} : " )
    print(colorama.Fore.CYAN + "-----------------------------")
    cursor_view.execute("""select * from customer_details """)

    records=cursor_view.fetchall()
    for row in records:
        print(row ,end="\n")
    database_connection.commit()
    cursor_view.close()
    print(colorama.Fore.CYAN + "-----------------------------")

# TODO // method to insert data into the selected table in the selected database
def insert_data(database_connection):
    print(colorama.Fore.CYAN + "insert function ")
    selected_table="customer_details"
    is_run=True
    while is_run:
        customer_id=input("enter your customer id : ")
        while  customer_id=="" or str(customer_id).isalpha():
            print(colorama.Fore.RED + "Invalid customer id. Please enter a customer id")
            customer_id=input("enter your customer id : ")
        if (int(customer_id) >100) or (int(customer_id) < 1):
            print(colorama.Fore.RED + "Id cannot be less than 1 and greater than 100")
            customer_id=input("enter your customer id : ")

        else:
            product_name=input("enter your product name : ")
            while (product_name=="") or product_name.isdigit():
                print(colorama.Fore.RED + "Invalid product name. Please enter a product name without any numbers")
                product_name=input("enter your product name : ")
            if len(product_name)>50:
                print(colorama.Fore.RED + "Please enter a product name with maximum length of 50 characters")
                product_name=input("enter your product name : ")

            else:
                price=input("enter your product price : ")
                while  price=="" or str(price).isalpha():
                    print(colorama.Fore.RED + "Please enter a price")
                    price=input("enter your product price : ")
                if int(price)<=0 :
                    print(colorama.Fore.RED + "Invalid product price. Please enter a product price greater than 0")
                    price=input("enter your product price : ")

                else:
                    print(colorama.Fore.GREEN + "Insertion Initiated..")
                    is_run= False
    confirm=input(f"""Confirm to add this data({customer_id},{product_name},{price}) to {selected_table} , type yes : """)
    if not confirm.lower() == "yes":
        print("Operation cancelled")
    else:
        cursor_insert=database_connection.cursor()
        query=f""" insert into {selected_table} values
        ({customer_id},"{product_name}",{price})"""

        cursor_insert.execute(query)
        database_connection.commit()
        print(f""" ({customer_id},"{product_name}",{price}) is inserted successfully """)


# TODO // method to update data in the selected table in the selected database
def update_data(database_connection):
    print("update function ")
    select_table="customer_details"
    update_what=input(colorama.Fore.CYAN +"""
    -----------------------------
    what do you want update : 
    -----------------------------                  
    1.update product_name
    2.update product_price
    -----------------------------                  
    >>> """)
    if int(update_what)==1:
        cus_id=input(colorama.Fore.CYAN + "enter the customer_id of the product_name to be updated : ")
        while cus_id=="" or cus_id.isalpha():
            print(colorama.Fore.RED + "Invalid customer id. Please enter a customer id")
            cus_id=input(colorama.Fore.CYAN + "enter the customer_id of the product_name to be updated : ")

        cursor_update=database_connection.cursor()
        Query=f"""select * from {select_table} ;"""
        cursor_update.execute(Query)
        records=cursor_update.fetchall()
        record_list1=[]
        for record in records:
            record_list1.append(record[0])
        #print("record_list :", record_list1)


        while int(cus_id) not in  record_list1:
            print(colorama.Fore.RED + f"{cus_id} is not in the table {select_table}")
            cus_id=input(colorama.Fore.CYAN + """
            enter the customer_id of the product_name to be updated : 
            (enter 'Q' to cancel) >>> """)
        if not cus_id.lower()=="q":
            update_product_name=input(colorama.Fore.CYAN + "enter the product name to be updated : ")
            Query2=f""" select * from {select_table} ;"""
            cursor_update.execute(Query2)
            records2=cursor_update.fetchall()
            record_list2=[]
            for row in records2:
                record_list2.append(row[1])
            if update_product_name in record_list2:
                print(colorama.Fore.CYAN + f"{update_product_name} is in the record ")
                new_product_name=input(colorama.Fore.CYAN + "enter the new product name : ")
                while len(new_product_name)>50 or new_product_name=="" or new_product_name.isalpha()==False:
                    print(colorama.Fore.RED + "Invalid product name. Please enter a product name without any numbers and less than 50 characters")
                    new_product_name=input(colorama.Fore.CYAN + "enter the product name to be updated : ")
                new_product_query=f"""update {select_table} 
                set product_name="{new_product_name}"
                where customer_id={cus_id};
                """
                cursor_update.execute(new_product_query)  
                database_connection.commit()
                cursor_update.close()
                print(colorama.Fore.GREEN + "Customer details updated successfully")
                to_view=input(""""enter '0' to view 
                              ('q' to exit): """) 
                while not to_view.lower()=="q" and not int(to_view)==0:
                    print(colorama.Fore.RED + "Invalid input. Please enter '0' to view or 'q' to exit")
                    to_view=input(""""enter '0' to view 
                              ('q' to exit): """)
                if int(to_view)==0:
                    view_database(database_connection)
                else :
                    print("Operation cancelled")
            else:
                print(colorama.Fore.RED + f"{update_product_name} is not in the record ")    
        print(colorama.Fore.CYAN + "program ended ")   




    elif int(update_what)==2:
        cus_id=input(colorama.Fore.CYAN + "enter the customer_id of the price to be updated : ")
        while cus_id=="" or cus_id.isalpha():
            print(colorama.Fore.RED + "Invalid customer id. Please enter a customer id")
            cus_id=input(colorama.Fore.CYAN + "enter the customer_id of the price to be updated : ")

        cursor_update=database_connection.cursor()
        Query=f"""select * from {select_table} ;"""
        cursor_update.execute(Query)
        records3=cursor_update.fetchall()
        record_list3=[]
        for record in records3:
            record_list3.append(record[0])
        #print(colorama.Fore.CYAN + "record_list :", record_list3)

        while int(cus_id) not in  record_list3:
            print(colorama.Fore.RED + f"{cus_id} is not in the table {select_table}")
            cus_id=input(colorama.Fore.CYAN + """
enter the customer_id of the price to be updated 
(enter 'Q' to cancel) >>> """)
        if not cus_id.lower()=="q":
            old_price=input(colorama.Fore.CYAN + "enter the price to be updated : ")
            while old_price=="" or old_price.isalpha():
                old_price=input(colorama.Fore.CYAN + "enter the price to be updated : ")
                
            Query2=f""" select * from {select_table} ;"""
            cursor_update.execute(Query2)
            records4=cursor_update.fetchall()
            record_list4=[]
            for row in records4:
                record_list4.append(row[2])
            print(record_list4)

            old_price=decimal.Decimal(old_price)
            if old_price in record_list4:
                print(colorama.Fore.GREEN + f"{old_price} is in the record ")
                new_price=input(colorama.Fore.CYAN + "enter the new price : ")
                while new_price=="" or new_price.isalpha():
                    print(colorama.Fore.RED + "Invalid price ")
                    new_price=input(colorama.Fore.CYAN + "enter the new price  to be updated : ")


                new_product_query=f"""update {select_table} 
                set price="{new_price}"
                where customer_id={cus_id};
                """
                cursor_update.execute(new_product_query)  
                database_connection.commit()
                cursor_update.close()
                print(colorama.Fore.GREEN + "Customer details updated successfully")
                to_view=input("""
enter '0' to view ('q' to exit): """) 
                
                while not to_view.lower()=="q" and not int(to_view)==0:
                    print(colorama.Fore.RED + "Invalid input. Please enter '0' to view or 'q' to exit")
                    to_view=input("enter '0' to view ('q' to exit): ")
                if int(to_view)==0:
                    view_database(database_connection)
                elif (to_view.lower()=="q") :
                    print(colorama.Fore.GREEN + "Operation cancelled")
            else:
                print(colorama.Fore.RED + f"{old_price} is not in the record ")
        print(colorama.Fore.GREEN + "program ended")
    else:
        print(colorama.Fore.RED + " invalid input - re-run the program ..")
        database_connection.close()

# TODO // method to delete the data in the selected table 
def delete_data(database_connection):
    #print("delete function ")
    
    select_table="customer_details"

    cursor_delete=database_connection.cursor()
    query_select=f"""select * from {select_table}"""
    cursor_delete.execute(query_select)
    records=cursor_delete.fetchall()
    print("All records from ",select_table)
    print(colorama.Fore.WHITE + colorama.Style.BRIGHT + "----------------------")
    for record in records:
        print(record, end="\n")
    print(colorama.Fore.WHITE + colorama.Style.BRIGHT + "----------------------")
    #print(colorama.Fore.CYAN + "Select the ID of the record you want to delete")
    record_len=len(records)


    #print(f" record length : {record_len}")
    records_list=[]
    for i in range(1,record_len+1):
        records_list.append(i)
    #print(f" Recorded list : {records_list}")
    row_to_delete=input(colorama.Fore.CYAN + "enter the ID of the row to be deleted : ")
    if int(row_to_delete) in records_list:
        delete_query=f"""delete from {select_table} where customer_id = {row_to_delete};"""
        
        cursor_delete.execute(delete_query)
        print(colorama.Fore.GREEN + f"{row_to_delete} is deleted from the table {select_table} ")
        database_connection.commit()
        cursor_delete.close()
    elif row_to_delete.isalpha():
        print(colorama.Fore.RED + f"{row_to_delete} is not a row number") 

    elif int(row_to_delete) not in records_list :
        print(colorama.Fore.RED + f"{row_to_delete} doesnot exists in the {select_table}")      
    

    database_connection.close()


# TODO // method to choose the edit option 
def edit_database(database_connection):
    user_in=int(input(colorama.Fore.CYAN + """
-----------------------------                  
which operation (1,2,3): 
-----------------------------                  
1.To Insert
2.To Update
3.To Delete
-----------------------------                  
>>> """))
    if user_in==1:
        insert_data(database_connection)
    elif user_in==2:
        update_data(database_connection)
    elif user_in==3:
        delete_data(database_connection)
        


# TODO // main function
def main():
    dotenv.load_dotenv()

    host=os.getenv("HOST")
    pass_word=os.getenv("PASSWORD")
    db=os.getenv("DATABASE")

    database_connection=mysql.connector.connect(
        host=host,
        user="root",
        password=pass_word,
        database=db
    )
    input_in=input(colorama.Fore.CYAN + colorama.Style.BRIGHT + f"""
-----------------------------               
enter the operation (1/2/3) :
-----------------------------     
1.View table
2.Edit table           
3.Exit 
-----------------------------           
>>> """)
    
    while not (int(input_in)==1 or int(input_in)==2 or int(input_in)==3):
        print("Invalid option. Please try again.")
        input_in=input(colorama.Fore.CYAN + colorama.Style.BRIGHT + f"""
-----------------------------               
enter the operation (1,2,3) :
-----------------------------
1.View 
2.Edit
3.Exit
-----------------------------
>>> """)
    else:
        if int(input_in)==1:
            #print("loading database...")
            view_database(database_connection)
        elif int(input_in)==2:
            print(colorama.Fore.CYAN + "-----------------------------")
            edit_database(database_connection)
        else:
            print(colorama.Fore.GREEN + "-----------------------------")
            print(colorama.Fore.GREEN + "Exited ")
            database_connection.close()


if __name__=="__main__":
    main()
