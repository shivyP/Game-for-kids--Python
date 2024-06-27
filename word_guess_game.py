#Shivangi Prajapati
#Word guessing game with two levels
import pygame
import random
import time
from pygame import mixer   ##for the background audio
import os

#------------------------
#initialise the pygame
#------------------------
pygame.init()
screen=pygame.display.set_mode([800,600])
pygame.display.set_caption("My word guessing game")
#setting the icon
icon= pygame.image.load ("media/image/logo.png") # load the icon image in the variable
pygame.display.set_icon(icon)

#--------------
#Defining colors
#---------------
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 150, 0)
blue = (0, 50, 85)
yellow = (255, 255, 0)
hover_green = (0, 100, 0)
hover_yellow = (200, 200, 0)
light_red = (150, 0, 0)
hover_red= (255,0,0)
hover_green=(0,255,0)
screen_color=(204,255,255)
text_color=(204,255,229)
#-----------
#clock
#-----------
clock = pygame.time.Clock()


#----------------------
#loading reqired images 
#----------------------
wordFrame =pygame.image.load("media/image/backframe.jpg")    #On which word would be printed
wordFrame= pygame.transform.scale(wordFrame,(800,280))
scoreButton =pygame.image.load("media/image/score.png")      #The score button
levelButton =pygame.image.load("media/image/level.png")      #The level button
#heart = pygame.image.load("heart.jpg")            #The heart-- chances left for each word
inputText = pygame.image.load("media/image/input.png")        #Here the programmer will guess the word, and marks will be displayed for once
#percent = pygame.image.load("media/image/percents.png")
background=pygame.image.load("media/image/back.png")

#-------------
#fonts
#-------------
wordGuessFont = pygame.font.Font("media/font/Brightly Crush Shine.otf", 50)   #Font for the to be guessed word
wordType = pygame.font.SysFont("Calibri", 30)                   #Font for the word to be typed by user
scoreFont = pygame.font.SysFont("Comic Sans MS", 25)            #Font for score and level
helpFont = pygame.font.SysFont("Arial", 22)             #Font for start screen help
nameFont = pygame.font.SysFont("CopperPlate Gothic",25)        #Font for displaying marks (5 out of 10)
msgFont = pygame.font.SysFont("CopperPlate Gothic",50)          #Font for displaying scores at the end
lifeFont = pygame.font.SysFont("Juice ITC", 50)
ansFont=pygame.font.Font("media/font/Almond Nougat.ttf",50)
font= pygame.font.Font("media/font/Brightly Crush Shine.otf",32)
totFont= pygame.font.SysFont("Eras Demi ITC",50)
gameOverFont=pygame.font.Font("media/font/DIMIS___.ttf",50)
ans=pygame.font.Font("media/font/Schoolwork-Regular.ttf",40)
ansL1=pygame.font.Font("media/font/Schoolwork-Regular.ttf",55)

#-------------------------
#variables for the level 1
#--------------------------


list1={}## will conatin all the images 
list2={} ## will have souds
chance=[]## will have the images to display the chances ,heart 
list1X=30
list1Y=240
imgSize=(120,150)
chanceX=100
chanceY=530

imgChoose=[]   # will contain image choosen 
coordinates={} #will contain the coordinates of the choosen images 
levelOnePoints=0
correct=0
#click = pygame.mouse.get_pressed()
#----loading images-----
img1=pygame.image.load("media/image/cat.png")
img2=pygame.image.load("media/image/dog.png")
img3=pygame.image.load("media/image/butterfly.png")
img4=pygame.image.load("media/image/elephant.png")
img5=pygame.image.load("media/image/giraffe.png")
img6=pygame.image.load("media/image/lion.png")
img7=pygame.image.load("media/image/panda.png")
img8=pygame.image.load("media/image/peacock.png")
img9=pygame.image.load("media/image/zebra.png")
img10=pygame.image.load("media/image/parrot.png")

##--- add imges to the list--
list1['cat']=img1
list1['dog']=img2
list1['butterfly']=img3
list1['elephant']=img4
list1['giraffe']=img5
list1['lion']=img6
list1['panda']=img7
list1['peacock']=img8
list1['zebra']=img9
list1['parrot']=img10

#---loading sounds -----
list2['cat']=mixer.Sound('media/sound/cat.mp3')
list2['dog']=mixer.Sound('media/sound/dog.mp3')
list2['butterfly']=mixer.Sound('media/sound/butterfly.mp3')
list2['elephant']=mixer.Sound('media/sound/elephant.mp3')
list2['giraffe']=mixer.Sound('media/sound/giraffe.mp3')
list2['lion']=mixer.Sound('media/sound/lion.mp3')
list2['panda']=mixer.Sound('media/sound/panda.mp3')
list2['peacock']=mixer.Sound('media/sound/peacock.mp3')
list2['zebra']=mixer.Sound('media/sound/zebra.mp3')
list2['parrot']=mixer.Sound('media/sound/parrot.mp3')
#print("The list 2 is:",list2)
#-------------------------
#--------chances limit------------
life=pygame.image.load("media/image/life.png")
totLife=5
for i in range (0,totLife):
   chance.append(life)
#print (chance)


#--------------------------
#variables of level 2
#--------------------------
alphaImg={}                #a list will all the alphabet images
wordGuessImg={}            ##will conatin all the images of the words to guess
word=[]                    #coontain all the list of fruits (from the external file)
wordChoice=""              #will contain the random word choosen 
imgCoordinates=[]          #will conatin the coordinates of the alphabets displayed on the screen
keyCoordinates=[]          #will cotain alphabet on the screen
choiceList=[]              #will contain all the iamges that have been chosen,
                           #prevent the repeating of the same word
letter=""                  #will contain the words formed by clicking on the alphabet
levelTwoPoint=0
levelTwoCorrect=0

#---------------------------------------------------
#Functions
#-----------------------------------------------------

#the start screen of the game 
def startscreen():
   screen.fill(blue)
   pygame.display.update()
   heading = wordGuessFont.render("WORD GUESSING GAME", True, yellow)
   screen.blit(heading, [150,50])
   pygame.display.update()
   clock.tick(1) #wait before loading other elements 

   

   
##def user(name):
##    #print("The name is:",name)
##    file= loadFile('user.txt')
##    #print(file)
##    for i in range (0,len(file)):
##      # print(file[i])
##       if str(name) == str(file[i]) :
##          
##          n=wordType.render("Welcome back"+name,True,screen_color)
##          screen.blit(n,(504,178))
##          
##       else:
##          n=wordType.render("Welcome "+name+"!",True,screen_color)
##          screen.blit(n,(504,178))
##     
   
#instructions lines   
def instructions():
    Line1 = helpFont.render("Level 1:", True, (204,0,204))
    Line2 = helpFont.render("     -> sound will be played ", True, text_color)
    Line3 = helpFont.render("     -> Click on the correct image", True, text_color)
    Line4 = helpFont.render("     -> You will have 5 attempts to guess the animal", True,text_color)
    Line5 = helpFont.render("     -> You must pass level 1 to play the next level", True,text_color)
    Line6 = helpFont.render("Level 2:", True, (204,0,204))
    Line7 = helpFont.render("     -> A jumbbled word will be on the screen", True, text_color)
    Line8 = helpFont.render("     -> Click on the alphabet to write the word ", True,text_color)
    Line9 = helpFont.render("     -> You have 5 attempts to guess the word ", True, text_color)
    Line0 = helpFont.render("     -> Points will be given for each correct answer", True, text_color)

#display the instaructions
    screen.blit(Line1, [60,320]) 
    screen.blit(Line2, [60,345])
    screen.blit(Line3, [60,370])
    screen.blit(Line4, [60,395])
    screen.blit(Line5, [60,420])
    screen.blit(Line6, [60,445])
    screen.blit(Line7, [60,470])
    screen.blit(Line8, [60,495])
    screen.blit(Line9, [60,520])
    screen.blit(Line0, [60,545])

    pygame.display.update()
    

#for the text on the button  
def text_objects(text, font):
    textArea = helpFont.render(text, True, black)
    return textArea, textArea.get_rect()

#button function   
def button (message,x,y,width,height,i_color,a_color):
   #gets the mouse postion 
   mouse = pygame.mouse.get_pos() #will be an array 
   click = pygame.mouse.get_pressed()
   if x+width> mouse[0] > x and y+height> mouse[1]>y:
      #----hover effects-----
      pygame.draw.rect(screen, a_color,(x,y,width,height)) # x,y, width, height
      if click[0] == True:
         return True
   else:
       pygame.draw.rect(screen, i_color,(x,y,width,height)) # x,y, width, height   
   #-- text on the button ----
   
   smallText= pygame.font.Font("freesansbold.ttf",20)
   text_area , text_rec = text_objects(message, smallText) #passing parameters to the function
   text_rec.center= ((x+(width/2)), (y+(height/2)))
               # x+ width/2      #y+height/2
   screen.blit(text_area,text_rec)
   
   pygame.display.update()


#design rectangles 
def rec(x,y,w,h,color):
   pygame.draw.rect(screen,color,(x,y,w,h)) 

def levelScreen(level):
   #print("hello")
   screen.fill(blue)
   pygame.display.update()
   #screen.blit(background, [0,0])
   screen.blit(scoreButton, [0,0])        #Displaying the score button
   screen.blit(levelButton, [565,0])      #level
   screen.blit(wordFrame, [0,200])        #image frame 
   screen.blit(inputText, [0,110])        #correct frame
   screen.blit(inputText, [0,420])        #find frame 
   levelText = scoreFont.render("Level: "+str(level), True, black)
   screen.blit(levelText, [610,25])
   pygame.display.update()
   if level==1:
      intro("Listen & Choose",270,35)
   else:
      intro("Find me!",325,20)
   #time.sleep(3)
#------------------------------------
#level 1 functions
#------------------------------------

def intro(titleText, x, y):   
   display_title= font.render(titleText, True, (255,107,107))
   screen.blit (display_title, (x,y))
   pygame.display.update()
   clock.tick(2)
   
def dispImgaes(listImg):
   global coordinates,chance   #gets the coordnates variables
   global chanceX,chanceY,totLife
   global levelOnePoints
   lifes(chance,chanceX,chanceY,totLife)
   dispScore(levelOnePoints,1)
   options= choose(listImg)# to dispaly random 3 images
   #print("The options are:",options)
   #print("the chosen list is:",options)
   x_axis=100
   keys=[]
   #dispaly the 3 randomly choosen images 
   for i in options:
     OneKey= list(listImg.keys())[i]
     coordinates[OneKey]=(list1X + x_axis,list1Y)
     keys.append(OneKey)
     animal=listImg[OneKey]
     animal=pygame.transform.scale(animal,(imgSize))
     image= screen.blit(animal,(list1X + x_axis,list1Y))
     x_axis+=200
   pygame.display.update()
   ques=sound(keys) #call the sound function
   #print("The coordinates are:",coordinates)
   return ques

#choose random images and pass it to the calling function 
def choose(listData):
   global imgChoose
   choice=[]  #will contain the three images to display
  
   for i in range(0,len(listData)-1):
      num= random.randint(0,len(listData)-1) #choose a random number to extarct that image 
      keys=list(listData.keys())    #get all the  keys (name of the images)
      #print("Keys in list:",keys)
      while keys[num] in imgChoose:  #if the image chooswn was alreday a sound played, than choose another one 
         num= random.randint(0,len(listData)-1)
      if len(choice)== 3:
         break
      elif not (num in choice)and len(choice)<=3:
         choice.append(num)
   
   return(choice)


#dispaly the chances available 
def lifes(possibility,x,y,tL): #possibility will be the list
  
   x_axis=0
  # print("The length is ", totLife)
  # print(possibility)
   textLife= lifeFont.render("Lifes:",True,white)
   screen.blit(textLife,(x-80,y))
   if tL<5:
      pygame.draw.rect(screen,blue, [x,y,323,y+35])
   for i in range (0,tL):
    #  print("i:",i)
      c_guess=possibility[i]  # list will number of hearts generated 
      c_guess=pygame.transform.scale(c_guess,(35,35))
      image=screen.blit(c_guess,(x+x_axis,y+10))
      x_axis+=37   #increase the x-axis
   pygame.display.update()
   

#choose random sound and play it 
def sound(sound_keys):
   
   global imgChoose
   index= random.randint(0,2)
   s_key= sound_keys[index]
   imgChoose.append(sound_keys[index])#played sound will be saved,prevent the repetition
   #print("The sound_keys are:",imgChoose)
   
   sound=list2[s_key]
   pygame.display.update()
   time.sleep(1)
   sound.play()
   
   return s_key

#replace this with calling the rec function 
def animalName(name):
   #render the text
   anName=nameFont.render("Find:"+" "+name, True, (0,0,0))
   #display on the screen
   screen.blit(anName,(100,450))
   name=""
   pygame.display.update()


#check the answer, if yes than happy sound, if not than try again
def answer(axis,q_key):
   global totLife
   global correct,levelOnePoints
   global remLife,imgSize
   x=0
   y=0
   mouse = pygame.mouse.get_pos()
   mouse_pos=()
   
   #print("The click is:",click)
   for i in axis:
      if i== q_key:
         ans_coordinates= axis[i]
         x=ans_coordinates[0]
         y=ans_coordinates[1]
   
   
   click = pygame.mouse.get_pressed()     
   for event in pygame.event.get():
         if event.type == pygame.QUIT:
                pygame.quit()# need this line to close the widnow or it wont work 
                quit()
         if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            

            if x+imgSize[0]>mouse_pos[0]> x and y+imgSize[1]>mouse_pos[1]>y:
               
               clap=mixer.Sound('media/sound/clapping.mp3')
               clap.play()
               #score_value+=50
               #print("The points are:",points)
               correct+=1
               screen.blit(scoreButton, [0,0])
               screen.blit(inputText, [0,110]) 
               levelOnePoints=score(levelOnePoints,1)
               pygame.display.update()
               time.sleep(2)
               return True
            
            
            if not(x+imgSize[0]> mouse_pos[0] > x and y+imgSize[1]> mouse_po[1]>y):
               if (130+120>mouse_pos[0]>130) or (330+120>mouse_pos[0]>330) or (530+120>mouse_pos[0]>530):
                 if 240+150>mouse_pos[1] >240 and totLife!=0:
                     #print("worng")                       
                     wrong=mixer.Sound('media/sound/tryAgain.mp3')
                     wrong.play()
                     
                     time.sleep(2)
                     totLife-=1
                     
            if totLife==0:
               lifes(chance,chanceX,chanceY,totLife)
               screen.blit(wordFrame, [0,200])
               screen.blit(inputText, [0,420])  
               write=ansL1.render("Answer:",True,green)
               screen.blit(write,[100,280])
               showAnswer=list1[imgChoose[-1]]
               showAnswer=pygame.transform.scale(showAnswer,(imgSize))
               screen.blit(showAnswer,[350,240])
               
               dispScore(levelOnePoints,1)
               pygame.display.update()
               totLife=5
              # print("tot life is:",totLife)
               time.sleep(5)
               return True 
               
  # return False


def remove(level):
   levelScreen(level)
   

#--------------make changes in this (look level2 )------

def score(levelPoints,level):
   global totLife
   if totLife == 5:
      levelPoints+= 50
   elif totLife == 4:
      levelPoints+= 40
   elif totLife == 3:
      levelPoints+= 30
   elif totLife == 2:
      levelPoints+= 20
   elif totLife == 1:
      levelPoints+= 10
   else:
      levelPoints+=0
      
   dispScore(levelPoints,level)
   return levelPoints     
   
 
def dispScore(levelPoints,level):
   global correct,levelTwoCorrect
   if level==1:
     c=correct
     t=5
   if level==2:
     c=levelTwoCorrect
     t=10
   
   reward=scoreFont.render("Score:"+ str(levelPoints),True,black) 
   screen.blit(reward,[25,20])
   
   right=nameFont.render(str(c)+" OUT OF "+str(t),True,black)
   screen.blit(right,[300,140])


#------------------------------
#level two functions
#------------------------------
###function to load all the png files in the a given directory    
def loadImg(List,directory):
   key=""      #name of the file, than key in the dictionary
   for file in os.listdir(directory):
    if file.endswith(".png"):
        location=directory+str(file) #directory will be passed when fuction is called 
        key=""
        for i in range(0, len(file)):
           if file[i]==".":
              break
           key+=file[i]
           
        List[key]=pygame.image.load(location)

##load the file and return the conatent of it 
def loadFile(fileName):
     file=open(fileName,'r')
     fileContent=file.read().split(',')
     file.close
     return fileContent

#### choose a random word from the  
def chooseWord(wordList):
   # print("The wordList is:",wordList)
    global wordChoice
    global choiceList
    choice=random.choice(wordList)   #chose a radom word from the given list 
    while choice in choiceList:      #to prevent the selection of same element 
       choice=random.choice(wordList)
    choiceList.append(choice)        #new element will be stored in the choiceList
    
    wordChoice=choice                #the choosen word will be stored globally for other fucntions 
    chooseImg(choice)                #diaply images required
    



#--display the choosen image    
def chooseImg(wordImg):
   global wordGuessImg
   global word                   #list of all the words from the external file
   
   wImg=wordGuessImg[wordImg]   #get the image given the key(wordImg),i.e. wordImg['apple']
   wImg=pygame.transform.scale(wImg,(160,150))
   image= screen.blit(wImg,(120,250)) #coordinates
   jumble(wordImg)             #pass the word to jumble it 
   
def jumble(word): 
     # sample() method to shuffle the characters of the word
     random_word = random.sample(word, len(word))
    # print("The the random_word:",random_word) 
     jumbled = ''.join(random_word)#joins the element in the list
     
     #if the shuffled word is same as orginal
     #shuffle again
     while word == jumbled:
        random_word = random.sample(word, len(word))
        jumbled= ''.join(random_word)
     
    #if the shuffle is succefull and outcome diffrent from original
    #display it 
     dispText(nameFont,jumbled,(0,0,0,0),400,250,42)
     
     jumImg(random_word) #pass the suffled word to diaply required aplbhates


####function to display alphabets required 
def jumImg(wL):
    global alphaImg
    global imgCoordinates
    global keyCoordinates
    global wordText
    subImg={}# will conatin the extracted alphabets(images) 
    xInc=20
    key=""   # will contain the key one by one 


    #get the images for the choosen word
    #and display them on the screen
    
    for i in range (0,len(wL)):
       key=wL[i]
       subImg[key]=alphaImg[key] #print the image one by one 
       wImg=subImg[key]
       wImg=pygame.transform.scale(wImg,(50,50))
       image= screen.blit(wImg,(60+xInc,438))
       imgCoordinates.append((60+xInc,438))### coordinates of the images stored required 
       keyCoordinates.append(key)## keys with coordinates required later
       xInc+=60  #increase the x-axis to place the next image next to it 


#draw the screen to dispaly the letters choosen by player
def rec(x,y,w,h,color):
   pygame.draw.rect(screen,color,(x,y,w,h))   #draw a rectangle with the same color as the background


#display the letters choosen by player on the screen   
def dispText(fontType,message,color,x,y,size):
   s=fontType.render(message,True,color)
   screen.blit(s,(x,y))


   
#display letters required to guess the correct fruit name 
def dispLetter(letter):
   la=nameFont.render(letter,True,red)
   screen.blit(la,(400,300))
   pygame.display.update()
   return True

#identify the charaacter choosen by the user    
def userChoice(axis,wChoice,key,mousepos):
   clock = pygame.time.Clock()
   #get the mouse click and arrow coordinates
   global letter,totLife
   global wordChoice  
      
   for i in range (0,len(axis)):
         if axis[i][0]<mousepos[0]<(axis[i][0])+54 and axis[i][1] <mousepos[1]< (axis[i][1])+54:
            letter+=key[i]
            done=dispLetter(letter)
            
   if len(letter)== len(wordChoice):  
      return True 

#check if the word type by user is equal or not to the original word 
def correctTwo (aL,wordChoice):
     # pygame.time.wait(3)
      global keyCoordinates,imgCoordinates
      global letter,totLife,levelTwoCorrect
      global chance,chanceX,chanceY
      
      if len(letter)== len(wordChoice):
         if letter == wordChoice:
            keyCoordinates=[]  #empty it to conatain coordinates of new word 
            imgCoordinates=[]  #empty it to conatain coordinates of new word
            
            clap=mixer.Sound('media/sound/clapping.mp3') ###--------make it global
            clap.play()
            letter=""
            time.sleep(2)
           # print("correct")
            levelTwoCorrect+=1
            
            return True 
         else:
            letter=""
            #print("wrong")
            wrong=mixer.Sound('media/sound/tryAgain.mp3')###--------make it global
            wrong.play()
            totLife-=1
            lifes(chance,chanceX,chanceY,totLife)#display the attempts left
            time.sleep(2)
            rec(400,300,220,40,(255,255,255))# empty the text area(where the letters are displayed 

#display the answer when the user attempts are finished 
def dispAnswer(word):
    rec(400,300,265,55,(255,255,255))
    dispText(ans,"Answer:"+word.upper(),green,400,300,32)
    pygame.display.update()
    time.sleep(2)#waiting time 
    
def endoflevel(levelScore):
   #animation for the level change at the end  
    for printRect in range(0,610,10):
        pygame.draw.rect(screen, screen_color, [0,600-(printRect),800,50+(printRect)])
        pygame.display.update()
        clock.tick(50)
    clock.tick(1)
    #animation to display the total score of the level
    finalScore=totFont.render("Total score:"+str(levelScore),True,green)
    screen.blit(finalScore,[200,240])
    pygame.display.update()
    time.sleep(1)
    
    #animation to remove the total score 
    for printRect in range(0,610,10):
        pygame.draw.rect(screen, screen_color, [0,600-(printRect),800,50+(printRect)])
        pygame.display.update()
        #time.sleep(1)

def endGame():
    global levelOnePoints,levelTwoPoint
    #animation to display the end of the game 
    for printRect in range(0,610,10):
        pygame.draw.rect(screen, screen_color, [0,600-(printRect),800,50+(printRect)])
        pygame.display.update()
        clock.tick(50)
    clock.tick(1)
    #animation to display the overall socre ( from both levels)
    finalScore=totFont.render("Overall score:"+str(levelOnePoints+levelTwoPoint),True,red)
    screen.blit(finalScore,[200,240])
    pygame.display.update()
    time.sleep(1)
    #animation for the last game over screen 
    for printRect in range(0,610,10):
        pygame.draw.rect(screen, blue, [0,600-(printRect),800,50+(printRect)])
        pygame.display.update()
        clock.tick(50)
    clock.tick(1)
    finalScore=gameOverFont.render("Game Over",True,white)
    screen.blit(finalScore,[260,240])
    pygame.display.update()
       # time.sleep(1)


#function to display the start of the level
def changeScreen (level):
   for i in range(0,610,10):
        pygame.draw.rect(screen, screen_color, [0,0+(i),800,50+(i)])
        pygame.display.update()
        clock.tick(50)
   finalScore=totFont.render(("Level "+str(level)).upper(),True,(0,102,204))
   screen.blit(finalScore,[280,220])
   pygame.display.update()
   time.sleep(1)
    

def levelTwo():

   levelScreen(2)
   time.sleep(1)
   global wordChoice,alphaImg
   global imgCoordinates,correct
   global keyCoordinates,totLife
   global letter,levelTwoPoint
   global wordText,countTwo
   intro("Find me!",325,20)
   
   totLife=5
   ans=False #will have the answer from the correct function/true or false 
  # pygame.display.update()
   #time.sleep(1)
   chooseWord(word)   #start the actual game
   
   pygame.display.update()
   rec(400,300,220,40,(255,255,255))   #letters screen 
   dispScore(levelTwoPoint,2)
   lifes(chance,chanceX,chanceY,totLife)
   
   while True:
      click = pygame.mouse.get_pressed() #gets the mouse clicks 
      for event in pygame.event.get():
         if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos() #caputer the single click of the mouse 
           
           
            if len(letter)<=len(wordChoice) and totLife!=0:
                 #check if the click has been captured on alphabets 
                 ans=userChoice(imgCoordinates,wordChoice,keyCoordinates,mouse_pos)
                 
                
                 if ans==True:
                    if correctTwo(letter,wordChoice):
                        correct+=1
                        levelTwoPoint=score(levelTwoPoint,2)
                        #print("The levelPointsocre:",levelTwoPoint)
                        if len (choiceList)== len (word):
                           #print("hey i am in here")
                           
                           screen.blit(scoreButton, [0,0])
                           screen.blit(inputText, [0,110])#correct(right)
                           levelTwoPoint=score(levelTwoPoint,2)
                           pygame.display.update()
                           time.sleep(3)
                           endoflevel(levelTwoPoint)
                           endGame()
                           #return True
                        else:
                           totLife=5
                           remove(2)
                           levelTwo()
         if totLife== 0:
            dispAnswer(wordChoice)
            pygame.display.update()
            pygame.time.wait(2)
            keyCoordinates=[]
            imgCoordinates=[]
            remove(2)
            totLife=5
            levelTwo()
            
      for event in pygame.event.get(): # capture all the events are 
             if event.type == pygame.QUIT:
                pygame.quit()# need this line to close the widnow or it wont work 
                quit()
         
     # pygame.display.update()
      
      pygame.display.flip()
      

###############required in level 2###################
#---loading images and words required        
loadImg(alphaImg,"media/image/level2/alphabet/")     #calling the function to load alphabet images    
loadImg(wordGuessImg,"media/image/level2/fruit/")   #calling the function to load images of word to guess
word=loadFile("name.txt")           # the list of the word is the file will be stored in words
##################################################       

   

def levelOne():
   #screen.blit(bgImage,(80,120))
   changeScreen (1)
   levelScreen(1)
   time.sleep(1)
   global totLife,imgSize
   global coordinates,levelOnePoints
   question=""
   
   gameExit=False
   showAnswer=None
   #intro("Listen & Choose",270,35)
  
   #mouse = pygame.mouse.get_pos() #get the position of the mouse,will be an array
   lifes(chance,chanceX,chanceY,totLife)
   dispScore(levelOnePoints,1)
   question=dispImgaes(list1)
   animalName(question)
   
     #main function 
   while True:
      
      if len(imgChoose)<6:
         intro("Listen & Choose",270,35)
         lifes(chance,chanceX,chanceY,totLife)
         animalName(question)
         if answer(coordinates,question)== True and totLife!=0:
            
            #print ("The len of img is", len(imgChoose))
            if len(imgChoose)== 5:
              # print("Hey i am in here")
               screen.blit(scoreButton, [0,0])
               screen.blit(inputText, [0,110])        #correct frame 
               #levelOnePoints=score(levelOnePoints,1)
               dispScore(levelOnePoints,1)
               pygame.display.update()
               time.sleep(2)
               endoflevel(levelOnePoints)
               return True

            else:
               #levelOnePoints=score(levelOnePoints,1)
               pygame.time.wait(2)
               totLife=5
               remove(1)
               pygame.display.update()
               question=dispImgaes(list1)
                     
 
      #show_score(650,560)
     #dispScore(levelOnePoints,1)
     # clock.tick(100)
      pygame.display.update()



#main fuction to start the game 
def main():
   clock.tick(2)
   startscreen()
   uName=""
   userName=nameFont.render("Username:", True,white)
   screen.blit(userName, (220,180))
   rec(370,175,130,40,white)
   choice =0
   while choice==0:                    
      b1 = button ("Play",200,250,100,50,green,hover_green)
      b2 = button ("Help",350,250,100,50,red,hover_red)
      b3 = button ("Quit",500,250,100,50,yellow,hover_yellow)
      
      #userName()
      if b1 == True: 
         #levelOne()
         if levelOne():
            changeScreen (2)
            clock.tick(4)
            levelTwo()
         choice=1
      elif b2 == True:
         #print("I wasnt instrauctions")
         instructions()
      elif b3 == True:
        # clock.tick(1)
         pygame.quit()# need this line to close the widnow or it wont work 
         quit()
         
      #capture events 
      for event in pygame.event.get(): # capture all the events are 
             if event.type == pygame.QUIT:
                pygame.quit()# need this line to close the widnow or it wont work 
                quit()
                
            #capture keystroke and record it in a variable 
             if event.type == pygame.KEYDOWN:
               if len(uName)<10:
                    char = (chr(event.key))
                    uName+= char
                    n=wordType.render(uName,True,black)
                    screen.blit(n,(370,178))
               if event.key == pygame.K_RETURN: 
                    n1=wordType.render("Welcome "+uName.upper(),True,screen_color)
                    screen.blit(n1,(504,178))
      pygame.display.flip()
      
main()
