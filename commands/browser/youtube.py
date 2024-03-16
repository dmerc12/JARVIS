from ..utils.command import take_command
from ..utils.speak import speak
import urllib.parse
import webbrowser

# Function for opening youtube
def open_youtube():
    statement = 'Opening...'
    print(statement, flush=True)
    speak(statement)
    webbrowser.open('https://www.youtube.com')

# Function for seaerching youtube
def search_youtube():
    response = 'Yes sir, what should I search?'
    print(response, flush=True)
    speak(response)
    query = take_command().lower()
    encoded_query = urllib.parse.quote(query)
    webbrowser.open(f'https://www.youtube.com/results?search_query={encoded_query}')
    response = 'Here are your youtube search results'
    print(response, flush=True)
    speak(response)
