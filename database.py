import psycopg2

#establishing connection to psycopg2
conn = psycopg2.connect(host='localhost',port='5432',user='postgres',password='6979',dbname='myduka_db')
#cur object
cur = conn.cursor()


#fetching prods
def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products



def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()


def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales


#method 1 - f-string
def insert_sales(values):
    cur.execute(f"insert into sales(pid,quantity)values{values}")
    conn.commit()


#method 2 - using placeholders
def insert_sales_2(values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",values)
    conn.commit()


def available_stock(pid):
    cur.execute(f"select sum(stock_quantity) from stock where pid = {pid}")
    total_stock = cur.fetchone()[0] or 0

    cur.execute(f"select sum(quantity) from sales where pid = {pid}")
    total_sold = cur.fetchone()[0] or 0

    return total_stock - total_sold


#inserting stock
def insert_stock(values):
    cur.execute(f"insert into stock(pid,stock_quantity)values{values}")
    conn.commit()


#fetching stock
def get_stock():
    cur.execute("select * from stock")
    stock = cur.fetchall()
    return stock


#adding users
def insert_users(user_details):
    cur.execute(f"insert into users(full_name,email,phone_number,password)values{user_details}")
    conn.commit()


    

