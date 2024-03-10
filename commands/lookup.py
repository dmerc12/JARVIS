from wikipedia.exceptions import PageError, DisambiguationError
from .speak import speak
import wikipedia

# Function for looking up definitions and other things on wikipedia
def lookup(query): 
    speak('Searching...')
    query = query.replace('what is', '')
    try:
        results = wikipedia.summary(query, sentences=2)
        response = 'According to Wikipedia'
        print(response)
        speak(response)
        print(results)
        speak(results)
    except DisambiguationError as e:
        options = e.options[:5]  # Get the first 5 options
        error_message = f"Sorry, '{query}' is ambiguous. Here are some options:"
        for option in options:
            error_message += f"\n- {option}"
        print(error_message)
        speak(error_message)
    except PageError:
        error = f"Sorry, I couldn't find any information about '{query}' on Wikipedia"
        print(error)
        speak(error)
