from bs4 import BeautifulSoup

import faker
from pprint import pprint

# import pprint


fake = faker.Faker()

# pprint_grace = pprint()

# nom = "phaka"

# pprint_grace.nom

number = int(input("veux-tu générer combien d'utilisateur ? : "))


def user():
    
    res_user = f"{fake.first_name()} {fake.last_name()}"
    
    return res_user
    
def users(number):
    
    get_user = []
    
    for _ in range(number):
        
        get_user.append(user())
        
    return get_user
    

if __name__ == "__main__":
    
    result = users(number)
    pprint(result)