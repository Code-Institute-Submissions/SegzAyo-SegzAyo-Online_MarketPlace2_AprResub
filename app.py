import os
from flask import (
    Flask, flash, render_template,
    request, redirect, session, url_for, jsonify)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from models import Seller

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
    products_data = mongo.db.productMDB.find()

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
            url_for("update_profile", username=session["user"]))
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
        return render_template("profile.html", seller=seller)
           
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