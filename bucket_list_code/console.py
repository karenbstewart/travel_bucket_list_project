import pdb 
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository 
import repositories.country_repository as country_repository

city_repository.delete_all()
country_repository.delete_all()


country1 = Country("Spain")
country_repository.save(country1)
country2 = Country("Italy")
country_repository.save(country2)

city1 = City("barcelona", True, country1 )
city_repository.save(city1)
city2 = City("Astorga", False, country1)
city_repository.save(city2)
city3 = City("Milan", False, country2)
city_repository.save(city3)
city4 = City("Rome", True, country2)
city_repository.save(city4)





pdb.set_trace()