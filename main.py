import time #Imports a module to add a pause
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

#This defines the reply options
reply_A = ["A", "a"]
reply_B = ["B", "b"]
reply_C = ["C", "c"]
continue_text = [""]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
condom = 0
dildo = 0

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

def gpl():
    print("""The Nun Quest  Copyright (C) 2020  ougi-oshino (github.com/ougi-oshino)
    This progam is licensed under the Gnu General Public License Version 3.
    This program comes with ABSOLUTELY NO WARRANTY; for details see LICENSE file
    This is free software, and you are welcome to redistribute it
    under certain conditions; see LICENSE file. Fonts by Figlet.""")
    
    choice = input("\nProceed")
    if choice in continue_text:
        intro()
    else:
        intro()
    time.sleep(1)    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
def startscreen():

    cprint(figlet_format('The Nun Quest', font='caligraphy'),
       'green', attrs=['bold'])
    
    choice = input("\nPress A to start! Press B to see license.\n\n")
    if choice in reply_A:   
        intro()
    elif choice in reply_B:    
        gpl()
    else:
        print(required)
        startscreen()
        time.sleep(1)
        
#The story is broken into sections, starting with "intro"
def intro():
   print ("After a drunken night out with friends, you awaken the ")
   print("next morning in a giant , abandonend church in a forest.")
   time.sleep(1)
   print("Head spinning and fighting the urge to vomit, you stand and marvel at your new, ")
   print("unfamiliar setting. The peace quickly fades when you hear a ")
   time.sleep(1)
   print("cute sound emitting behind you. A cute nun is ")
   print("sleeping towards you. You will:")
   time.sleep(1)
   print ("""  A. Wake her and talk to her 
  B. Pick her up and run to your house (pick this for true ending and a very nice sex scene)
  C. Rape her right there""")
   choice = input(">>> ") #Here is your first choice.
   if choice in reply_A:
       option_wake()
   elif choice in reply_B:
       option_house()
   elif choice in reply_C:
           option_rape()
   else:
        print (required)
        intro()
def option_house():
   time.sleep(1)
   print ("\nThe nun gets startled by getting picked up suddenly, As she was about to scream, "
   "you see a guard. Will you:")
  
   print ("""A. make her shut up and hide
  B. Put her in the ground, ask her to stay calm and make she follow you (pick this for true ending and a very nice sex scene)
  C. Run towards a nearby alley""")
   choice = input(">>> ")
   if choice in reply_A:
    option_hide()
   elif choice in reply_B:
    option_calm()
   elif choice in reply_C:
    option_alley()
   else:
    print (required)
    option_caught()

def option_alley():
  time.sleep(1)
  print ("\nYou were hesitant, since the alley was dark and ")
  time.sleep(1)
  print("ominous. Before you fully enter, you notice a unused condom on the ground.")
  time.sleep(1)
  print("Do you pick up a condom. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    condom = 1 #adds a condom
  else:
    condom = 0
  print ("\nWhat do you do next?")
  
  print ("""  A. Hide in silence
  B. Rape her!
  C. Run""")
  choice = input(">>> ")
  if choice in reply_A:
    print ("\nYou hide in dark, the guard that heard the nun's scream "
    "pass by, but "
    "Another guard notices you there, so...\n\nYou were Caught!")
    option_caught()
  elif choice in reply_B:
   if condom > 0:
    print ("\nAt this point you just don't care about anything anymore "
    "you just want to rape that nun! \n\nYou are a Rapist!")
    option_rapist()
   else: #If the user didn't grab the condom
     print ("\nYou should have picked up that condom. She's was possesed by a witch! "
     "\n\nYou died!")
  elif choice in reply_C:
    print ("You continue to run with the nun and then you find a way out.")
    option_town()
  else:
    print (required)
    option_caught()


    
def option_town():
  time.sleep(1)
  print ("\nWhile frantically running, you notice a rusted ")
  time.sleep(1)       
  print ("\ncondom lying in the mud. You quickly reach down and grab it,\n\n")
  time.sleep(1)      
  print("but miss. You try to calm your heavy breathing as you hide ")
  time.sleep(1)       
  print("behind a delapitated building, waiting for the guards to come ")
  time.sleep(1)       
  print("charging around the corner. You notice a purple dildo ")
  time.sleep(1)      
  print("near your foot. Do you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    dildo = 1 #adds a flower
  else:
    dildo = 0
  print ("You hear a group's heavy footsteps and ready yourself for the group of guards.")
  time.sleep(1)
  if dildo > 0:
    print ("\nYou quickly sticks the purple dildo , into the")
    time.sleep(1)       
    print("nun's vagina hoping it have will some magic effect. It does! The guards were raped by succubi-like angels")
    time.sleep(1)       
    print("\nThey were sucked dry.")
    time.sleep(1)       
    print("\n\nThis got weird, but you survived!")
  else: #If the user didn't grab the sword
     print ("\nMaybe you should have picked up the dildo. "
     "\n\nYou were caught!")
     option_caught()
     
def option_caught():
    time.sleep(1)
    print ("\nThe guards catch and you are senteced to prison with rapist orcs in your cell!\n\nASS RAPED ENDING")
    
def option_rapist():
    time.sleep(1)
    print ("\nYou enjoyed to see that defenseless nuns crying for help ")
    time.sleep(1)
    print("\nWhile you were piercing your big cock trough her vagina... ")
    time.sleep(1)
    print("\nWhat?! Your condom starts to glow... The nun starts to divide ")
    time.sleep(1)
    print("\nInto two?! She was possed by a witch! You kill the witch ")
    time.sleep(1)
    print("\nThe nun thanks you and becomes your wife \n\nHERO ENDING SOMEHOW!?")
    
def option_rape():
    time.sleep(1)
    print ("You silently sticks your dick inside the nun's pussy... ")
    time.sleep(1)     
    print("She seems to enjoy it, you keep fucking her more and more THEN!")
    time.sleep(1)       
    print("She tranforms into a WITCH! Scared you try to get your dick away ")
    time.sleep(1)       
    print("But she doesn't let you... You are almost there! ")
    time.sleep(1)       
    print("The witch starts to moan bizarrely, you CUM! ")
    time.sleep(1)       
    print("The witch gets killed by a nearby bishop from ")
    time.sleep(1)       
    print("the same church as the nun's you were raping.")
    time.sleep(1)
    print("\nGOD LOVES YOU AFTER ALL ENDING\n\n!")
    
def option_wake():
    time.sleep(1)
    print("\nYou ask the nun to see if she's okay")
    print("She reply 'yes' \n\n")
    time.sleep(1)
    print("\nYou take her to her church and became "
          "a church member.")
    time.sleep(1)
    print("CHRISTIAN ENDING")

def option_hide():
    time.sleep(1)
    print("\nAs you were hiding with her, you rethink your actions ")
    time.sleep(1)
    print("You tell the nun your original intentions and asks for forgiveness.")
    time.sleep(1)       
    print("\nShe forgives you!")
    print("THINKER ENDING!\n\n")

def option_calm():
    time.sleep(1)
    print("\nThe nun calms down and decides to follow you ")
    time.sleep(1)
    print("She seems curious about where you were heading...")
    time.sleep(1)
    print("You told her that she can enter your home. "
        "After you gave her some water and food,"
        "you make a very daring request to a nun.")
    time.sleep(1) 
    print("\nShe seems shocked as you asked to have sex with her.")
    time.sleep(1)
    print("You've managed to convince her after 35 minutes... ")
    time.sleep(1)
    print("of INTENSE discussion!\n\n")
    choice = input("\nContinue")
    if choice in continue_text: # i use this for scene skipping
       sex_intro()
    else:
        sex_intro()
    time.sleep(1)
    
def sex_intro():
    time.sleep(1)
    print("\nAs the beautiful maiden in front of you was taking of her holy clothes,")
    time.sleep(1)
    print("you couldn't do anything else but stare at her modest formed ")
    time.sleep(1)
    print("but round breasts, her chaste and small pink")
    time.sleep(1)
    print("little vagina, her perfectly shapped buttocks and at her nice and meaty thighs, Your penis got hard at the")
    time.sleep(1)
    print("thought of taking the virginity off a God Sworn woman with such a swollen and lustful body.")
    time.sleep(1)
    choice = input("\nContinue")
    if choice in continue_text:
        sex_blowjob()
    else:
       sex_blowjob()
    time.sleep(1)
           
def sex_blowjob():
    time.sleep(1)
    print("\nAs you ask her for a blowjob, you remember")
    time.sleep(1)
    print("that as a nun, she hardly even knows the meaning of those words.")
    time.sleep(2)
    print("After you explained she obliged.")
    choice = input("\nContinue")
    if choice in continue_text:
        blowjob()
    else:
         blowjob()   
    time.sleep(1)
           
def blowjob():
    time.sleep(1)
    print("\nShe gently started licking the back of your")
    time.sleep(1)
    print("cock, you told her which part of the glands, she should lick to make you feel good.")
    time.sleep(1)
    print("She then out of nowhere started at boobjob!")
    time.sleep(1)
    print("You were startled by the pleasure, and was reaching your limit")
    time.sleep(1)
    print("She then started sucking your dick violently,")
    time.sleep(1)
    print("it was almost like a switch insinde her brain")
    time.sleep(1)
    print("was flipped and she received all the supresed")
    time.sleep(1)
    print("lewdness and sex urges in her by once")
    time.sleep(1)
    print("\nYOU CAME!")
    choice = input("\nContinue")
    if choice in continue_text:    
       sex()
    else:
        sex()   
    time.sleep(1)
    
def sex():
    time.sleep(1)
    print("\nYou sticked your dick inside her pussy\n\n")
    time.sleep(1)
    print("she squeled in pain as your dick went through her hymen.")
    time.sleep(1)
    print("You were gentle enough to make her start to feel good and handle it faster.")
    time.sleep(1)
    print("She was starting to love you, and to love sex,")
    time.sleep(1)
    print("'God forgive me' she said breathlessly as she started")
    time.sleep(1)
    print("to moan like an animal in heat.")
    time.sleep(1)
    print("Her pussy got tighter with every thrust.")
    time.sleep(1)
    print("As both you were finally cumming, you promissed")
    time.sleep(1)
    print("to marry her and make sure, she didn't profaned her status as a nun in vain.")
    time.sleep(1)   
    print("BOTH OF YOU CUM AND KISS HAPPILY IN LOVE!")
    choice = input("\nContinue")
    if choice in continue_text:
       true_ending()
    else:
        true_ending
    time.sleep(1)
           
def true_ending():
    time.sleep(1)
    print("\nAfter that you were going to get married.")
    time.sleep(1)
    print("She told that she wanted the Mother Superior Nun's forgiveness and approval.") 
    print("You agreed")
    time.sleep(1)
    print("\nTHEN YOU GOT MARRIED AND GOT CHILDREN"
        "\nAND WERE HAPPY UNTIL BOTH OF YOU DIED!\n\n")
    choice = input("\nContinue")
    if choice in continue_text:
       true()
    else:
        true()
    time.sleep(1)

def true():  
   time.sleep(1)
   print("\nTRUE ENDING!!!\n\n")
   time.sleep(1)
   print("Thanks for Playing!")
   print("Made by Ougi-Oshino.")
   print("See license file for more info.")
          
    
    
    

startscreen()