from commands.command import take_command, listen_for_name
from commands.greeting import greeting, initial_greeting
from commands.personal_questions.name import speak_name
from commands.personal_questions.default import default
from commands.personal_questions.kenobi import kenobi
from commands.google import search_google, open_google
from commands.stop_jarvis import stop_jarvis

# Main function for running JARVIS
if __name__ == '__main__':

    # Sets variables for initial startup and listening
    initial = True
    listening = False

    # Infinite loop to have JARVIS running while program is running
    while True:

        # Greet user on startup
        if initial:
            initial_greeting()
            initial = False

        # Listen for the name 
        while True:
            if listen_for_name():
                listening = True
                greeting()
                break

        # Listen for a command
        while True:
            query = take_command().lower()

            shutdown_commands = ['shut down', 'shutdown', 'power down', 'power off', 'power cycle']
            name_questions = ['who are you', "what's your name", 'what is your name', 'what are you called', "what're you called"]

            if 'hello there' in query:
                kenobi()
            elif any(command in query for command in shutdown_commands):
                stop_jarvis()
            elif 'are you there' in query:
                default()
            elif any(question in query for question in name_questions):
                speak_name()
            elif 'open google' in query:
                open_google()
            elif 'search google' in query:
                search_google()

            # Sets listening back to false to await name again
            listening = False
            break
