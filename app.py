import os
from flask import (
    Flask, flash, render_template,
    request, redirect, session, url_for, jsonify)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from models import Seller, ProductListing, Category

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_products")
def get_products():
    products_data = ProductListing.objects().all()

    return render_template("products.html", products=products_data)



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        seller_name_v = request.form.get("seller_name")
        seller_email_v = request.form.get("email")
        seller_phone_v = request.form.get("phone")
        seller_city_v = request.form.get("city")
        password_v = request.form.get("password")

        # check if username already exists in db
        existing_seller = Seller.objects(seller_email=seller_email_v).first()

        if existing_seller:
            flash("Username already exists")
            return redirect(url_for("register"))

        new_seller = Seller(seller_name=seller_name_v, seller_email=seller_email_v, 
        seller_city=seller_city_v, seller_phone=seller_phone_v)

        new_seller.set_password(password_v)

        new_seller.save()


        # put the new user into 'session' cookie
        session["user"] = new_seller.seller_name
        session["userId"] = str(new_seller.id)
        flash("Registration Successful!")
        return redirect(
            url_for("update_profile", userId=session["userId"]))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email_v = request.form.get("email")
        password_v = request.form.get("password")
        # check if email and password exists in db
        existing_seller = Seller.objects(seller_email=email_v).first()

        if existing_seller:
            # ensure hashed password matches user input
            password_valid = existing_seller.check_password(password_v)
            if password_valid:
               session["user"] = existing_seller.seller_name
               session["user_id"] = str(existing_seller.id)
               flash(f"Welcome {existing_seller.seller_name}")
               return render_template("profile.html", seller=existing_seller)    
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
            
    return render_template("login.html")

@app.route("/users/<userId>", methods=["GET", "PUT"])
def update_profile(userId):
    print(userId)
    seller = Seller.objects(id=userId).first()
    if request.method == "GET":
        sellers_listings = ProductListing.objects(seller_id=seller).all()
        return render_template("profile.html", seller=seller, listings=sellers_listings)
           
    seller_name_v = request.json.get("seller_name")
    seller_email_v = request.json.get("email")
    seller_phone_v = request.json.get("phone")
    seller_city_v = request.json.get("city")
    password_v = request.json.get("password") 

    seller.seller_name = seller_name_v
    seller.email = seller_email_v
    seller.phone = seller_phone_v
    seller.city = seller_city_v
    seller.password = password_v
    seller.save()

    return jsonify({
        "msg": "Profile updated successfully"
    })
    

@app.route("/<userId>/list_product", methods=["GET", "POST"])
def list_product(userId):
    categories = Category.objects().all()
    seller = Seller.objects(id=userId).first()
    if request.method == "POST":
        category_id = request.form.get("category_id")
        product_name_v = request.form.get("product_name")
        product_price_v = request.form.get("product_price")
        product_description_v = request.form.get("product_description")

        # check if product is already listed
        existing_product = ProductListing.objects(product_name=product_name_v).first()

        category = Category.objects(id=category_id)
        if existing_product:
            flash("Product already listed")
            return redirect(url_for("list_product"))

        new_listing = ProductListing(category_id=category_id, product_name=product_name_v, 
            product_price=product_price_v, product_description=product_description_v, seller_id=seller)

        new_listing.save()
        flash("Item listed")

    return render_template("listing_page.html", seller=seller, categories=categories)

@app.route("/categories")
def populate_cat():
    Category(name="Electronics").save()
    Category(name="Household").save()
    Category(name="Furniture").save()
    Category(name="Cars").save()
    Category(name="Computers").save()
    return "Successfully added"

@app.route("/search")
def search():
    Search_word = request.args.get("product_name")
    products = ProductListing.objects.search_text(Search_word).all()
    print(products)
    print("testing text")

    return jsonify(products)
    

@app.route("/sign_out")
def sign_out():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))
    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)    