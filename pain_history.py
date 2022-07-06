import json
import plotly.graph_objects as go
import plotly.express as px
from log_pain import get_body_part
import os
import os.path

cwd = os.getcwd()
os.chdir(cwd + '/')

def create_graph(pains, strengths):
    """Graphic showing pain history."""
    my_layout = {
        'title': 'Kipuhistoria',
        'titlefont': {'size': 25},
        'xaxis': {
            'title': 'Kipu ja aika',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14}
        },
        'yaxis': {
            'title': 'Kivun lujuus',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14}
        }
    }

    fig = go.Figure(
        data=[go.Bar(
            y=strengths,
            x=pains
        )],
        layout=my_layout
        #layout_title_text = "Test"
    )

    fig.show()

def create_pie_chart(pains):
    """Create pie chart view."""
    fig = px.pie(names=pains, title='Piirakka')
    fig.show()

def pie_chart_view():
    """Get data for pie chart view showing how much each body part has experienced pain."""
    pains = []
    filename = 'data/pain_history.json'
    with open(filename) as f:
        pain_history = json.load(f)

        for pain in pain_history:
            pains.append(f"{pain['body_part'].title()}")
    create_pie_chart(pains)

def selected_pain_history(selection):
    """Get data for selected body part."""
    pains, strengths = [], []
    filename = 'data/pain_history.json'
    with open(filename) as f:
        pain_history = json.load(f)

        for pain in pain_history:
            if pain['body_part'] == selection:
                pains.append(f"{pain['body_part'].title()} {pain['date']}")
                strengths.append(int(pain['strength']))

        create_graph(pains, strengths)

def pain_history():
    """Get data of whole pain history."""
    pains, strengths, dates = [], [], []
    filename = 'data/pain_history.json'
    with open(filename) as f:
        pain_history = json.load(f)

        for pain in pain_history:
            try:
                print(f"Mihin sattui: {pain['body_part'].title()}", end = ' ')
                pains.append(f"{pain['body_part'].title()} {pain['date']}")
            except KeyError:
                print("Mihin sattui: Tieto puuttuu.", end = ' ')
            except ValueError:
                print("Mihin sattui: Tieto puuttuu.", end = ' ')
            except AttributeError:
                print("Mihin sattui: Tieto puuttuu.", end = ' ')

            try:
                print(f"\tKivun lujuus: {pain['strength']}", end = ' ')
                strengths.append(int(pain['strength']))
            except KeyError:
                print("\tKivun lujuus: Tieto puuttuu.", end = ' ')
            except ValueError:
                print("\tKivun lujuus: Tieto puuttuu.", end = ' ')
            except AttributeError:
                print("\tKivun lujuus: Tieto puuttuu.", end = ' ')

            try:
                print(f"\tPäivä: {pain['date']}")
                dates.append(pain['date'])
            except KeyError:
                print("\tPäivä: Tieto puuttuu.")
            except ValueError:
                print("\tPäivä: Tieto puuttuu.")
            except AttributeError:
                print("\tPäivä: Tieto puuttuu.")

        create_graph(pains, strengths)

def select_pain_history_type():
    """Select how the pain history is displayed."""
    selection = input("Valitse esitystapa:\n1 - Koko kipuhistoria\n2 - Piirakkanäkymä\n3 - Niska\n4 - Hartia\n5 - Pää\n6 - Kuukautiskipu\n")
    if selection == str(1):
        pain_history()
    elif selection == str(2):
        pie_chart_view()
    else:
        selected_pain_history(get_body_part(int(selection)))


            
        