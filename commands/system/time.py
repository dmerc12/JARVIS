from ..utils.command import take_command
from ..utils.speak import speak
from datetime import datetime

# Function to tell the current time
def tell_time():
    current_time = datetime.now().strftime("%I:%M %p")
    response = f'It is {current_time}'
    print(response, flush=True)
    speak(response)

# Function to tell the current time in a particular location
