from pain import Pain
import json
from datetime import date
from datetime import datetime
import os
import os.path

cwd = os.getcwd()
os.chdir(cwd + '/')

def log_pain():
    """Add a new pain."""
    #Log a new pain to the pain history.
    while True:
        body_part = get_body_part(input("Mihin sattuu:\n1 - Niska\n2 - Hartia\n3 - Pää\n4 - Kuukautiskipu\n5 - Kirjaa oma kipu\n"))
        if body_part == 'not_valid':
            print("Valintaa ei tunnistettu.")
            continue
        else:
            break   
    
    while True:
        strength = verify_strength(input("Kuinka kova kipu on asteikolla 1-10.\n"))
        if strength == 'not_valid':
            print("Kivun lujuusarvo ei vastaa annettua asteikkoa.")
            continue
        else:
            break
    
    #Create a new pain object, though not neccessary in this case. 
    pain = Pain(body_part, strength)

    pain_history = []

    filename = 'data/pain_history.json'
    with open(filename) as f:
        pain_history = json.load(f)

    #Get current date.
    #current_date = date.today().isoformat()
    current_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    #current_date = current_date.strftime("%d/%m/%Y, %H:%M:%S")

    pain_history.append({
        'body_part': pain.body_part,
        'strength': pain.strength,
        'date': current_date
    })

    with open(filename, 'w') as f:
        json.dump(pain_history, f, indent=4)


def get_body_part(selection):
    """Get body part selected by user."""
    #Get body part according to user selection.
    match int(selection):
        case 1:
            return 'niska'
        case 2:
            return 'hartia'
        case 3:
            return 'pää'
        case 4:
            return 'kuukautiskipu'
        case 5:
            return input('Anna vapaavalintainen kivun nimi:\n')
        case _:
            return 'not_valid'

def verify_strength(selection):
    """Verify strength validity."""
    #Check if pain strength is between 1 and 10. If more or less, assign a default value.
    if int(selection) > 10 or int(selection) < 1:
        return 'not_valid'
    else:
        return selection