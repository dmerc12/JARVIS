from .speak import speak
import webbrowser

# Function for opening google
def open_google(): 
    statement = 'Opening...'
    print(statement)
    speak(statement)
    webbrowser.open('https://www.google.com')
