from datetime import datetime
from .speak import speak

# Greeting function for initially greeting user
def initial_greeting():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour <= 12:
        greeting = 'Good morning sir'
        print(greeting, flush=True)
        speak(greeting)
    elif hour >= 12 and hour <= 17:
        greeting = 'Good afternoon sir'
        print(greeting, flush=True)
        speak(greeting)
    else:
        greeting = 'Good evening sir'
        print(greeting, flush=True)
        speak(greeting)

# Greeting function for greeting user
def greeting():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour <= 12:
        greeting = 'Good morning sir, how may I be of assistance?'
        print(greeting, flush=True)
        speak(greeting)
    elif hour >= 12 and hour <= 17:
        greeting = 'Good afternoon sir, how may I be of assistance?'
        print(greeting, flush=True)
        speak(greeting)
    else:
        greeting = 'Good evening sir, how may I be of assistance?'
        print(greeting, flush=True)
        speak(greeting)
