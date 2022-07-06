from user import User
import json
import os
import os.path
import user_data
import log_pain
import pain_history

#os.chdir(r'...')

cwd = os.getcwd()
os.chdir(cwd + '/')
print(f"Current dir {cwd}")

#Check if user data file exists and if it has data.
check_user_data = user_data.check_user_data()

#If user data is not found, go to first launch. Else, greet user.
if not check_user_data:
    print("Tervetuloa käyttämään Mihin sattuu? -sovellusta.\n")
    user_data.ask_user_data()
else:
    filename = 'data/user_data.json'
    with open(filename) as f:
        user_info = json.load(f)
        print(f"Tervetuloa takaisin, {user_info['name']}\n")

while True:
    selection = input("Mitä haluat tehdä?\n1 - Kirjaa kipu\n2 - Kipuhistoria\n3 - Käyttäjätiedot\n4 - Sammuta ohjelma\n")

    if selection == str(1):
        print("Kirjaa kipu valittu.\n")
        log_pain.log_pain()
        continue
    elif selection == str(2):
        print("Kipuhistoria valittu.\n")
        pain_history.select_pain_history_type()
        continue
    elif selection == str(3):
        print("Käyttäjätiedot valittu.\n")
        user_data.access_user_data()
        continue
    elif selection == str(4):
        #Quit program.
        print("Ohjelma lopetettu.")
        break
    else:
        print("Valintaa ei tunnistettu. Yritä uudelleen.\n")
        continue

#Program terminated.