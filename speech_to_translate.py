import speech_recognition as sr
import pyttsx3
import translators as ts
import time
import sys
import os


#initializing Speech Recognition Engine
recog = sr.Recognizer()
#initializing Speech-To-Text Engine
spkEng = pyttsx3.init()

print('\n-------------------------------------------------')
print(ts.google('Hello!', from_language='en', to_language='pl'))
print(ts.google('Hello!', from_language='en', to_language='zh-CN'))

loopNo = 1

try:
    while True:

        #printing the 3-2-1 decrementing loop
        for i in range(3, 0, -1):
            time.sleep(0.6)
            print(str(i)+"..")

        with sr.Microphone() as mic:
            print("["+str(loopNo)+"]", end=" ")
            print("Start speaking...       (press CTRL+C to Stop or say 'FINISH')")
            #adjusts the threshold from the source and records from the source (microphone)
            recog.adjust_for_ambient_noise(mic, duration=0.6)
            audio = recog.listen(mic, phrase_time_limit=5)

            try:
                #performs speech recognition using Google SR API
                text = recog.recognize_google(audio, language="en-US")
                text = text.lower()
                print(f"Recognized: {text}")

                #kills the program if user says 'finish'
                if text == "finish" or text=="finished":
                    print('Ending script..')
                    break

                #speaks out the phrase caught by the SR
                spkEng.say(text)
                spkEng.runAndWait()

                #translates the phrase
                transPL = ts.google(text, from_language='en', to_language='pl')
                print(f"POLISH: "+transPL)
                transCN = ts.google(text, from_language='en', to_language='zh-CN')
                print(f"CHINESE: "+transCN)
                print('-------------------------------------------------\n')

            #saves the script from breaking in case of SR error
            except sr.UnknownValueError:
                print('Recognition Error! Try again..')
                continue

            loopNo += 1

#kills the script upon pressing 'CTRL-C'
except KeyboardInterrupt:
    print('Script stopped..')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
