import tkinter as tk
import math
import threading
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()

# API Keys
newsapi_key = "940495ad4b3b454ab2fcfa738eafea08"
weather_api_key = "152d8982aa1aecf2ec86fa224988179b"

# Function to speak text aloud
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Backend function to process commands
def process_command(command, root):
    command = command.lower()

    # Exit or stop command
    if "exit" in command or "stop" in command:
        speak("Goodbye, closing the assistant.")
        root.quit()  # This will stop the Tkinter mainloop and exit the program.
        return

    # Other commands
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open telegram" in command:
        speak("Opening Telegram")
        webbrowser.open("https://web.telegram.org")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "open whatsapp" in command:
        speak("Opening whatsapp")
        webbrowser.open("https://whatsapp.com")
    elif "news" in command:
        try:
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi_key}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                articles = data.get('articles', [])
                if articles:
                    speak("Here are the top headlines")
                    for i, article in enumerate(articles[:5]):
                        title = article.get('title', 'No title available')
                        speak(f"News {i+1}: {title}")
                else:
                    speak("I couldn't find any news at the moment.")
            else:
                speak("Failed to fetch the news. Please try again later.")
        except Exception as e:
            speak("There was an error fetching the news.")
    elif "weather" in command:
        try:
            city = command.split("weather in")[-1].strip()
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                main = data.get('main', {})
                weather = data.get('weather', [{}])[0]
                temperature = main.get('temp', 'N/A')
                description = weather.get('description', 'No description available')
                speak(f"The temperature in {city} is {temperature} degrees Celsius with {description}.")
            else:
                speak("Could not fetch the weather data.")
        except Exception as e:
            speak("There was an error fetching the weather.")
    elif "wikipedia" in command:
        try:
            topic = command.replace("wikipedia", "").strip()
            summary = wikipedia.summary(topic, sentences=1)
            speak(f"According to Wikipedia: {summary}")
        except wikipedia.exceptions.DisambiguationError as e:
            speak("There are multiple results. Could you be more specific?")
        except wikipedia.exceptions.HTTPTimeoutError:
            speak("There was a timeout error while fetching the Wikipedia data.")
        except Exception as e:
            speak("Sorry, I couldn't fetch information from Wikipedia.")
    elif "calculate" in command:
        try:
            command = command.replace("calculate", "").strip()
            result = eval(command)
            speak(f"The result is {result}")
        except Exception as e:
            speak("Sorry, I couldn't perform the calculation.")
            print(f"Error calculating: {e}")

# Function to listen for voice commands continuously
def listen_for_commands(root):
    recognizer = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for the activation word....")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes Sir, I am listening")
                with sr.Microphone() as source:
                    print("Jarvis is active. Listening for your command.")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                    command = recognizer.recognize_google(audio)
                    process_command(command, root)

        except sr.WaitTimeoutError:
            print("Listening timed out. No input detected.")
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            speak("I couldn't understand that. Could you please repeat?")
        except sr.RequestError as e:
            print(f"API error: {e}")
            speak("There is an issue with the speech recognition service.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            speak("An unexpected error occurred. Please try again.")

# Function to create the arc reactor design
def create_arc_reactor(canvas, x, y, radius):
    for glow in range(15):
        canvas.create_oval(
            x - radius - glow, y - radius - glow,
            x + radius + glow, y + radius + glow,
            fill="", outline=f"#{255 - glow * 15:02x}{255 - glow * 15:02x}ff",
            width=2,
        )
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="#000022", outline="#88ccff", width=4)
    inner_radius = radius * 0.7
    canvas.create_oval(x - inner_radius, y - inner_radius, x + inner_radius, y + inner_radius, fill="#ffffff", outline="")
    for angle in range(0, 360, 30):
        angle_rad = math.radians(angle)
        x1 = x + math.cos(angle_rad) * (radius * 0.8)
        y1 = y + math.sin(angle_rad) * (radius * 0.8)
        x2 = x + math.cos(angle_rad) * radius
        y2 = y + math.sin(angle_rad) * radius
        canvas.create_line(x1, y1, x2, y2, fill="#88ccff", width=2)

# Main function to create the GUI
def main():
    root = tk.Tk()
    root.title("Jarvis Assistant")
    root.geometry("500x600")
    root.configure(bg="black")

    canvas = tk.Canvas(root, width=400, height=400, bg="black", highlightthickness=0)
    canvas.pack(pady=20)
    create_arc_reactor(canvas, 200, 200, 100)

    # Run the voice command listener in a separate thread
    threading.Thread(target=listen_for_commands, args=(root,), daemon=True).start()

    root.mainloop()

if __name__ == "__main__":
    main()
