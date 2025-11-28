import psycopg2

conn = psycopg2.connect(host='localhost',port='5432',user='postgres',password='6979',dbname='myduka_db')


cur = conn.cursor()

cur.execute("select * from products")
products = cur.fetchall()
# print(products)

def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

products = get_products()
print(products)


def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()
   
product1 = ('iphone',100000,120000)
product2 = ('hp',50000,60000)
insert_products(product1)
insert_products(product2)




