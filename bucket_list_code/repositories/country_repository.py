from db.run_sql import run_sql

from models.country import Country
from models.city import City

def save(country):
    sql = "INSERT INTO countries (country_name) VALUES (%s) RETURNING *"
    values = [country.country_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country


