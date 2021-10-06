from flask import Flask, render_template, request, redirect 
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository 
import repositories.country_repository as country_repository

search_blueprint = Blueprint("search", __name__)

@search_blueprint.route("/search")
def index():
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template("search/index.html", cities = cities, countries = countries)