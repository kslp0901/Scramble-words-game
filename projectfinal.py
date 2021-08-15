from tkinter import * 
import tkinter.messagebox
import random
import string
import timeit
from functools import partial

########## GLOBAL VARIABLES ##############
marks=[]
#While loop terminates after 2 players complete their game

e1=''
t = ''
playNum = 1
i = 0
trial=0
start = 0


##selcting random word text file 'wordslist'##

def enter():
    
    b=a.get()
    textlabel = Label(w1,text="Hi! "+b,bg='black',fg='green',font=20).grid(row=0,column=1)
    enterlabel=Label(w1,text="Start the game!!!",bg='black',fg='pink',font=20).grid(row=2,column=1)
                 
    
def select_word():
    file1=open("word.txt","r")
    words=file1.readlines()
    w=random.choice(words)
    file1.close()
    return(w)

def select_word3():
    file3=open("word3.txt","r")
    words3=file3.readlines()
    w3=random.choice(words3)
    file3.close()
    return(w3)
def select_word4():
    file4=open("word4.txt","r")
    words4=file4.readlines()
    w4=random.choice(words4)
    file4.close()
    return(w4)
def select_word5():
    file5=open("word5.txt","r")
    words5=file5.readlines()
    w5=random.choice(words5)
    file5.close()
    return(w5)
def select_word6():
    file6=open("word6.txt","r")
    words6=file6.readlines()
    w6=random.choice(words6)
    file6.close()
    return(w6)
def select_word7():
    file7=open("word7.txt","r")
    words7=file7.readlines()
    w7=random.choice(words7)
    file7.close()
    return(w7)
def select_word8():
    file8=open("word8.txt","r")
    words8=file8.readlines()
    w8=random.choice(words8)
    file8.close()
    return(w8)
def select_word9():
    file9=open("word9.txt","r")
    words9=file9.readlines()
    w9=random.choice(words9)
    file9.close()
    return(w9)

def shufl(chosenWord):
    e=chosenWord.lower()
    #print(e)
#splitting letters of word
    d=list(e)
    l1=len(e)
##Shuffles charecters in list and printing.
    split_word = e
    while(split_word==e):
       random.shuffle(d)
       split_word=''.join(d)
    print(split_word,end=" ")
    return(split_word)

def playGame(yesOrNo, playerNumber):
    global e1
    global t
    global trial
    global i
    global start
    l= len(e1)
    print("correct word = ", e1)
    print("l = ", l)
    
    # while(i<5):
        # t1=str(input(''))
    t1 = ''

    if yesOrNo == "yes":
        t1 = guessBoxYes.get()
    else:
        t1 = guessBoxNo.get()

    print("got string ", t1)
    t1 = t1.strip('\n')
    t=t1.lower()
    l2=len(t)
    print(l)  #Printing length to for checking
    print(l2)

    if(l2!=l):
        print('check length')
        if yesOrNo == "yes":
            incorrectLenY.config(text = "Length of the entered word is incorrect")
        else:
            incorrectLenN.config(text = "Length of the entered word is incorrect")
        count=0
    else:
               
        if yesOrNo == "yes":
            incorrectLenY.config(text = "")
        else:
            incorrectLenN.config(text = "")
        count=0
        for k in range(0,l):
            if(e1[k]==t[k]):
                count=count+1
            else:
                break

    if(count==l): 
        print('congratulation you guessed correct word')
        if yesOrNo == "yes":
            resultLabelY.config(text = "congratulation you guessed correct word",bg='black',fg='pink')
        else:
            resultLabelN.config(text = "congratulation you guessed correct word",bg='black',fg='pink')
        i=6
    else:
        print('try again')
        if yesOrNo == "yes":
            resultLabelY.config(text = "try again",bg='black',fg='red')
        else:
            resultLabelN.config(text = "try again",bg='black',fg='red')
        i=i+1
    trial=trial+1 #counts number of trails taken.
    if(count==l): #score is 1 if he guessed correct.
        score=0
    else:
        score=1


    if count==l or trial > 5:
        print('you took  %d trials'%trial)
        stop=timeit.default_timer()
        print('Time taken is %dsec'%((stop-start)/3))
        print(score)

        total=(trial+((stop-start)/3)+score)
        
        marks.append(total)
        textToPrint = "you took "+ str(trial) + "trials.\n "+"Time taken is "+str((stop-start)/3)+"sec.\n"+"Score is "+str(score)+"\nTotal is"+str(marks)
    
        if yesOrNo == "yes":
            scoreLabelY.config(text = textToPrint,fg='green',bg='black')
        else:
            scoreLabelN.config(text = textToPrint,fg='green',bg='black')


      

        print("player number = ", playerNumber)
        if playerNumber == 2:
            nextPlayerY.config(state=DISABLED)
            nextPlayerN.config(state=DISABLED)
            if(marks[0]>marks[1]):
                print('Player 2 is the winner')
                if yesOrNo == "yes":
                    winnerLabelY.config(text = "Player 2 is the winner",fg='blue',bg='black')
                else:
                    winnerLabelN.config(text = "Player 2 is the winner",fg='blue',bg='black')
            else:
                print('Player 1 is the winner')
                if yesOrNo == "yes":
                    winnerLabelY.config(text = "Player 1 is the winner",fg='blue',bg='black')
                else:
                    winnerLabelN.config(text = "Player 1 is the winner",fg='blue',bg='black')
        
        # TODO: Disable button
    
def sword():
        global e1
        m=text1.get()
        n=int(m)
       
        print(n)
        print(m)
        if(n==3):
            e1=select_word3()
        elif(n==4):
            e1=select_word4()
        elif(n==5):
            e1=select_word5()
        elif(n==6):
            e1=select_word6()
        elif(n==7):
            e1=select_word7()
        elif(n==8):
            e1=select_word8()
        else:
            e1=select_word9()
        e1 = e1.strip('\n')
        shuffWord = shufl(e1)
        
        mylabel7.config(text=shuffWord)
        mylabel8.config(text=e1)    

def yes_1():
    print("reached 1")
    no_frame.grid_forget()
    yes_frame.grid(row=1,column=0)

def no_2():
    global mylabel6
    global e1
    print("reached")
    yes_frame.grid_forget()
    no_frame.grid(row=1,column=0)
    e1=select_word()
    e1 = e1.strip('\n')
    shuffWord = shufl(e1)    
    mylabel6.config(text=shuffWord)
    mylabel9.config(text=e1)   


########################## MAIN ###########################

  
#while playNum <= 2:
def startGUI():
    global w
    global w1
    global w2
    global a
    global c
    global m
    global value
    global yes_frame
    global no_frame
    global guessBoxYes
    global guessBoxNo
    global incorrectLenY
    global incorrectLenN
    global resultLabelY
    global resultLabelN
    global scoreLabelY
    global scoreLabelN
    global winnerLabelY
    global winnerLabelN
    global guessButtonY
    global guessButtonN
    global nextPlayerY
    global nextPlayerN
    global mylabel8
    global mylabel9
    global mylabel6
    global mylabel7
    global text1

    w = Tk()
    w.title("JUMBLED WORDS")
    w.geometry("800x300+1+1")
    w.configure(background='black')
    w1 = Tk()
    w1.title("GAME BEGINS!!")
    w1.configure(background='black')
    w1.geometry("800x300+1+1")
    w2 = Tk()
    w2.title("PLAY MODE")
    w2.configure(background='black')
    w2.geometry("800x300+1+1")
    a=StringVar()
    c=IntVar()
    m=IntVar()
    value=IntVar()
    c.set("1")

    myLabel1 = Label(w,text='JUMBLED WORDS World Welcomes you!!',fg = 'red',bg = 'pink',font=30)
    myLabel1.grid(row=0,column=1)
    myLabel2 = Label(w,text='Enter your details before starting game:',fg='blue')
    myLabel2.grid(row=3,column=0)
    myLabel3 = Label(w,text = 'Name of the player:',font='20')
    myLabel3.grid(row=5,column=0,sticky='w')
    text=Entry(w,textvariable=a).grid(row=5,column=1)
    myButtton=Button(w,text="Enter",command=enter,fg="black").grid(row=7,column=1)
    myLabel4 = Label(w1,text = "Do you want to provide length of word").grid(row=4,column=1)

    radiobutton1 = Radiobutton(w1,text = 'Yes',variable=c,value=1,command=yes_1)
    radiobutton1.grid(row=4,column=3)
    radiobutton2 = Radiobutton(w1,text ='No',variable=c,value=2,command=no_2)
    radiobutton2.grid(row=4,column=5)
    yes_frame=Frame(w2,bg='black')
    no_frame=Frame(w2,bg='black')    

    letterlabel=Label(yes_frame,text='Enter number of letters from 3 to 9:').grid(row=1,column=3)
    text1=Entry(yes_frame,text=m)
    text1.grid(row=1,column=6)
    enter1button = Button(yes_frame,text="enter",command=sword).grid(row=3,column=5)  
     
    guessBoxYes = Entry(yes_frame)
    guessBoxYes.grid(row=10, column=5)

    guessBoxNo = Entry(no_frame)
    guessBoxNo.grid(row=10, column=5)

    incorrectLenY = Label(yes_frame)
    incorrectLenY.grid(row = 13, column = 5)

    incorrectLenN = Label(no_frame)
    incorrectLenN.grid(row = 13, column = 5)

    resultLabelY = Label(yes_frame)
    resultLabelY.grid(row = 15, column = 5)

    resultLabelN = Label(no_frame)
    resultLabelN.grid(row = 15, column = 5)

    scoreLabelY = Label(yes_frame)
    scoreLabelY.grid(row = 17, column = 5)

    scoreLabelN = Label(no_frame)
    scoreLabelN.grid(row = 17, column = 5)

    winnerLabelY = Label(yes_frame)
    winnerLabelY.grid(row = 18, column = 5)

    winnerLabelN = Label(no_frame)
    winnerLabelN.grid(row = 18, column = 5)

    guessButtonY = Button(yes_frame,text="enter", command = partial(playGame, "yes", playNum) )
    guessButtonY.grid(row = 12, column = 5)

    guessButtonN = Button(no_frame,text="enter", command = partial(playGame, "no", playNum) )
    guessButtonN.grid(row = 12, column = 5)

    # changeButtonY = Button(yes_frame, text = "Change response", command = lambda: buttonWait.set("somestring"))
    # changeButtonY.grid(row = 75, column = 10)

    # changeButtonN = Button(no_frame, text = "Change response", command = lambda: buttonWait.set("somestring"))
    # changeButtonN.grid(row = 75, column = 10)

    nextPlayerY = Button(yes_frame, text="Player 2's turn", command = refresh)
    nextPlayerY.grid(row = 20, column=5)

    nextPlayerN = Button(no_frame, text="Player 2's turn", command = refresh)
    nextPlayerN.grid(row = 20, column=5)


    mylabel8=Label(yes_frame,text='')
    mylabel8.grid(row=5,column=5)

    mylabel9=Label(no_frame,text='')
    mylabel9.grid(row=5,column=5)

    mylabel7=Label(yes_frame,text='')
    mylabel7.grid(row=6,column=5)

    mylabel6=Label(no_frame,text='')
    mylabel6.grid(row=6,column=5)  

    col_count, row_count = w.grid_size()

    for col in range(col_count):
      w.grid_columnconfigure(col, minsize=20)

    for row in range(row_count):
      w.grid_rowconfigure(row, minsize=20)

    col_count, row_count = w1.grid_size()
    for col in range(col_count):
      w1.grid_columnconfigure(col, minsize=20)

    for row in range(row_count):
      w1.grid_rowconfigure(row, minsize=20)

    col_count, row_count = w2.grid_size()
    for col in range(col_count):
      w2.grid_columnconfigure(col, minsize=20)

    for row in range(row_count):
      w2.grid_rowconfigure(row, minsize=20)

    w.mainloop()
    w1.mainloop()
    w2.mainloop()

if __name__ == "__main__":
    def refresh():
        global playNum
        global trial
        global start
        playNum = 2
        trial = 0
        w.destroy()
        w1.destroy()
        w2.destroy()
        start = timeit.default_timer() 
        startGUI()

    start=timeit.default_timer()    
    startGUI()
