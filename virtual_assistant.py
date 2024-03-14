'''Python-Virtual-assistant
'Virtual Assistant Version One' A python based programme that uses speech recognition and text-to-speech functions.Google text-to-speech API were used. (Only work when the system is online)
Your computer must be running Python3.9 or newer.

Below is the list of libraries that has been used. You must need to install all, before executing the program
pip install speechrecognition
pip install gTTS
pip install pyaudio
pip install playsound==1.2.2

pip install PyAudio'''


import speech_recognition as sr # recognise speech
import webbrowser # open browser
import time  
import playsound # to play an audio file
import random
import os
from gtts import gTTS # google text to speech
from time import ctime


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=False):

    with sr.Microphone() as source: # microphone as source
        r.energy_threshold=500             #voice level number increse more sensitive  
        r.adjust_for_ambient_noise(source,1.2)# noise cancel rate
        r.pause_threshold= 1
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
       
        try :
            voice_data = r.recognize_google(audio)  # convert audio to text
       
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        except sr.UnknownValueError: # error: recognizer does not understand
            print('Recognizing..')
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def speak(audio_string): 
    tts = gTTS(text=audio_string, lang='en-in') # text to speech(voice)
    r  = random.randint(1,20000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(audio_string) # print what app said
    os.remove(audio_file) # remove audio file
     
def respond(voice_data):
     
       # 1: greeting
    if there_exists(["hey","hi","hello","wake up","hai"]):
        greetings = ["hey", "hey, what's up? ", " how can I help you","I'm listening","hello"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    # 2: name
    if there_exists(["your name","what i call you","what is your good name"]):
        name= record_audio("my name is Vavo stand for virtual assistance version One. what's your name?")
        speak('Nice to meet you '+ name )
        speak('how can i help you ' + name)
  
        

  # 3: Origin
        
    if there_exists(["who are you","your inventor","invented you","created you","who is your developer"]):
        greetings = ["I am Virtual Voice Assistant","I am developed by mr.abhijeet as a voice assistance"] # You can Add your name
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    if there_exists(["what is your age","how old are you","when is your birthday"]):
        greetings = ["I came into this world in march 2021"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)
        

    # 3: Take care's 
    if there_exists(["how's everything" ,"how ia everything","how are you","how are you doing","what's up","whatsup"]):
        greetings = ["I am well ...thanks for asking ","i am well" ,"Doing Great" ]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)
        
        
    # 3: greeting
    if there_exists(["What are you doing" ,"what you doing","doing"]):
        greetings = ["nothing", "nothing...,just working for you","Nothing much"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)


         # 4.1: time
    if there_exists(["what's  the time","tell me the time","what time is it","what is the time","time is going on"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)
    
          # 5: search wekiapedia
    if there_exists(["wikipedia"]):
        search = record_audio('What do you want to search for?')
        url = 'https://en.wikipedia.org/wiki/'+ search
        webbrowser.get().open(url)
        speak('Here is what I found for' + search)

    # 5: search 
    if there_exists(["do google","search google","on google","search for","in google"]):
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q='+ search
        webbrowser.get().open(url)
        speak('Here is what I found for' + search)

      # 5.6: opening youtube
    if there_exists(["open the youtube","open youtube"]):
        url = 'https://www.youtube.com/'
        webbrowser.get().open(url)
        speak('Opening')
     
      # 5.7: opening google
    if there_exists(["open the  google","open google"]):
        url = 'https://www.google.com/'
        webbrowser.get().open(url)
        speak('Opening')
         # 5.7: opening gemail
    if there_exists(["open gmail","open email","open my email","check email"]):
        url = 'https://mail.google.com/'
        webbrowser.get().open(url)
        speak('Opening')
        
    # 5.5: find location 
    if there_exists(["location"]):
        location = record_audio('What is the locatio n?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Opening map of' + location )


    # 6: search youtube
    if there_exists(["search youtube","search the youtube","search in youtube","in youtube","on youtube"]):
        search = record_audio('What do you want to search for?')
        r.pause_threshold=2
        url = 'https://www.youtube.com/results?search_query='+search
        webbrowser.get().open(url)
        speak('Here is what I found')



        #OS shutdown
    if  there_exists(["shutdown system","system off","shutdown the system","system shutdown"]):
        speak('Okay system will off in 30 seconds')
        os.system("shutdown /s /t 30")
         

    if there_exists(["good","thank you","thanks","well done"]):
       greetings = ["my pleasure","Don't mention","Thanks for your compliment","No problem.","Thank you, it makes my day to hear that."]
       greet = greetings[random.randint(0,len(greetings)-1)]
       speak(greet)


    if there_exists(["exit", "quit","sleep","shut up","close"]):
       greetings = ["Going offline ! you can call me Anytime","Okay ,you can call me Anytime","See you later","See you soon","Have a good day."]
       greet = greetings[random.randint(0,len(greetings)-1)]
       speak(greet)
       exit()

time.sleep(1)
while(1):
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond


