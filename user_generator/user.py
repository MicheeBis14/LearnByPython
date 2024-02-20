import faker
from pprint import pprint

fake = faker.Faker()

n = 100
def get_user():
    return f"{fake.first_name()} {fake.last_name()}"


def get_users(n):
    # return [get_user() for _ in range(n)]
    
    users =[]
    
    for _ in range(n):
        users.append(get_user())
           
    return users


if __name__ == "__main__":
    
    user = get_users(n)
    pprint(user)
    
    
    