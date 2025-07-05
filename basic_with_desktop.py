# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 16:17:31 2017

@author: waqas
"""

import tkinter  as tk
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from lxml import etree
from nltk.stem import WordNetLemmatizer
import re

def display():
    txt.delete(0.0,'end')
    dis=ent.get()
    example_sent=dis.lower()
    
    example_sent = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', example_sent)
    copy_example=example_sent
    for char in example_sent:
        if char in "!@#$%^&*,.';?/\:|1234567890":
            example_sent = example_sent.replace(char,'')
    
    ##tokken generation and removing useless part      
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(example_sent)
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)        
    
    i=0
#print(t)
    sentence=copy_example.split(' ')
    
    neg=["no","not","never","don't","doesn't","didn't","haven't","hasn't","couldn't","wouldn't","can't","aren't","isn't","wasn't"]        
    negation=False 
    for a in neg: 
        for b in sentence:
            if(a==b):
                negation=True
                #            print("found")
                break
        if(negation==True):
                break
            
    def remove_duplicates(values):
        output = []
        seen = set()
        for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
            if value not in seen:
                output.append(value)
                seen.add(value)
        return output
    
    filtered_sentence = remove_duplicates(filtered_sentence)
    
     ##port of speech tagging   
    stemming=nltk.pos_tag(filtered_sentence)
    
    s0 = []
    s1 = []
    for i in stemming:
        s0.append(i[0])
        s1.append(i[1])
    
#pos_tag converting into class 
#n noun
#v verb
#a adjuctive
#r adverb
#s adjuctive satalite   

    for w in range(len(s1)):
         if (s1[w] == "JJ" or s1[w] == "JJR" or s1[w] == "JJS"):
               s1[w] = "a"
         elif (s1[w] == "NN" or s1[w] == "NNP" or s1[w] == "NNPS" or s1[w] == "NNS"):
             s1[w] = "n"
         elif (s1[w] == "RB" or s1[w] == "RBR" or s1[w] == "RBS"):
             s1[w] = "r"
         elif (s1[w] == "VB" or s1[w] == "VBD" or s1[w] == "VBG" or s1[w] == "VBN" or s1[w] == "VBP" or s1[w] == "VBZ"):
             s1[w] = "v"
         else:
            s1[w] = "v"
            
            
    lemmatizer = WordNetLemmatizer()
    temp=[]
    for w in range(len(s0)):
        temp.append(lemmatizer.lemmatize(s0[w], pos=s1[w]))    
#    print(temp)    
        
    synonyms = []
    length=[] 
#    total_words=len(s0)
    synsets_store=[]
    n=0
    #synsets  finding 
    for w in range(len(s0)):
        synonyms = wordnet.synsets(temp[w],s1[w])
        for synset in synonyms:
            synsets_store.append(synset.name().split('.')[0])
            n+=1
        length.append(n)
        n=0

    synsets_store=remove_duplicates(synsets_store)
    print(synsets_store)
    
    data = """<categ-list>

              <categ name="root"/>

              <categ name="mental-state" isa="root"/>
              <categ name="physical-state" isa="root"/>
              <categ name="behaviour" isa="root"/>
              <categ name="situation" isa="root"/>
              <categ name="signal" isa="root"/>
              <categ name="trait" isa="root"/>
              <categ name="sensation" isa="root"/>

              <categ name="cognitive-state" isa="mental-state"/>
              <categ name="affective-state" isa="mental-state"/>
              <categ name="cognitive-affective-state" isa="mental-state"/>

              <categ name="mood" isa="affective-state"/>
              <categ name="emotion" isa="affective-state"/>

              <categ name="emotion-eliciting-situation" isa="situation"/>

  <categ name="edonic-signal" isa="signal"/>

  <categ name="positive-emotion" isa="emotion"/>
  <categ name="negative-emotion" isa="emotion"/>
  <categ name="neutral-emotion" isa="emotion"/>
  <categ name="ambiguous-emotion" isa="emotion"/>

  <categ name="joy" isa="positive-emotion"/>
   <categ name="happy" isa="positive-emotion"/>
  <categ name="love" isa="positive-emotion"/>
  <categ name="affection" isa="positive-emotion"/>
  <categ name="liking" isa="positive-emotion"/>
  <categ name="enthusiasm" isa="positive-emotion"/>
  <categ name="gratitude" isa="positive-emotion"/>
  <categ name="self-pride" isa="positive-emotion"/>
  <categ name="levity" isa="positive-emotion"/>
  <categ name="calmness" isa="positive-emotion"/>
  <categ name="fearlessness" isa="positive-emotion"/>
  <categ name="positive-expectation" isa="positive-emotion"/>
  <categ name="positive-fear" isa="positive-emotion"/>
  <categ name="positive-hope" isa="positive-emotion"/>

  <categ name="amusement" isa="joy"/>
  <categ name="elation" isa="joy"/>
  <categ name="exultation" isa="joy"/>
  <categ name="exhilaration" isa="joy"/>
  <categ name="exuberance" isa="joy"/>
  <categ name="happiness" isa="joy"/>
  <categ name="bonheur" isa="joy"/>
  <categ name="gladness" isa="joy"/>
  <categ name="merriment" isa="joy"/>
  <categ name="rejoicing" isa="joy"/>
  <categ name="belonging" isa="joy"/>
  <categ name="cheerfulness" isa="joy"/>
  <categ name="contentment" isa="joy"/>

  <categ name="euphoria" isa="elation"/>

  <categ name="triumph" isa="exultation"/>

  <categ name="bang" isa="exhilaration"/>
  <categ name="titillation" isa="exhilaration"/>

  <categ name="hilarity" isa="merriment"/>
  <categ name="jocundity" isa="merriment"/>
  <categ name="jollity" isa="merriment"/>

  <categ name="comfortableness" isa="belonging"/>
  <categ name="closeness" isa="belonging"/>

  <categ name="togetherness" isa="closeness"/>

  <categ name="buoyancy" isa="cheerfulness"/>
  <categ name="carefreeness" isa="cheerfulness"/>

  <categ name="satisfaction" isa="contentment"/>

  <categ name="satisfaction-pride" isa="satisfaction"/>
  <categ name="complacency" isa="satisfaction"/>
  <categ name="fulfillment" isa="satisfaction"/>
  <categ name="gloat" isa="satisfaction"/>

  <categ name="smugness" isa="complacency"/>

  <categ name="attachment" isa="affection"/>
  <categ name="protectiveness" isa="affection"/>
  <categ name="regard" isa="affection"/>
  <categ name="soft-spot" isa="affection"/>

  <categ name="simpathy" isa="liking"/>
  <categ name="fondness" isa="liking"/>
  <categ name="captivation" isa="liking"/>
  <categ name="preference" isa="liking"/>
  <categ name="friendliness" isa="liking"/>
  <categ name="approval" isa="liking"/>
  <categ name="admiration" isa="liking"/>

  <categ name="positive-concern" isa="sympathy"/>
  <categ name="kindheartedness" isa="sympathy"/>
  <categ name="compatibility" isa="sympathy"/>
  <categ name="empathy" isa="sympathy"/>

  <categ name="softheartedness" isa="positive-concern"/>

  <categ name="identification" isa="empathy"/>

  <categ name="weakness" isa="preference"/>

  <categ name="amicability" isa="friendliness"/>
  <categ name="good-will" isa="friendliness"/>
  <categ name="brotherhood" isa="friendliness"/>

  <categ name="favor" isa="approval"/>

  <categ name="hero-worship" isa="admiration"/>

  <categ name="gusto" isa="enthusiasm"/>
  <categ name="eagerness" isa="enthusiasm"/>
  <categ name="exuberance" isa="enthusiasm"/>

  <categ name="enthusiasm-ardor" isa="eagerness"/>

  <categ name="worship" isa="love"/>
  <categ name="love-ardor" isa="love"/>
  <categ name="amorousness" isa="love"/>
  <categ name="puppy-love" isa="love"/>
  <categ name="devotion" isa="love"/>
  <categ name="benevolence" isa="love"/>
  <categ name="lovingness" isa="love"/>
  <categ name="loyalty" isa="love"/>

  <categ name="beneficence" isa="benevolence"/>

  <categ name="warmheartedness" isa="lovingness"/>

  <categ name="gratefulness" isa="gratitude"/>

  <categ name="self-esteem" isa="self-pride"/>
  <categ name="ego" isa="self-pride"/>
  <categ name="amour-propre" isa="self-pride"/>

  <categ name="playfulness" isa="levity"/>

  <categ name="placidity" isa="calmness"/>
  <categ name="coolness" isa="calmness"/>
  <categ name="tranquillity" isa="calmness"/>

  <categ name="peace" isa="tranquillity"/>
  <categ name="easiness" isa="tranquillity"/>

  <categ name="positive-languor" isa="easiness"/>

  <categ name="security" isa="fearlessness"/>

  <categ name="confidence" isa="security"/>

  <categ name="anticipation" isa="positive-expectation"/>

  <categ name="positive-suspense" isa="anticipation"/>

  <categ name="frisson" isa="positive-fear"/>

  <categ name="hopefulness" isa="positive-hope"/>
  <categ name="encouragement" isa="positive-hope"/>
  <categ name="optimism" isa="positive-hope"/>

  <categ name="sanguinity" isa="optimism"/>

  <categ name="negative-fear" isa="negative-emotion"/>
  <categ name="sadness" isa="negative-emotion"/>
  <categ name="sad" isa="negative-emotion"/>
  <categ name="general-dislike" isa="negative-emotion"/>
  <categ name="ingratitude" isa="negative-emotion"/>
  <categ name="shame" isa="negative-emotion"/>
  <categ name="compassion" isa="negative-emotion"/>
  <categ name="humility" isa="negative-emotion"/>
  <categ name="despair" isa="negative-emotion"/>
  <categ name="anxiety" isa="negative-emotion"/>
  <categ name="daze" isa="negative-emotion"/>

  <categ name="alarm" isa="negative-fear"/>
  <categ name="creeps" isa="negative-fear"/>
  <categ name="horror" isa="negative-fear"/>
  <categ name="hysteria" isa="negative-fear"/>
  <categ name="panic" isa="negative-fear"/>
  <categ name="scare" isa="negative-fear"/>
  <categ name="stage-fright" isa="negative-fear"/>
  <categ name="apprehension" isa="negative-fear"/>
  <categ name="timidity" isa="negative-fear"/>
  <categ name="fear-intimidation" isa="negative-fear"/>
  <categ name="negative-unconcern" isa="negative-fear"/>

  <categ name="trepidation" isa="apprehension"/>
  <categ name="foreboding" isa="apprehension"/>
  <categ name="negative-suspense" isa="apprehension"/>
  <categ name="chill" isa="apprehension"/>

  <categ name="shadow" isa="foreboding"/>
  <categ name="presage" isa="foreboding"/>

  <categ name="shyness" isa="timidity"/>
  <categ name="diffidence" isa="timidity"/>

  <categ name="hesitance" isa="diffidence"/>
  <categ name="unassertiveness" isa="diffidence"/>

  <categ name="heartlessness" isa="negative-unconcern"/>

  <categ name="cruelty" isa="heartlessness"/>

  <categ name="dolefulness" isa="sadness"/>
  <categ name="melancholy" isa="sadness"/>
  <categ name="misery" isa="sadness"/>
  <categ name="forlornness" isa="sadness"/>
  <categ name="weepiness" isa="sadness"/>
  <categ name="sorrow" isa="sadness"/>
  <categ name="cheerlessness" isa="sadness"/>
  <categ name="depression" isa="sadness"/>
  <categ name="downheartedness" isa="sadness"/>

  <categ name="gloom" isa="melancholy"/>
  <categ name="heavyheartedness" isa="melancholy"/>
  <categ name="world-weariness" isa="melancholy"/>

  <categ name="lost-sorrow" isa="sorrow"/>
  <categ name="regret-sorrow" isa="sorrow"/>

  <categ name="grief" isa="lost-sorrow"/>
  <categ name="mournfulness" isa="lost-sorrow"/>
  <categ name="self-pity" isa="lost-sorrow"/>

  <categ name="dolor" isa="grief"/>

  <categ name="woe" isa="mournfulness"/>
  <categ name="plaintiveness" isa="mournfulness"/>

  <categ name="attrition" isa="regret-sorrow"/>
  <categ name="compunction" isa="regret-sorrow"/>

  <categ name="guilt" isa="compunction"/>
  <categ name="repentance" isa="compunction"/>

  <categ name="joylessness" isa="cheerlessness"/>


  <categ name="demoralization" isa="depression"/>
  <categ name="helplessness" isa="depression"/>
  <categ name="despondency" isa="depression"/>
  <categ name="oppression" isa="depression"/>
  <categ name="dysphoria" isa="depression"/>

  <categ name="blue-devils" isa="despondency"/>

  <categ name="weight" isa="oppression"/>

  <categ name="anger" isa="general-dislike"/>
  <categ name="hate" isa="general-dislike"/>
  <categ name="dislike" isa="general-dislike"/>

  <categ name="fury" isa="anger"/>
  <categ name="infuriation" isa="anger"/>
  <categ name="umbrage" isa="anger"/>
  <categ name="indignation" isa="anger"/>
  <categ name="huffiness" isa="anger"/>
  <categ name="dander" isa="anger"/>
  <categ name="bad-temper" isa="anger"/>
  <categ name="annoyance" isa="anger"/>

  <categ name="wrath" isa="fury"/>
  <categ name="lividity" isa="fury"/>

  <categ name="dudgeon" isa="indignation"/>

  <categ name="irascibility" isa="bad-temper"/>
  <categ name="fit" isa="bad-temper"/>

  <categ name="pique" isa="annoyance"/>
  <categ name="frustration" isa="annoyance"/>
  <categ name="aggravation" isa="annoyance"/>
  <categ name="harassment" isa="annoyance"/>
  <categ name="displeasure" isa="annoyance"/>

  <categ name="abhorrence" isa="hate"/>
  <categ name="misanthropy" isa="hate"/>
  <categ name="misogamy" isa="hate"/>
  <categ name="misogyny" isa="hate"/>
  <categ name="misology" isa="hate"/>
  <categ name="misoneism" isa="hate"/>
  <categ name="misopedia" isa="hate"/>
  <categ name="murderousness" isa="hate"/>
  <categ name="despisal" isa="hate"/>
  <categ name="hostility" isa="hate"/>
  <categ name="malevolence" isa="hate"/>

  <categ name="misocainea" isa="misoneism"/>

  <categ name="animosity" isa="hostility"/>
  <categ name="class-feeling" isa="hostility"/>
  <categ name="antagonism" isa="hostility"/>
  <categ name="aggression" isa="hostility"/>
  <categ name="belligerence" isa="hostility"/>
  <categ name="resentment" isa="hostility"/>

  <categ name="warpath" isa="belligerence"/>

  <categ name="heartburning" isa="resentment"/>
  <categ name="sulkiness" isa="resentment"/>
  <categ name="grudge" isa="resentment"/>
  <categ name="envy" isa="resentment"/>

  <categ name="covetousness" isa="envy"/>
  <categ name="jealousy" isa="envy"/>

  <categ name="maleficence" isa="malevolence"/>
  <categ name="malice" isa="malevolence"/>
  <categ name="vindictiveness" isa="malevolence"/>

  <categ name="disinclination" isa="dislike"/>
  <categ name="unfriendliness" isa="dislike"/>
  <categ name="alienation" isa="dislike"/>
  <categ name="antipathy" isa="dislike"/>
  <categ name="disapproval" isa="dislike"/>
  <categ name="contempt" isa="dislike"/>
  <categ name="disgust" isa="dislike"/>

  <categ name="isolation" isa="alienation"/>

  <categ name="repugnance" isa="disgust"/>
  <categ name="nausea" isa="disgust"/>

  <categ name="conscience" isa="shame"/>
  <categ name="self-disgust" isa="shame"/>
  <categ name="embarrassment" isa="shame"/>

  <categ name="self-consciousness" isa="embarrassment"/>
  <categ name="shamefacedness" isa="embarrassment"/>
  <categ name="chagrin" isa="embarrassment"/>
  <categ name="confusion" isa="embarrassment"/>
  <categ name="abashment" isa="embarrassment"/>
  <categ name="discomfiture" isa="embarrassment"/>

  <categ name="commiseration" isa="compassion"/>
  <categ name="tenderness" isa="compassion"/>
  <categ name="mercifulness" isa="compassion"/>

  <categ name="forgiveness" isa="mercifulness"/>

  <categ name="self-depreciation" isa="humility"/>
  <categ name="meekness" isa="humility"/>

  <categ name="hopelessness" isa="despair"/>
  <categ name="resignation" isa="despair"/>
  <categ name="discouragement" isa="despair"/>
  <categ name="pessimism" isa="despair"/>

  <categ name="defeatism" isa="resignation"/>

  <categ name="despair-intimidation" isa="discouragement"/>

  <categ name="cynicism" isa="pessimism"/>

  <categ name="discomfiture" isa="anxiety"/>
  <categ name="negative-agitation" isa="anxiety"/>
  <categ name="distress" isa="anxiety"/>
  <categ name="negative-concern" isa="anxiety"/>
  <categ name="anxiousness" isa="anxiety"/>
  <categ name="insecurity" isa="anxiety"/>
  <categ name="edginess" isa="anxiety"/>
  <categ name="sinking" isa="anxiety"/>
  <categ name="scruple" isa="anxiety"/>
  <categ name="jitteriness" isa="anxiety"/>
  <categ name="angst" isa="anxiety"/>
  <categ name="anxiousness" isa="anxiety"/>
  <categ name="solicitude" isa="anxiety"/>

  <categ name="fidget" isa="negative-agitation"/>
  <categ name="stewing" isa="negative-agitation"/>
  <categ name="tumult" isa="negative-agitation"/>

  <categ name="impatience" isa="fidget"/>

  <categ name="apathy" isa="neutral-emotion"/>
  <categ name="neutral-unconcern" isa="neutral-emotion"/>

  <categ name="emotionlessness" isa="apathy"/>
  <categ name="neutral-languor" isa="apathy"/>

  <categ name="indifference" isa="neutral-unconcern"/>

  <categ name="distance" isa="indifference"/>
  <categ name="withdrawal" isa="indifference"/>

  <categ name="thing" isa="ambiguous-emotion"/>
  <categ name="gravity" isa="ambiguous-emotion"/>
  <categ name="surprise" isa="ambiguous-emotion"/>
  <categ name="ambiguous-agitation" isa="ambiguous-emotion"/>
  <categ name="ambiguous-fear" isa="ambiguous-emotion"/>
  <categ name="pensiveness" isa="ambiguous-emotion"/>
  <categ name="ambiguous-expectation" isa="ambiguous-emotion"/>

  <categ name="earnestness" isa="gravity"/>

  <categ name="astonishment" isa="surprise"/>

  <categ name="wonder" isa="astonishment"/>
  <categ name="surprise" isa="astonishment"/>
  <categ name="stupefaction" isa="astonishment"/>

  <categ name="awe" isa="wonder"/>

  <categ name="unrest" isa="ambiguous-agitation"/>
  <categ name="stir" isa="ambiguous-agitation"/>
  <categ name="tumult" isa="ambiguous-agitation"/>

  <categ name="electricity" isa="stir"/>
  <categ name="sensation" isa="stir"/>

  <categ name="reverence" isa="ambiguous-fear"/>

  <categ name="ambiguous-hope" isa="ambiguous-expectation"/>
  <categ name="fever" isa="ambiguous-expectation"/>

  <categ name="buck-fever" isa="fever"/>

</categ-list>

"""
    

    flag=True
    abc=""
    t=0
    isa=''
    val=''
    lastindex=0;
    increment=0
    emotion=[]
    file = etree.HTML(data)
    for a in s0:
        val=a
        isa=file.xpath("//categ-list/categ[@name=" + "'" + val + "'" + "]/@isa")
        isa="".join(isa)
        if isa=="positive-emotion" or isa=="ambiguous-emotion" or isa=="negative-emotion" or isa=="neutral-emotion":
            emotion.append(a)
            flag=False
            break
    abc=""    
    isa=''
    val=''
    for a in s0:
        val=a
#    print(val)
        while(t<15):
#        print(val)
            abc="".join(val)
            isa=file.xpath("//categ-list/categ[@name=" + "'" + abc + "'" + "]/@isa")
            isa="".join(isa)
            if isa:
#            isa="".join(isa)
                if isa!="positive-emotion" :
                    if isa!="ambiguous-emotion":
                        if isa!="negative-emotion" :
                            if isa!="neutral-emotion":
                                emotion.append(isa)
                                t+=1
                                val=isa
                                increment+=1
                            else:
                                break
                        else:
                            break
                    else:
                       break
                else:
#                    print("error")
                    break
            else:
#                t+=1
#                print("error")
                break
        lastindex=len(emotion)    
        if (lastindex>=1):    
            if("positive-emotion"==emotion[lastindex-1]):
                print("value of index=",emotion[lastindex-1])
                flag=False
                break
            if("ambiguous-emotion"==emotion[lastindex-1]):
                print("value of index=",emotion[lastindex-1])
                flag=False
                break
            if("negative-emotion"==emotion[lastindex-1]):
                print("value of index=",emotion[lastindex-1])
                flag=False
                break
            if("neutral-emotion"==emotion[lastindex-1]):
                print("value of index=",emotion[lastindex-1])
                flag=False
                break
            
        else:
             continue  
    if flag==True:
        for a in synsets_store:
            val=a
#    print(val)
            while(t<15):
#            print(val)
                abc="".join(val)
                isa=file.xpath("//categ-list/categ[@name=" + "'" + abc + "'" + "]/@isa")
                isa="".join(isa)
                if isa:
#                isa="".join(isa)
                    if isa!="positive-emotion" :
                        if isa!="ambiguous-emotion":
                            if isa!="negative-emotion" :
                                if isa!="neutral-emotion":
                                    emotion.append(isa)
                                    t+=1
                                    val=isa
                                    increment+=1
                                else:
                                    break
                            else:
                                break
                        else:
                            break
                    else:
#                    print("error")
                        break
                else:
#                t+=1
#                print("error")
                    break
            
            lastindex=len(emotion)    
            if (lastindex>=1):
                if("negative-fear"==emotion[lastindex-1] or "sadness"==emotion[lastindex-1] or "sad"==emotion[lastindex-1] or "general-dislike"==emotion[lastindex-1] or "ingratitude"==emotion[lastindex-1] or "shame"==emotion[lastindex-1] or "compassion"==emotion[lastindex-1] or "humility"==emotion[lastindex-1] or "despair"==emotion[lastindex-1] or "anxiety"==emotion[lastindex-1] or "daze"==emotion[lastindex-1]):
                    print("value of index=",emotion[lastindex-1])
#                    flag=False
                    break
                if("joy"==emotion[lastindex-1] or "happy"==emotion[lastindex-1] or "love"==emotion[lastindex-1] or "affection"==emotion[lastindex-1] or "liking"==emotion[lastindex-1]  or "enthusiasm"==emotion[lastindex-1] or "gratitude"==emotion[lastindex-1] or "self-pride"==emotion[lastindex-1] or "levity"==emotion[lastindex-1] or "calmness"==emotion[lastindex-1] or "fearlessness"==emotion[lastindex-1] or "positive-expectation"==emotion[lastindex-1] or "positive-fear"==emotion[lastindex-1] or "positive-hope"==emotion[lastindex-1]):
                    print("value of index=",emotion[lastindex-1])
#                flag=False
                    break
                if("thing"==emotion[lastindex-1] or "gravity"==emotion[lastindex-1] or "surprise"==emotion[lastindex-1] or "ambiguous-agitation"==emotion[lastindex-1] or "ambiguous-fear"==emotion[lastindex-1] or "pensiveness"==emotion[lastindex-1] or "ambiguous-expectation"==emotion[lastindex-1]):
                    print("value of index=",emotion[lastindex-1])
#                flag=False
                    break
                if("apathy"==emotion[lastindex-1] or "neutral-unconcern"==emotion[lastindex-1]):
                    print("value of index=",emotion[lastindex-1])
#                    flag=False
                    break
            else:
                continue
            
    final_emotion=""  
    verify=""          
    if (lastindex>=1):            
        final_emotion=emotion[lastindex-1]
        verify=emotion[lastindex-1]
        
    if (negation==True):
            if('positive-fear'==verify):
                final_emotion="negative-fear"
            if('negative-fear'==verify):
                final_emotion="positive-fear"    
            if('sad'==verify):
                final_emotion="happy"
            if('happy'==verify):
                final_emotion="sad"
            if('love'==verify):
                final_emotion="general-dislike"
            if('general-dislike'==verify):
                final_emotion="love"
            if('liking'==verify):
                final_emotion="general-dislike"
            if('general-dislike'==verify):
                final_emotion="liking"
            if('ingratitude'==verify):
                final_emotion="gratitude"
            if('joy'==verify):
                final_emotion="despair"
            if('joy'==verify):
                final_emotion="sadness"    
            if('despair'==verify):
                final_emotion="joy"
            if('affection'==verify):
                final_emotion="general-dislike"
            if('general-dislike'==verify):
                final_emotion="affection"
            if('general-dislike'==verify):
                final_emotion="love"    
            if('self-pride'==verify):
                final_emotion="humility"
            if('humility'==verify):
                final_emotion="self-pride"
            if('anxiety'==verify):
                final_emotion="calmness"
            if('calmness'==verify):
                final_emotion="anxiety"    
            if('levity'==verify):
                final_emotion="gravity"
            if('gravity'==verify):
                final_emotion="levity"
            if('enthusiasm'==verify):
                final_emotion="apathy"
            if('apathy'==verify):
                final_emotion="enthusiasm"
            if('pensiveness'==verify):
                final_emotion="neutral-unconcern" 
            if('neutral-unconcern'==verify):
                final_emotion="pensiveness"
            if('surprise'==verify):
                final_emotion="unsurprise"
            if('unsurprise'==verify):
                final_emotion="surprise"    
            if('ambiguous-agitation'==verify):
                final_emotion="calmness"    
            if('ambiguous-fear'==verify):
                final_emotion="calmness"
            if('fearlessness'==verify):
                final_emotion="fearfulness"
            if('shame'==verify):
                final_emotion="pride"
            if('self-pride'==verify):
                final_emotion="shame"
            if('daze'==verify):
                final_emotion="positive-hope"
            if('positive-hope'==verify):
                final_emotion="daze"
            if('positive-expectation'==verify):
                final_emotion="despair"
                
#    print(emotion)
    if(final_emotion):
        print("final emotion is ==>",final_emotion)
    else:
        print("Neutral sentence")
        final_emotion="Neutral sentence"
#    l4=tk.Label(root,text=final_emotion)
#    l4.grid(row=10,column=4)    
    txt.insert(0.0,final_emotion)
    



root=tk.Tk()
root.title("Emotion Prediction from Text through Sentiment Analysis")
root.geometry("500x250")
example_sent=tk.StringVar()
l1=tk.Label(root,text="Emotion Prediction from Text  ",bg="black",fg="white",font=("Helvetica", 17))
l2=tk.Label(root,text="Enter the Text")

ent=tk.Entry(root)


l1.grid(row=0,column=2,columnspan=2)
l2.grid(row=2,columnspan=2)
ent.grid(row=2,column=2)

bt=tk.Button(root,text="SUBMIT",bg="brown",fg="black" ,command=display)
bt.grid(row=3,column=1,columnspan=2)

txt=tk.Text(root,width="25", height="2", wrap="word")
txt.grid(row=4 ,columnspan=2, column=2,sticky='w')
root.mainloop()