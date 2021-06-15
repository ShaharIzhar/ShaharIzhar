/*
    Created by: S.I
    Date Created: 07/09/19
    This sketch connects to wifi in order to control electronic devices using payloads from servers.
    in this case, controlling lights and fan in my room
*/
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#define LightPin 16 //Default 0
#define FanPin 5 //Default 1
#ifndef STASSID
#define STASSID "User" //WiFi username
#define STAPSK  "Pass"//Wifi Password
#endif

const char* ssid     = STASSID;
const char* password = STAPSK;
String payload;
String lastCommand = "";

void setup () {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println(".");
  }
  
    Serial.println("");
    Serial.println("Connected!");
}

//returns true if server current meathod is post
bool checkIfPostOrGet(String Payload){
  String keyWord = "POST";
  if(Payload.indexOf(keyWord)!=-1)
    return true;
  else
    return false;
}

//Toggles light
void LightToggle()
{
  pinMode(LightPin, OUTPUT);
              digitalWrite(LightPin, !digitalRead(LightPin));
}

//Toggles Fan
void FanToggle()
{
  FanToggle != FanToggle;
  pinMode(FanPin, OUTPUT);
              digitalWrite(FanPin, !digitalRead(FanPin));
}

//Parses payload from server
String bodyExtractor(String payload)
{
  int codeBeginIndex =0;
  String codeBeginKeyword = "#B#";
  
  int codeEndIndex =0;
  String codeEndKeyword = "#E#";
  
  codeBeginIndex = payload.indexOf(codeBeginKeyword);
  codeEndIndex = payload.indexOf(codeEndKeyword);
  String Body ="";
  Body = payload.substring(codeBeginIndex+3, codeEndIndex);
  return Body;
}

//Retrieves payload from server 
void webHooksListener(){
  while (WiFi.status() == WL_CONNECTED) { 
    Serial.print("*");
    //Check WiFi connection status
    HTTPClient http;  //Declare an object of class HTTPClient
    http.begin("http://ptsv2.com/t/8eexx-1549996746/d/latest");  //Specify request destination
    int httpCode = http.GET();
    if (httpCode > 0) { //Check the returning code   
      
      String oldPayLoad = payload;
      payload = http.getString();   //Get the request response payload
      if(payload != "" && payload != oldPayLoad && payload != lastCommand)
        {          
          if(checkIfPostOrGet(payload)) //checks if Post or Get
          { 
            String Body = bodyExtractor(payload);
            Serial.println(Body);
            if(Body.indexOf("light") != -1)
            {
              LightToggle();
              lastCommand = payload;
            }
            if(Body.indexOf("fan") != -1)
            {
                FanToggle();
                lastCommand = payload;
            }
          }
          else
          {Serial.println("Meathod: GET");}
        }
    }
    http.end();   //Close connection
    delay(2500);    //Send a request every X seconds
  }
  
}

void loop() {
  webHooksListener();
}
