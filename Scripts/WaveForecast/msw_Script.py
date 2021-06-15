#Written and created by: S.I
#Date created: 14/02/2019

# Automation to me accessing MSW forecast app everyday to check for waves.
# Uses Webscraping to access wave and sea data, 
# checks 2-days in for waves - if condition is true, sends message using Pushbullet service to contacts.

import requests
import smtplib
from pushbullet import Pushbullet

accessToken='o.xH38oX3Tdj3f9Db4i6pbRyKUOhX4CCOV'
pb= Pushbullet(accessToken) #Pushbullet Service
url = "https://magicseaweed.com/Marina-Herzelia-Surf-Report/3979/" #forecast website URL
minHight = 0.5 #minimal height of waves for text send
sendalert = False

#Retrieves wave heights
def getwaveheight(url):
    r = requests.get(url)
    data = r.text
    waveheights=list()

    while(data.find("maxBreakingHeight")>0):
        flag = False
        index = data.find("maxBreakingHeight")
        beg=index
        newdata=data[beg+40:beg+60]
        if(newdata.find("0.")==-1):
            height=newdata.find("1.")
        else:
            height=newdata.find("0.")

        waveheight=newdata[height:height+3] 
        
        for x in waveheights:
            if(waveheight == x):
                flag = True
                break
            else:
                flag = False
        if(flag==False):
            waveheights.append(float(waveheight))
        temp = data
        data=temp[beg+50:]
    
    return waveheights

#Checks weather an notification is needed
def alertneeded(waveheights):
    for x in waveheights:
        if(x>minHight):
            break
        break
    sendnotification()
    
#Sends Notification to contacts
def sendnotification(): 
    msg = "Surf Time!"
    pb.push_note("SurfTime", msg)

#Main
alertneeded(getwaveheight(url))