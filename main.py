###Variable Assignments

app.stepsPerSecond = 5
app.debugBuffer = 50
app.startTheVariables = 0
app.background = gradient('black','black','darkRed',start='top')
app.choiceStage=1
app.corruptSpeed=2
app.checkStatus=False
###Shape Config

cog = Image('https://i.ibb.co/PQfPdMQ/gaysex.png',0,360)
cog.height = 40
cog.width = 40
mainMenu = Image('https://i.ibb.co/Sxb9sqv/corruption.png',0,0)
mainMenu.width = 440
mainMenu.height = 400
mainMenu.centerX = 200

startButton = Rect(90, 205, 220, 80, opacity=app.debugBuffer)

corruption = Rect(25,25,1,25,fill="red")
power = Rect(25, 75, 75, 25, fill="aqua")
popularity = Rect(25, 125, 150, 25, fill="yellow")

Label('Corruption', (corruption.centerX+290),corruption.centerY,fill='white',size=15,bold=True,font='orbitron')
Label('Power', (corruption.centerX+290),power.centerY,fill='white',size=15,bold=True,font='orbitron')
Label('Popularity', (corruption.centerX+290),popularity.centerY,fill='white',size=15,bold=True,font='orbitron')

Rect(25, 25,350,25,fill=None,border='white',borderWidth=5)
Rect(25, 75, 350, 25, fill=None, border="white" , borderWidth=5)
Rect(25, 125, 350, 25, fill=None, border="white" , borderWidth=5)


TitleText = Label('+10 Corruption -10 Power +5 Popularity', 200, 200, size=20, bold=True, fill="red", visible=False)

option1 = Rect(50, 250, 75, 50, fill="blue")    
        
option2 = Rect(275, 250, 75, 50, fill="blue")

mainMenu.toFront()
startButton.toFront()
#####
box = Rect(150, 230, 30, 30, fill=None, border="black")
TaC = Group(
Rect(0, 0, 400, 400, fill="white"),
Label("Terms and Conditions", 200, 25, bold=True, size=20),
Label("These terms and conditions govern your use of Corruption, by accessing you agree to these", 200, 50, size=10),
Label("terms, if you do not agree, please do not access the game", 200, 60, size=10),
Label("1. License: We grant you a limited, non exclusive, non transferable, revocable items", 200, 70, size=10),
Label("2. Age requirement: By using the game, you affirm you are atleast 13 years old", 200, 80, size=10),
Label("If you are under 13 years old, you may not use the game without parental approval", 200, 90, size=10),
Label("3. Prohibited Conduct: You agree not to: Use the game for unlawful purposes", 200, 100, size=10),
Label("Attempt to gain authorized access to any part of the game, or any connected systems", 200, 110, size=10),    
Label("5. Intellectual Property: The game, including all content, graphics, features, and design", 200, 120, size=10),
Label("are owned by the company and are protected by copyright, trademark, and other laws", 200, 130, size=10),
Label("6. User Content: By submitting any content to the game, you grant permission for", 200, 140, size=10),
Label("reproduction and modification of such content in any form now or later", 200, 150, size=10),
Label("7. Privacy: Your privacy is important. Our privacy policy outlines how we collect", 200, 160, size=10),
Label("your personal data. By agreeing to the terms and using the game, you consent to the ", 200, 170, size=10),
Label("collection and redistribution of your personal information", 200, 180, size=10),
Label("8. Academic Use: In academic settings, such as classrooms, use of the game is to be", 200, 190, size=10),
Label("evaluated by the teacher, in which the teacher will grade the project. The game does not", 200, 200, size=10),
Label("guarantee or imply a particular grade or outcome as a result of use", 200, 210, size=10),
Label("By clicking the box, you agree", 300, 235, size=10),
Label(" to the terms and conditions", 300, 245, size=10),

box
)

check = Group(
Rect(150, 300, 25, 8, fill="green", rotateAngle=50),
Rect(161, 300, 33, 8, fill="green", rotateAngle=310)

)

check.visible=True
check.centerX=167
check.centerY=243
check.visible=False



Allow = Group(

Label("CONFIRM",200, 320, size=30),
Rect(100, 300, 200, 40, fill=None, border="black"),
)
Allow.visible=False

box.centerX=10000
TaC.centerX=10000
Allow.centerX=10000


#####


###Predef functions

def gameStartForRealNoCap():
    app.startTheVariables = 1
    mainMenu.centerX = 9999 #lmao move it offscreen because deleting is mid
    startButton.centerX = 9999
    
def makeSomeBars():
    corruption.width+=app.corruptSpeed
    popularity.width-=1
    
    if popularity.width >350:
        popularity.width=350
        
    if power.width >350:
        power.width=350
    
def selectOption1(title, c, pw, pu):
    TitleText.visible=True
    TitleText.opacity=100
    TitleText.value=title
    
    app.corruptSpeed*=c
    
    if power.width+pw >0:
        power.width+=pw
    else:
        power.width= 1
    
    if popularity.width+pu >0:
        popularity.width+=pu
    else:
        popularity.width = 1
    
    if popularity.width >150:
        popularity.width=150
        
    if power.width >150:
        power.width=150
    app.choiceStage+=1
def selectOption2(title, c, pw, pu):
    
    TitleText.visible=True
    TitleText.opacity=100        
    TitleText.value=title

    app.corruptSpeed*=c
    power.width+=pw
    popularity.width+=pu
    
    if popularity.width >150:
        popularity.width=150
        
    if power.width >150:
        power.width=150
    app.choiceStage+=1
    
def gameEnd(ending):
    Rect(0,0,400,400,fill='darkRed')
    Label("You Lost!",200,150,size=50,font='orbitron')
    if ending =='power':
        Label("Your power was too low,",200,200,size=25,font='orbitron')
        Label("and you were overthrown",200,250,size=25,font='orbitron')
    if ending =='corrupt':
        Label("Your corruption was too high.",200,200,size=23,font='orbitron')
    if ending =='popularity':
        Label("Your popularity was too low.",200,200,size=20,font='orbitron')
    app.stop()
###Active functions

def onMousePress(mX,mY):
    if startButton.contains(mX,mY):
        gameStartForRealNoCap()
        
    if option1.contains(mX,mY):
        if app.choiceStage==1:
            selectOption1("Title Text", 1.1, -25, -40) # Test values change when implementing actual code
        elif app.choiceStage==2:
            selectOption1("Title Text", 2, -25, -35)
        elif app.choiceStage==3:
            selectOption1("Title Text", 1.1, -25, 25)
        elif app.choiceStage==4:
            selectOption1("Title Text", 1.1, 5, -15)

    ### Maybe use app.choiceStage to check which choices/stats to use        
    if option2.contains(mX,mY):
        if app.choiceStage==1:
            selectOption2("Title Text", 2, -25, 25) # Test value here too
        elif app.choiceStage==2:
            selectOption2("Title Text", 1.1, 30, -35)
        elif app.choiceStage==3:
            selectOption2("Title Text", 2, 25, -10)
        elif app.choiceStage==4:
            selectOption2("Title Text", 2, -10, 15)
            
            
       #####     
    if cog.contains(mX, mY):
        check.centerX=200
        TaC.centerX=200
        Allow.centerX=200
        box.toFront()
        TaC.toFront()
        Allow.toFront()
    if box.contains(mX, mY):
        check.visible=True
        app.checkStatus=True
        Allow.visible=True
    if app.checkStatus==True:
        if Allow.contains(mX, mY):
            TaC.centerX=10000
            check.centerX=10000
            Allow.centerX=10000
        #####
        
def onStep():
    if app.startTheVariables == 1:
        makeSomeBars()
    if corruption.width>350:
        gameEnd('corrupt')
    if power.width<4:
        gameEnd('power')
    if popularity.width<4:
        gameEnd('popularity')
        
    if TitleText.opacity>0:
        TitleText.opacity-=5
    cog.toFront()
  
  
  
    
        
