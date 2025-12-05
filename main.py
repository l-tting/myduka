from flask import Flask, render_template
from database import get_products,get_sales


#Flask instance
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html") 


@app.route('/products')
def fetch_products():
    products = get_products()
    return render_template("products.html")


@app.route('/sales')
def fetch_sales():
    return render_template("sales.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


app.run(debug=True)

