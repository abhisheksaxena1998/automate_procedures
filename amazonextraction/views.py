def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
import warnings 
import pandas as pd
import numpy as np
from sklearn.externals import joblib

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def result(request):
    #nm="amazonextraction\\az_joy_corpus.txt" #request.GET['url']
    #"az_joy_corpus.txt"
    nm=request.GET['url']
    nm="amazonextraction/" + nm
    sample = open(nm, "r",encoding='utf-8') 
    s = sample.read() 

    # Replaces escape character with space 
    f = s.replace("\n", " ") 

    from os import path
    from PIL import Image
    from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
    import matplotlib.pyplot as plt
    #% matplotlib inline
    stopwords= set(STOPWORDS)

    stopwords.update(["status","still","must","support","",'pretty','mmine','loud','amazon','stays','anything','mine','month','proper','listen','written','box' ,"public","last","read","johnson","didn","ve","put","needs","save","help","deal","tories","years","articles","need","back","government","pm","back","life","care","everyone","give","day","country","new","look","mps","everything","really","need","hard","believe","even","still","re","eu","pic","dlidington", "philiphammonduk","jeremy_hunt","may","theresa_may","alanduncanmp","watson","work",'don', "anna_soubry","voted","heidi","constituents","heidiallen","claiming","yasmin","george_osborne","ayeshahazarika","tom","conservatives","griffith","hear","tory", "twitter","amberrudduk","love","take","real","friend","good","conservative","election","right","tell","vote","sure","parliament",'people',"justinegreening","tom_watson","labour","time","party","think","going","set","lines","nickymorgan","amberruddhr","will","one","brexit","say","mp","said","want","come","well","no","see","now","know","borisjohnson","stephentwigg","please","happy","share","remember","thank","much","constituent","spaces","job","action","got","jbl",'sound','product','speaker','rha','gya','high','hai',"today",'ho','go','ll','amazes','working','thing','laptop','gaya','raha','purchase','bluetooth','speakers','amazing','compactness','connect'])

    wordcloud = WordCloud(
                            background_color='black',
                            stopwords=stopwords,
                            max_words=200,
                            max_font_size=150, width=1000, height=450,
                            random_state=42
                            ).generate(f)
    print(wordcloud)
    plt.figure(figsize = (10, 10), facecolor = None) 
    fig = plt.figure(1)
    plt.imshow(wordcloud)
    plt.tight_layout(pad=0)

    plt.axis('off')
    plt.show()
    fig.savefig("static\\cloud_amazon3.png", bbox_inches='tight')
    plt.savefig('static\\cloud_amazon.png', facecolor='k', bbox_inches='tight')

    #loaded_model = joblib.load('amazonextraction\\emotion_model.sav')
    #result = loaded_model.predict([nm])
    #print (result)    

    return render(request,'result.html',{'result':'Real-time analysis successfull','url':nm})

def about(request):
    return render(request,'about.html')    