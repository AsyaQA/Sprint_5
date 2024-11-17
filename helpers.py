import random

def random_email():
    login = f'anastasiia{random.randint(100, 999)}@gmail.com'
    return login

def random_password():
    return random.randint(100000, 999999)

def random_name():
    name = ['Anastasiia', 'Yulia', 'Ivan', 'Evgeniy']
    random_name = random.choice(name)

    return random_name

def random_password_invalid():
    return random.randint(10000, 99999)