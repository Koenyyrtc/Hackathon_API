import random

def random_user():
    first_names = ["John", "Jane", "Alice", "Bob", "Charlie"]
    last_names = ["Smith", "Doe", "Johnson", "Brown", "Lee"]
    domains = ["gmail.com", "yahoo.com", "outlook.com"]
    
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}"
    
    return {
        "name": f"{first_name} {last_name}",
        "email": email,
        "avatar": f"https://robohash.org/{first_name}{last_name}.png",
        "bio": "This is a randomly generated user profile."
    }

