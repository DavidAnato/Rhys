# greet.py
import pyttsx3
import random

def execute():
    engine = pyttsx3.init()

    greetings = [
        'Salut', 'Bonjour', 'Bonsoir', 'Coucou', 'Hey', 'Salutations', 'Hello',
        'Salut à toi', 'Salut l\'ami', 'Bien le bonjour', 'Salut tout le monde'
        # Ajoutez d'autres salutations en français
    ]

    phrases = [
        'comment je peux vous aider ?', 'Que puis-je faire pour vous ?',
        'Comment ça va aujourd\'hui ?', 'En quoi puis-je vous assister ?',
        'Besoin d\'aide pour quelque chose ?', 'Comment puis-je vous rendre service ?',
        'Salut ! Que puis-je faire pour vous ?', 'Bonjour ! Comment puis-je vous assister ?',
        'Hey ! Comment ça va ?', 'Bonjour à tous ! Qu\'est-ce que je peux faire pour vous ?',
        # Ajoutez d'autres phrases en français
    ]

    engine.say(f'{random.choice(greetings)}, {random.choice(phrases)}')
    engine.runAndWait()

if __name__ == '__main__':
    execute()
