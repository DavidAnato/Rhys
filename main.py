#main.py
import speech_recognition as sr
from commands import greet
import winsound
import sys
import pyttsx3

def beep_sound():
    # Utiliser winsound pour reproduire un son de bip
    winsound.Beep(1000, 500)  # fréquence de 1000 Hz, durée de 500 ms

def speak_text(text):
    # Utiliser pyttsx3 pour lire le texte à haute voix
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    greetings = ['salut', 'bonjour', 'bonsoir', 'coucou', 'hey']
    if any(greeting in command for greeting in greetings):
        greet.execute()
    else:
        # Ajouter ici d'autres commandes ou gestion des commandes non reconnues
        print('Commande non reconnue')
        speak_text('Désolé, je n\'ai pas compris votre commande.')

def launch_assistant():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        beep_sound()
        with microphone as source:
            print("Speak now:")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language='fr')
            print(f"Vous: {command}")
            process_command(command.lower())
        except sr.UnknownValueError:
            print("Je ne comprends pas.")
            speak_text("Je ne comprends pas.")
        except sr.RequestError as e:
            print(f"Google Speech Recognition requete echouer: {e}")
        except ConnectionAbortedError:
            print("Assurez-vous que votre appareil est connecté à Internet.")
            print("Le programme va maintenant se fermer.")
            speak_text("La reconnaissance vocale a échoué en raison d'un problème de connexion à Internet. Le programme va maintenant se fermer.")
            sys.exit()

if __name__ == '__main__':
    launch_assistant()
