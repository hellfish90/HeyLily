#if defined(ARDUINO) && ARDUINO >= 100

  #include "Arduino.h"

  #include "Platform.h"

  #include "SoftwareSerial.h"

#ifndef CDC_ENABLED

  // Shield Jumper on SW

  SoftwareSerial port(12,13);

#else

  // Shield Jumper on HW (for Leonardo)

  #define port Serial1

#endif

#else // Arduino 0022 - use modified NewSoftSerial

  #include "WProgram.h"

  #include "NewSoftSerial.h"

  NewSoftSerial port(12,13);

#endif



#include "EasyVR.h"



EasyVR easyvr(port);


#define SND_dontunderstand       1
#define SND_tellme               2
#define SND_what                 3
#define SND_youneedsomething     4
#define SND_done                 5
#define SND_yes                  6
#define SND_where                7
#define SND_ithasnotbeenpossible 8
#define SND_channel              9


//Groups and Commands

enum Groups

{
  GROUP_0  = 0,
  GROUP_1  = 1,
  GROUP_2  = 2,
  GROUP_3  = 3,
  GROUP_4  = 4,
};


enum Group0 
{
  G0_HEYLILY = 0,
};

enum Group1 
{
  G1_NEWS = 0,
  G1_TELEVISION = 1,
  G1_RADIO = 2,
  G1_LIGHT = 3,
  G1_COFFEE = 4,
  G1_SILENCE = 5,
  G1_STOP = 6,
  G1_NOTHING = 7,
};

enum Group2 
{
  G2_1 = 0,
  G2_2 = 1,
  G2_3 = 2,
  G2_4 = 3,
  G2_5 = 4,
  G2_6 = 5,
  G2_7 = 6,
  G2_8 = 7,
  G2_9 = 8,
  G2_10 = 9,
  G2_SILENCE = 10,
  G2_NOTHING = 11,
};

enum Group3 
{
  G3_SHORT = 0,
  G3_LONG = 1,
  G3_NOTHING = 2,
};

enum Group4 
{
  G4_TELEVISION = 0,
  G4_RADIO = 1,
  G4_NEWS = 2,
  G4_LIGHT = 3,
  G4_NOTHING = 4,
  G4_SILENCE = 5,
};



EasyVRBridge bridge;



int8_t group, idx;

//////////////////////////////
//  NEW Plugins              ///
/////////////////////////////

bool television=false; 
bool radio=false;
bool news=false;
bool light = false;
bool stop_p = false; 
bool coffee = false;

const String TELEVISION = "TELEVISION";
const String NEWS = "NEWS";
const String RADIO = "RADIO";
const String LIGHT = "LIGHT";
const String STOP = "STOP";
const String COFFEE = "COFFEE";

//////Finish plugins vars//////


/// Other vars ///

bool Lily = false;
int timeOut = 0;
int error = 0;
const int MAXTIMEOUT = 2;
const int MAXERRORS = 6;




void setup()

{

#ifndef CDC_ENABLED

  // bridge mode?

  if (bridge.check())

  {

    cli();

    bridge.loop(0, 1, 12, 13);

  }

  // run normally

  Serial.begin(9600);

  Serial.println("Bridge not started!");

#else

  // bridge mode?

  if (bridge.check())

  {

    port.begin(9600);

    bridge.loop(port);

  }

  Serial.println("Bridge connection aborted!");

#endif

  port.begin(9600);



  while (!easyvr.detect())

  {

    Serial.println("EasyVR not detected!");

    delay(1000);

  }



  easyvr.setPinOutput(EasyVR::IO1, LOW);

  Serial.println("EasyVR detected!");

  easyvr.setTimeout(5);

  easyvr.setLanguage(4);


  group = EasyVR::TRIGGER; //<-- start group (customize)

}



void action();



void loop()

{

  easyvr.setPinOutput(EasyVR::IO1, HIGH); // LED on (listening)



  Serial.print("Say a command in Group ");

  Serial.println(group);

  easyvr.recognizeCommand(group);



  do

  {

    // can do some processing while waiting for a spoken command

  }

  while (!easyvr.hasFinished());

  

  easyvr.setPinOutput(EasyVR::IO1, LOW); // LED off



  idx = easyvr.getWord();

  if (idx >= 0)

  {

    // built-in trigger (ROBOT)

    // group = GROUP_X; <-- jump to another group X

    return;

  }

  idx = easyvr.getCommand();

  if (idx >= 0)

  {

    // print debug message

    uint8_t train = 0;

    char name[32];

    Serial.print("CommandDetected: ");

    Serial.print(idx);

    if (easyvr.dumpCommand(group, idx, name, train))

    {

      Serial.print(" = ");

      Serial.println(name);

    }

    else

      Serial.println();

    //easyvr.playSound(0, EasyVR::VOL_FULL);

    // perform some action

    action();

  }

  else // errors or timeout

  {

    if (easyvr.isTimeout()){
      
      Serial.println("Timed out, try again...");
      
      if (Lily){
        playsound(SND_youneedsomething);
        timeOut++;
      }
     }

      

    int16_t err = easyvr.getError();

    if (err >= 0)

    {
      
      if(error>3){
      
        playsound(SND_dontunderstand);
        
      }

      Serial.print("Error ");

      Serial.println(err, HEX);
      
      if (Lily){
        error++;
      }
     }
     checkTimeOutAndError();

    }

  

}



void action()

{

    switch (group)

    {

    case GROUP_0:
      switch (idx)
      {
      case G0_HEYLILY:
         group = GROUP_1; //<-- or jump to another group X for composite commands
         playsound(SND_tellme);
         Lily = true;
        break;
      }
      break;
    case GROUP_1:
      switch (idx)
      {
      case G1_NEWS:
        news = true;
        group = GROUP_2;// <-- or jump to another group X for composite commands
        playsound(SND_tellme);
        break;
      case G1_TELEVISION:
        television = true;
        group = GROUP_2;// <-- or jump to another group X for composite commands
        playsound(SND_channel);
        break;
      case G1_RADIO:
        radio = true;
        group = GROUP_2;// <-- or jump to another group X for composite commands
        playsound(SND_channel);
        break;
      case G1_LIGHT:
        light = true;
        restartCommands();
        break;
      case G1_COFFEE:
        coffee = true;
        group = GROUP_3;// <-- or jump to another group X for composite commands
        playsound(SND_yes);
        break;
      case G1_SILENCE:
        silenceAction();
        break;
      case G1_STOP:
        stop_p = true;
        group = GROUP_4;// <-- or jump to another group X for composite commands
        playsound(SND_what);
        break;
      case G1_NOTHING:
        nothingAction();
        break;
      }
      break;
    case GROUP_2:
      switch (idx)
      {
      case G2_1:
        sendCommandByChanel("1");
        break;
      case G2_2:
        sendCommandByChanel("2");
        break;
      case G2_3:
        sendCommandByChanel("3");
        break;
      case G2_4:
        sendCommandByChanel("4");
        break;
      case G2_5:
        sendCommandByChanel("5");
        break;
      case G2_6:
        sendCommandByChanel("6");
        break;
      case G2_7:
        sendCommandByChanel("7");
        break;
      case G2_8:
        sendCommandByChanel("8");
        break;
      case G2_9:
        sendCommandByChanel("9");
        break;
      case G2_10:
        sendCommandByChanel("10");
        break;
      case G2_SILENCE:
        silenceAction();
        break;
      case G2_NOTHING:
        nothingAction();
        break;
      }
      break;
    case GROUP_3:
      switch (idx)
      {
      case G3_SHORT:
        sendCommandToServer(COFFEE, COFFEE, "LONG", "SELF");
        break;
      case G3_LONG:
        sendCommandToServer(COFFEE, COFFEE, "LONG", "SELF");
        break;
      case G3_NOTHING:
        nothingAction();
        break;
      }
      break;
    case GROUP_4:
      switch (idx)
      {
      case G4_TELEVISION:
        stopPlugin(TELEVISION, "SELF");
        break;
      case G4_RADIO:
        stopPlugin(RADIO, "SELF");
        break;
      case G4_NEWS:
        stopPlugin(NEWS, "SELF");
        break;
      case G4_LIGHT:
        stopPlugin(LIGHT, "SELF");
        break;
      case G4_NOTHING:
        nothingAction();
        break;
      case G4_SILENCE:
        silenceAction();
        break;
      }
      break;
    }
}

  void playsound(int num){
 
      easyvr.playSound(num, EasyVR::VOL_FULL);
  }
  
  void stopPlugin(String plugin, String module){
    
     sendCommandToServer(plugin, STOP + "_" + plugin, "0" ,module);
  
  }
    
  void sendCommandToServer(String plugin, String instruction, String parameter, String module ){
    Serial.print("COMMAND;");
    Serial.print(plugin);
    Serial.print(";");
    Serial.print(module);
    Serial.print(";");
    Serial.print(instruction);
    Serial.print(";");
    Serial.print(parameter);
    Serial.println("");
    
    restartCommands();
    playsound(SND_done);
  }  
  
  void sendCommandByChanel(String chanel){
  
    String plugin;
  
      if(news){
       sendCommandToServer(NEWS,"CHANEL_NEWS",chanel,"SELF"); 
      }else if(radio){
        sendCommandToServer(RADIO,"CHANEL_RADIO",chanel,"SELF");
      }else if(television){
        sendCommandToServer(TELEVISION,"CHANEL_TELEVISION",chanel,"SELF");  
      }
       
  }
  
  void nothingAction(){
  
     restartCommands();
     playsound(SND_done);
    
  }
  
  void silenceAction(){

     sendCommandToServer("SILENCE", "SILENCE", "SILENCE", "SELF" );
     restartCommands();
     
  }
  
  void restartCommands(){  
    resetPlugins();
    group = GROUP_0; 
    Serial.println("RESTART");
  }
  
  void resetPlugins(){
    news = false;
    radio = false;
    television = false;
    coffee = false;
    stop_p = false;
    Lily = false;
  }
  
  void checkTimeOutAndError(){
  
    if(timeOut > MAXTIMEOUT ){
        
        timeOut = 0;
        
        restartCommands();
    }
    
    if(error > MAXERRORS ){
  
        error = 0;
        
        restartCommands();
    }
  
    
  }




