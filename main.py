from flask import Flask
from database import get_products,get_sales


#Flask instance
app = Flask(__name__)


@app.route("/")
def home():
    return "This is the index route"


@app.route('/products')
def fetch_products():
    products = get_products()
    return products


@app.route('/sales')
def fetch_sales():
    return "This is sales route"


@app.route('/dashboard')
def dashboard():
    return "This is the dashboard route"


@app.route("/login")
def login():
    return "This is the login route"


@app.route("/register")
def register():
    return "This is the register route"


app.run()

