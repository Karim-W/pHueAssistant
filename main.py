#import library

import speech_recognition as sr
from phue import Bridge
b = Bridge('192.168.0.104')
# Initialize recognizer class (for recognizing the speech)

b.connect()
#b.set_light(1, 'on', False)
r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
command = False
while(True):
    print("hi\n")
    with sr.Microphone() as source:
        # print("Talk")
        audio_text = r.listen(source)
        # print("Time over, thanks")
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            f = r.recognize_google(audio_text)  # recognize_ibm(audio_text)
            if f == "hey Friday":
                command = True

                print("how can i help")
                while(command):
                    try:
                        audio_text = r.listen(source)
                        l = r.recognize_google(audio_text)
                        print("Text: "+l)
                        if l == "turn on the light":
                            b.set_light(1, 'on', True)
                            command = False
                            break
                        elif l == "turn off the lights":
                            b.set_light(1, 'on', False)
                            command = False
                            break
                    except:
                        command = False
        except:
            print("nothing")
