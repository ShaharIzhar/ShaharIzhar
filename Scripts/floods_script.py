#Written and created by: S.I
#Date created: 03/01/20

# While doing the INT(Israel National Trail) in the winter I was faced with a mobile service problem that couldn't allow me to check for floods
# Rented a satelite phone that only recieves SMS and Wrote the following script:

# Uses Webscraping to access temprature and floods data from https://ims.gov.il/, 
# checks 2-days in for floods - if condition is true, sends message to satelite phone that I am carrying in the field.

import requests
from pushbullet import PushBullet
import datetime


#Consts
accessToken='o.EhOTbRvCUkMhzSQySUkej7NDMdz5GNtC'
pb= PushBullet(accessToken)
oldName = "Samsung SM-G950F"
newName = "Galaxy S8"
Asaf = 'LGE LG-H870'
sender = pb.get_device(Asaf)
ForecastWebSiteURL = "http://www.ims.gov.il/IMSENG/All_Tahazit/homepage.htm"

#Contacts
addressBook = [
    "+972547726838"
    ,"+972544878843" 
    ,"+972526284139"
    ]

#Gets the date two days from today
def getTwoDaysFromToday():
    today = datetime.datetime.today()
    afterTwoDays = today + datetime.timedelta(days=2)
    Day = afterTwoDays.day
    Month = afterTwoDays.month
    if(len(str(Day))==1):
        Day = str(Day).zfill(2)
    if(len(str(Month))==1):
        Month = str(Month).zfill(2)
    return (str(Day) +'/' + str(Month))

#Checks if there are any warnings for the requested date
def checkForWarnings(data):
    keyword = getTwoDaysFromToday()
    if(data.find(keyword)>=0):
        return True
    return False

#Gets unbuffered data, returns buffered string of warnings
def getTempWarnings(data):
	keyword = getTwoDaysFromToday()
	newdata = ''
	if(data.find(keyword)>=0):
		index = data.find(keyword)
		beg=index
		newdata=data[beg:beg+1500] #substring
	return analyzeString(newdata)

#analyzes string to buffered warnings
def analyzeString(SubstringData):
    floodsKeyword = 'flood' 
    if(SubstringData.find(floodsKeyword)>=0):
        beg = SubstringData.find(floodsKeyword)
        newdata = SubstringData[beg:beg+1000]
        if(newdata.find('.')>=0):
            end = newdata.find('.')
            finalData = newdata[0:end]
    else:
        finalData='NF'
    return finalData

#gets all unbuffered data from server
def getWarnings(url):
    webString = requests.get(url) #Find a way to collect more chars to data
    data = webString.text
    if (checkForWarnings(data)):
        return getTempWarnings(data) #find how warnings are edited in url
    return "No News"

#Main
MsgContent  = getWarnings(ForecastWebSiteURL)
for number in addressBook:
    pb.push_sms(sender, number, MsgContent)
