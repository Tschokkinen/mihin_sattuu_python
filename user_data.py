import os
import os.path
import json
from user import User

#os.chdir(r'...')

cwd = os.getcwd()
os.chdir(cwd + '/')

def ask_user_data():
    """Ask user data if first launch or user data edited."""
    name = input("Nimi: ")
    height = input("Pituus: ")
    weight = input("Paino: ")

    user = User(name, height, weight)

    user_info = {
        'name': user.name,
        'height': user.height,
        'weight': user.weight,
    }

    filename = 'data/user_data.json'
    with open(filename, 'w') as f:
        json.dump(user_info, f)

def check_user_data():
    """Check user data."""
    #Check if user data file has been created.
    does_file_exist = os.path.exists("data/user_data.json")

    #Check if user name exists (i.e. file is not empty).
    if does_file_exist:
        filename = 'data/user_data.json'
        with open(filename) as f:
            user_data = json.load(f)
            try:
                get_user_name = user_data['name']
            except KeyError:
                return False
            if get_user_name:
                return True
    elif not does_file_exist:
        return False

def access_user_data():
    """Access user data."""
    selection = input("1 - Näytä käyttäjätiedot\n2 - Muuta käyttäjätietoja\n")
    if selection == str(1):
        #Print user data.
        filename = 'data/user_data.json'
        with open(filename) as f:
            user_data = json.load(f)
            print(f"Nimi: {user_data['name']}")
            print(f"Pituus: {user_data['height']}")
            print(f"Paino: {user_data['weight']}\n")
    elif selection == str(2):
        ask_user_data()
        