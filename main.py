from commands.personal_questions.name import speak_name
from commands.personal_questions.default import default
from commands.personal_questions.kenobi import kenobi
from commands.search_google import search_google
from commands.open_google import open_google
from commands.stop_jarvis import stop_jarvis
from commands.command import take_command
from commands.greeting import greeting

# Main function for running JARVIS
if __name__ == '__main__':
    # Set initial variable for inital greeting
    initial = True
    
    # Infinite loop to have JARVIS running while program is running
    while True:
        # Greet user on startup
        if initial == True:
            initial = False
            greeting()
        
        # Listen for command and return command
        query = take_command().lower()

        # Sets up lists of trigger commands
        defaults = ['jarvis', 'are you there']
        shutdown_commands = ['shut down', 'shutdown', 'power down', 'power off', 'power cycle']
        name_questions = ['who are you', "what's your name", 'what is your name', 'what are you called', "what're you called"]
        
        # Secret response for General Kenobi
        if 'hello there' in query:
            kenobi()

        # Reponse to stop JARVIS
        elif any(command in query for command in shutdown_commands):
            stop_jarvis()
            break
        # Response for default
        elif any(default in query for default in defaults):
            default()
        # Response for name questions
        elif any(question in query for question in name_questions):
            speak_name()
        # Response for opening google
        elif 'open google' in query:
            open_google()
        # Response fo r searching google
        elif 'search google' in query:
            search_google()
