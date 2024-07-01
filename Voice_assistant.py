import speech_recognition as sr   
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text) :
     engine.say(text)
     engine.runAndWait()
     
def listen() :
     with sr.Microphone() as source :
          print("Listening...")
          audio = recognizer.listen(source)
          command = recognizer.recognize_google(audio)
          print(f"You said : {command}")
          return command.lower()
     

# Respond to Greetings 
def respond_to_hello() :
     speak("Hello ! How can I help You ?")
     
# Function to tell Current Time
def tell_time() :
     now = datetime.datetime.now().strftime("%H : %M")
     speak(f"The time is {now}")
     
# Duction to tell current Date 
def tell_date() :
     today = datetime.date.today().strftime("%B %d, %Y")
     speak(f"Today's date is {today}")
     


# Searching Web
def search_web(query) :
     now = datetime.date.today().strftime("%B %d, %Y")
     speak(f"Searching the web for {query}")
     webbrowser.open(f"https://www.google.com/search?q={query}")
     

#processing Commands
def process_command(command) :
     if "hello" in command :
          respond_to_hello()
          
     elif "time" in command :
          tell_time()
          
     elif "date" in command :
          tell_date()
          
     elif "search for" in command :
          search_query = command.replace("search for", "").strip()
          search_web(search_query)
          
     else :
          speak("I don't know that command !")
          
# Main Loop
def main() :
     speak ("Voice assistant activated. Say 'hello' to start.")
     
     while True : 
          command = listen()
          process_command(command)
          
if __name__ == "__main__" :
     main()
     