from flask import Flask, render_template, request, redirect 
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository 
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/list")
def list():
    cities = city_repository.select_all()
    return render_template("list/index.html", cities = cities)




