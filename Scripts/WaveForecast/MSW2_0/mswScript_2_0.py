#Written and created by: S.I
#Date created: 12/05/2019

# An update to mswScript.py - Using API, Automation to me accessing MSW forecast app everyday to check for waves.
# Uses Api from https://www.msw.com to access wave and sea data, 
# checks 2-days in for waves - if condition is true, meaning there are waves, sends message using SMS to contacts.

import requests
import random
import datetime
import WeatherToConditionsConverter #A library i wrote to convert weather conditions from number icon to words
from pushbullet import PushBullet


#Consts
PbAccessToken='o.EhOTbRvCUkMhzSQySUkej7NDMdz5GNtC'
MSW_API = "c345356797c450980f654a476dcf81de"
pb = PushBullet(PbAccessToken)
sender = pb.get_device('Samsung SM-G950F')
MarinaHertzeliaSpotNumber = 3979
URL = r'http://magicseaweed.com/api/'+MSW_API+r'/forecast/?spot_id='+str(MarinaHertzeliaSpotNumber)+r'&fields=swell.minBreakingHeight,swell.maxBreakingHeight,wind.speed,wind.compassDirection,condition.temperature,condition.weather&units=eu'

blessings = [
    "Have a great day!",
    "Go Shred!",
    "Shred it!",
    "Rock it!",
    "Just do it!",
    "Ride on!",
    "No regrets!",
    "Live. Love. Surf.",
    "If in doubt, paddle out!",
    "Home is where the waves are",
    "You can't stop the waves, but you can surf them",
    "Catch a wave, then we'll talk",
    "May the waves rise to meet you",
    "When life gives you lemons, go surf!",
    "The only good suit is a SurfSuit",
    "The best wave of your life is still out there",
    "Dream it. Believe it. Achieve it.",
    "Get some wax, quick!"
]

adressBookDict = {
      "+972547726838" : "Shahar",
    "+972544888285" : "Yoav", 
    "+972528225533": "Nadav", 
    "+972526532900": "Asaf",
    "+972544455758": "Eylon",
    "+972528667009": "Guy",
    "+972547832810": "Guy"
}
minHight = 0.4 #minimal height of waves for text send

#Removes unwanted info and converts list to data 2 days from now
def analyzeList(DataList):
    del DataList[0]
    del DataList[24:]
    del DataList[0:15]
    return DataList

#Gets the day name two days from now
def getTwoDaysFromToday():
    today = datetime.datetime.today()
    afterTwoDays = today + datetime.timedelta(days=2)
    return afterTwoDays.strftime("%A")

#Gets dataList, returns list of heights - True = Max, False = Min
def getBreakingHeights(DataList, MaxorMin):
    waveheights=list()
    if(MaxorMin):
        keyword = "maxBreakingHeight"
    else:
        keyword ="minBreakingHeight"
        
    for details in DataList:
        waveHeight = details['swell'][str(keyword)]
        waveheights.append(float(waveHeight))
    return waveheights

#Gets dataList, returns wind details
def getWindDetails(DataList): 
    windSpeed = DataList[2]['wind']['speed']
    windDir = DataList[2]['wind']['compassDirection']
    msg = str(windDir)+', '+str(windSpeed)+' KPH'
    return msg

#Gets dataList, returns weather condition
def getConditionDetails(DataList):
    weatherCondition = DataList[2]['condition']['weather']
    return weatherCondition

#Gets dataList, returns temperature
def getTemperature(DataList):
    Temperature = DataList[2]['condition']['temperature']
    msg = str(Temperature)+'C'
    return msg

#Checks weather an alert should be sent or not, returns a message string
def minMaxData(afterTwoDays, maxWaveList, minWaveList, windDetailsStr, temperatureStr, conditions, spotName):
    minListMin = min(minWaveList)
    maxListMin = min(maxWaveList)
    maxListMax = max(maxWaveList)
    minListMax = max(minWaveList)
    
    if(minListMax>minHight):
        return msgNotification(afterTwoDays, maxListMin, maxListMax, minListMin, minListMax, windDetailsStr, temperatureStr, conditions, spotName)
    else:
        msg = 'No Surfing Waves For: ' +str(spotName)+'\n\n'
        return msg

#Builds message content, return message string
def msgNotification(afterTwoDays, maxListMin, maxListMax, minListMin, minListMax, windDetailsStr, temperatureStr, conditions, spotName): 
    # msg = str(spotName)
    msg = ' Waves on '+str(afterTwoDays)+'!\n High: '
    msg+= str(minListMax) +' - ' +str(maxListMax)
    msg+= " M\n Low: " 
    msg+= str(minListMin) +' - ' + str(maxListMin)
    msg+= ' M\n Temperature: ' + str(temperatureStr) + ', '+conditions
    msg+= "\n Wind: "
    msg+= str(windDetailsStr)
    msg += "\n\n"
    msg += ' ' + str(random.choice(blessings))
    return msg

#Sends message to all contacts using Push-Bullet server
def sendMessageToContacts(msgContent):
    if(msgContent.find("High")>0):
        for key ,value in adressBookDict.items():
            msg='Good morning '+value+'!\n' + msgContent
            # pb.push_sms(sender, key, msg)
            print(msg)

#Handles all data to be sent
def getAllData(DataList):
    MswDataList = analyzeList(DataList) #Analyzes List
    weatherConditionNum = getConditionDetails(MswDataList)
    conditions = WeatherToConditionsConverter.convertWeather(weatherConditionNum)
    windDetails = getWindDetails(MswDataList) #Gets Wind Details
    temperatureDetails = getTemperature(MswDataList) #Gets Temperature Details
    maxWaveHeightsList = getBreakingHeights(MswDataList, True) #Gets Maximum WaveHeights List
    minWaveHeightsList = getBreakingHeights(MswDataList, False) #Gets Minimum WaveHeights List
    afterTwoDays = getTwoDaysFromToday()
    msg = minMaxData(afterTwoDays, maxWaveHeightsList, minWaveHeightsList, windDetails, temperatureDetails, conditions, "Marina Hertzelia")
    return msg

#Main
mswData = requests.get(URL)
mswDataList = mswData.json()
sendMessageToContacts(getAllData(mswDataList))