# Translation_Multi_Tool_Bot

Translation Multi-Tool Bot (v1.0)

![speech_to_translate](https://user-images.githubusercontent.com/88622607/135081092-7464673c-a8d0-4c8b-94e0-9583c679bb8f.gif)

One of my first Python scripts. This particular tool is aimed at helping language learners by translating a sentence caught via speech recognition. 
It consists of 3 modules:
- speech_recognition
*(users might additionally need to install the **pyaudio** module to make the script run properly)*
- pyttsx3 *(python text-to-speech)*
- translators

The script starts by asking us to speak (uses Google Speech Recognition API, but can be changed to a different one), then it’ll catch the text and view it in the next line. Then, it’ll be transformed into speech and played back. Finally, it’ll be translated into two languages (set to PL and CHN by default).

Additional code guardians:
- *KeyboardInterrupt* exception outside the main loop allows to terminate the code at any moment
- *UnknownValue* Error from the **speech_recognition** module helps to continue the code if the speech was not properly recognized

Some updates planned to be added later on.
