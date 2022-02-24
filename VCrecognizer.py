import speech_recognition as sr
import asasasasasasasasari as asa
import re
import math
import sender
import random
import json
# -*- coding: utf-8 -*-

r = sr.Recognizer()
mic = sr.Microphone()

def checkNotJP(word):
    JP = re.compile('[a-zA-Z0-9]+')
    return JP.search(word)

def sigmo(x):
    return 1/(1+math.exp((-1)*x))

def wing(positiveness):
    with open('communicate_VCrecog.json') as f:
        value = json.load(f)
    positive = value["positive"]
    awkward = value["awkward"]
    patapata = value["patapata"]
    print("positive-prev: ",positive)
    if positive:
        if positiveness <= 0.6:
            # positive to negative
            positive = False
            awkward = True
            num = 0
        elif positiveness >= 0.7:
            # positive continues
            num = sigmo(positiveness*10-5) # up to 0.9933
            positive = True
            if random.random() >= 0.75:
                patapata = True
        else:
            # positive to neutral
            num = positiveness - 0.2
            positive = True
    else:
        if positiveness >= 0.7:
            # negative to positive
            positive = True
            patapata = True
            num = positiveness
        elif positiveness <= 0.5:
            # negative continues
            num = sigmo(positiveness*10-5) # down to 0.0067
            positive = False
        else:
            # negative to neutral
            num = positiveness - 0.1
            positive = False
    print("positive-now:  ",positive)
    data_write = {"num":float(num),"patapata":patapata,"awkward":awkward,"positive":positive}
    with open('communicate_VCrecog.json','w') as f:
        json.dump(data_write,f)

def main():
    while True:
        
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("----------listening...----------")
            audio = r.listen(source, phrase_time_limit=5)

        try:
            passage = r.recognize_google(audio, language='ja-JP')
            print(passage)
            ana = asa.analyze(passage)
            positiveness = ana[1]
            wing(positiveness)
            #sigmo(positiveness*10 - 5)

        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__" :
    main()