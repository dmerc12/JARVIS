from ..utils.command import take_command
from ..utils.speak import speak
import urllib.parse
import webbrowser

# Function for opening google
def open_google():
    statement = 'Opening...'
    print(statement, flush=True)
    speak(statement)
    webbrowser.open('https://www.google.com')

# Function for seaerching google
def search_google():
    response = 'Yes sir, what should I search?'
    print(response, flush=True)
    speak(response)
    query = take_command().lower()
    encoded_query = urllib.parse.quote(query)
    webbrowser.open(f'https://www.google.com/search?q={encoded_query}')
    response = 'Here are your search results'
    print(response, flush=True)
    speak(response)
