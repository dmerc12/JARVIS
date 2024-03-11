from .speak import speak
import webbrowser

# Function for opening google
def open_google(): 
    speak('Opening...')
    webbrowser.open('https://www.google.com')
    