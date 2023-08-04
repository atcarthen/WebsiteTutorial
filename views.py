#Entry we will store all of the roots to URL for BP.
#It's neccessary to like this .py file to the main .py files so URLs can be accessed
#Best Practice is to create a seprate page defining roots
from flask import Blueprint, render_template, request, jsonify

views = Blueprint( __name__, 'views')
#Create views
#/home is a route of the URL


@views.route("/")
def home():
    return "<h1>Toolkit Billing Page!</h1>"

@views.route("/visual")
def home2():
    args = request.args
    name = args.get('name')
    return render_template("index2.html", name=name, pwrLvL= "3hunna")
#<username> html wrapper above will render 3 ways where the {{name}} is used


# name = x is passing the variable through the 
# inded/index2 {{name}}</input>

@views.route("/billing/<username>")# <username> passes what ever the input is in URL
def profile(username):
    return render_template("index.html", name=username)

@views.route("/HQ")
def get_json():
    return jsonify({'name': 'Anthony', 'Power Level': 100})

#    return "Toolkit Home Page!"
@views.route("/views")
def toolkit():
    return "<h1>Toolkitshawty</h1>"


    #debug = True, 
    #detects/allows changes to be made without 
    #re-running the application