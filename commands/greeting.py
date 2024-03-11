from datetime import datetime
from .speak import speak

# Greeting function for initially greeting user
def initial_greeting():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour <= 12:
        greeting = 'good morning sir'
        print(greeting)
        speak(greeting)
    elif hour >= 12 and hour <= 17:
        greeting = 'good afternoon sir'
        print(greeting)
        speak(greeting)
    else:
        greeting = 'good evening sir'
        print(greeting)
        speak(greeting)

# Greeting function for greeting user
def greeting():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour <= 12:
        greeting = 'good morning sir, how may I be of assistance?'
        print(greeting)
        speak(greeting)
    elif hour >= 12 and hour <= 17:
        greeting = 'good afternoon sir, how may I be of assistance?'
        print(greeting)
        speak(greeting)
    else:
        greeting = 'good evening sir, how may I be of assistance?'
        print(greeting)
        speak(greeting)
    