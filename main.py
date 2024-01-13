import time #Imports a module to add a pause
import sys

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
finger = 0
mouth = 0

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

print('Welcome to Slutty Quest!')  # remeber to add stylish font
print('What is the size of your peepee?') # ask for their deek/veejay size
slut = input()
print('Get ready for a mindblowing handjob, ' + slut)
print('The wirth of your peepee:')
print(len(slut))
print('What is your sexual fantasy?') # ask for their fantasy
booba = input()
print(' You shall be ' + str(int(booba) + 1) + ' booby-mitized')
77
def intro():
    
    choice = input("\nProceed")
    if choice in continue_text:
        intro()
    else:
        intro()
    time.sleep(1) 
    
def start():
    print('Slutty Quest', font='caligraphy''green', attrs=['bold'])
    
    print ("After a drunken night out fantasing about your waifu, you awaken the ")
    print("next morning in an abandonend house in a forest.")
    time.sleep(1)
    print("Head spinning and struggling to remember, you stand and marvel at your new, ")
    print("unfamiliar setting. The peace quickly fades when you hear a ")
    time.sleep(1)
    print("cute voice emitting behind you. A cute girl with small nice boobs enough to breastfeed you for life is ")
    print("sleeping towards you. You will:")
    time.sleep(1)
    print ("""  A. Wake her up and talk to her 
                B. Pick her up and run to your house 
                C. Rape her right there like the coward you are""")
    choice = input(">>> ") # kys please
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
   print ("\nThe girl gets startled by getting picked up suddenly, As she was about to scream, "
   "you see a huge medieval vikling dude with an axe. Will you:")
  
   print ("""A. make her shut up and hide
             B. Leave her behind and hide like a coward
             C. Run towards a nearby alley with her""")
   choice = input(">>> ")
   if choice in reply_A:
    option_hide()
   elif choice in reply_B:
    option_coward()
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
  
  print ("""  A. Ask her to have sex with her
              B. Rape her like a degenerate!
              C. Run away from her like an incel""")
  choice = input(">>> ")
  if choice in reply_A:
    print ("\nYou hide in dark, the medieval vikling dude that heard the girl's scream "
            "pass by, but "
            "Another medieval vikling dude notices you there, so...\n\nYou were Caught!")
    option_caught()
  elif choice in reply_B:
   if condom > 0:
    print ("\nAt this point you just don't care about anything anymore "
           "you just want to sex this girl! \n\nYou are a horny bastard!")
    option_horny()
   else: #If the user didn't grab the condom
     print ("\nYou should have picked up that condom. She's was horny af and would love to give you the most awesome blow job! "
            "\n\nYou died like a pig!")
  elif choice in reply_C:
    print ("You continue to run with the girl and then you find a way out.")
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
  print("behind a delapitated building, waiting for the dudes to come ")
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
    print ("\nYou quickly sticks the purple dildo , into your")
    time.sleep(1)       
    print("your arse like a faggot")
    time.sleep(1)       
    print("\nYou notice your arse bleeding.")
    time.sleep(1)       
    print("\n\nThis got weird, but you destroyed your butt hole!")
  else: #If the user didn't grab the sword
     print ("\nMaybe you should have sex the girl. "
     "\n\nYou regret being born!")
     option_loser()
    
def option_loser():
    time.sleep(1)
    print ("\nThe dudes catch and you are senteced to prison with faggots in your cell!\n\nButthole RAPED ENDING")
    
def option_sex():
    time.sleep(1)
    print ("\nYou enjoyed an awesome sex with the girl and she begs you for more ")
    time.sleep(1)
    print("\nWhile you were piercing your big cock trough her vagina... ")
    time.sleep(1)
    print("\nWhat?! Your condom starts bursts... The girl starts to morphs ")
    time.sleep(1)
    print("\nInto a snake?! She turns into a giant snake like a chinese dragon! You had no option but to kill the snake ")
    time.sleep(1)
    print("\nThe girl thanks you for saving her and becomes your wife \n\nHERO ENDING SOMEHOW!?")
    
def option_sex():
    time.sleep(1)
    print ("You silently sticks your dick inside the girl's sweetass vagina... ")
    time.sleep(1)     
    print("She seems to enjoy it, you keep fucking her more and more THEN!")
    time.sleep(1)       
    print("She tranforms into fox! Scared you try to get your dick away ")
    time.sleep(1)       
    print("But she doesn't let you... You are almost there! ")
    time.sleep(1)       
    print("The fox starts to moan bizarrely, you CUM! ")
    time.sleep(1)       
    print("The fox gets killed by a nearby exorcist from ")
    time.sleep(1)       
    print("the same abandoned house as the girl you were sexing.")
    time.sleep(1)
    print("\nPlease kys\n\n!")
    
def option_wake():
    time.sleep(1)
    print("\nYou ask the girl to see if she's okay")
    print("She reply 'yes' \n\n")
    time.sleep(1)
    print("\nYou take her to her church and wed her "
          "You are officially married to her.")
    time.sleep(1)
    print("You sex her for the rest of your life")
    
def option_hide():
    time.sleep(1)
    print("\nAs you were hiding with her, you rethink your actions like the coward you are ")
    time.sleep(1)
    print("You tell the girl your original intentions and asks for forgiveness like a simp.")
    time.sleep(1)       
    print("\nShe hates you!")
    print("You are such a loser!\n\n")
    
def option_calm():
    time.sleep(1)
    print("\nThe girl calms down and decides to follow you ")
    time.sleep(1)
    print("She seems curious about where you were heading...")
    time.sleep(1)
    print("You told her that she can enter your home. "
        "After you gave her some water and food,"
        "you make a very daring request to her.")
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
    print("\nAs the girl is front of you was taking of off her clothes,")
    time.sleep(1)
    print("you couldn't do anything else but stare at her modest formed ")
    time.sleep(1)
    print("but round soft breasts, her chaste and small pink")
    time.sleep(1)
    print("little vagina, her perfectly shapped buttocks and at her nice and meaty thighs, Your penis got hard at the")
    time.sleep(1)
    print("thought of taking the virginity off a her with such a swollen and lustful body.")
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
    print("that as a girl, she hardly even knows the meaning of those words.")
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
    print("\nShe gently started sucking your")
    time.sleep(1)
    print("cock, you told her which part of your balls, she should lick to make you feel good.")
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
    print("to marry her and make sure, she didn't profaned her status as a virgin in vain.")
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
    print("She told that she wanted God's forgiveness.") 
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
  print("\nIt does not end here!!!\n\n")
  time.sleep(1)
  print("Thanks for Playing!")
  print("Made by Erik.")
    
