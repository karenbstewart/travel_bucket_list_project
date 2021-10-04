from flask import Flask, render_template, request, redirect 
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository 
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)


@countries_blueprint.route("/country/new")
def add_country():
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template("/country/new.html", cities = cities, countries = countries)

@countries_blueprint.route("/country/new", methods=['POST'])
def create_country():
    country_name = request.form['country_name']
    country = Country(country_name)
    country_repository.save(country)
    return redirect('/list/new')



