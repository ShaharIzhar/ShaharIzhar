/*
    Created by: S.I
    Date Created: 05/08/19
    This sketch connects to wifi in order to control electronic devices using payloads from servers.
    in this case, controlling blinds in my room
*/

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#define UpPin 4
#define DownPin 5 
#ifndef STASSID
#define STASSID "User" //WiFi username
#define STAPSK  "pass" //Wifi Password
#endif

const char* ssid     = STASSID;
const char* password = STAPSK;
bool hasPeeked = false;

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

//Rolls blinds up
void BlindUp()
{
  pinMode(UpPin, OUTPUT);
              pinMode(DownPin, OUTPUT);
              digitalWrite(DownPin, LOW);
              digitalWrite(UpPin, HIGH);
}

//Rolls blinds down
void BlindDown()
{
 pinMode(UpPin, OUTPUT);
                pinMode(DownPin, OUTPUT);
                digitalWrite(UpPin, LOW);
                digitalWrite(DownPin, HIGH); 
}

//Stops blinds action - sets voltage to Low
void BlindStill()
{
  pinMode(UpPin, INPUT);
              pinMode(DownPin, INPUT);
              digitalWrite(UpPin, LOW);
              digitalWrite(DownPin, LOW);
}
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
      String payload = http.getString();   //Get the request response payload
      if(payload != "")
        {          
          if(checkIfPostOrGet(payload)) //checks if Post or Get
          { 
            String Body = bodyExtractor(payload);
            Serial.println(Body);
            if(Body.indexOf("up") != -1)
            {
              digitalWrite(LED_BUILTIN, LOW);
              hasPeeked=false;
              BlindUp();
            }
            else if(Body.indexOf("down") != -1)
            {
              digitalWrite(LED_BUILTIN, HIGH);
                hasPeeked=false;
                BlindDown();
            }
             else if(Body.indexOf("peek") != -1)
            {
              if(!hasPeeked){
                BlindUp();
                delay(3000);
                BlindStill();
                hasPeeked=true;
              }
            }
          }
          else
          {Serial.println("Meathod: GET");}
        }
    }
    http.end();   //Close connection
    delay(3500);    //Send a request every X seconds
  }
  
}

void loop() {
  webHooksListener();
}
