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
    countries = country_repository.select_all()
    return render_template("list/index.html", cities = cities, countries = countries )

@cities_blueprint.route("/list/new")
def new_location():
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template("list/new.html", cities = cities, countries = countries)

@cities_blueprint.route("/list/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect("/list")

@cities_blueprint.route("/list/new", methods=['POST'])
def create_city():
    city_name = request.form['city_name']
    country_id = request.form['country_id']
    if "visited" in request.form:
        visited = True
    else:
        visited = False

    if country_id == "other":
        return redirect('/country/new')
    else:
        country = country_repository.select(country_id)
        city = City(city_name, visited, country)
        city_repository.save(city)
        return redirect('/list')
    
@cities_blueprint.route("/list/<id>/edit", methods=['GET']) 
def edit_city(id):
    city = city_repository.select(id)
    country = country_repository.select(city.country.id)
    countries = country_repository.select_all()
    return render_template('list/edit.html', city = city, country = country, countries = countries)

@cities_blueprint.route("/list/<id>", methods=["POST"])
def update_city(id):
    city_name = request.form['city_name']
    country_id = request.form['country_id']
    if "visited" in request.form:
        visited = True
    else:
        visited = False
    country = country_repository.select(country_id)
    city = City(city_name, visited, country, id)
    city_repository.update(city)
    return redirect('/list')

@cities_blueprint.route('/list/visited')
def visited_locations():    
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template("list/visited.html", cities = cities, countries = countries )

@cities_blueprint.route('/list/not_visited')
def not_visited_locations():    
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template("list/not_visited.html", cities = cities, countries = countries )





