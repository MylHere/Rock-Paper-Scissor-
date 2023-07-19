from tkinter import *
from PIL import Image,ImageTk
from random import randint

 # main window
root =  Tk()
root.title("ROCK SCISSOR PAPER")
root.configure(background="#BB9FAF")

#picture
rock_image = ImageTk.PhotoImage(Image.open("rock_user.jpg"))
paper_image = ImageTk.PhotoImage(Image.open("paper_user.jpg")) 
scissor_image = ImageTk.PhotoImage(Image.open("scissor_user.jpg")) 
rock_image_comp = ImageTk.PhotoImage(Image.open("rock.jpg"))
paper_image_comp = ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor_image_comp = ImageTk.PhotoImage(Image.open("scissor.jpg"))

#insert picture
comp_label = Label(root,image=scissor_image,bg="#AFBF34")
user_label = Label(root,image=scissor_image_comp)
comp_label.grid(row=1,column=4)
user_label.grid(row=1,column=0)


#scores
playerScore=Label(root,text=0,font=50,bg="#EEEEEE",fg="white")
computerScore=Label(root,text=0,font=50,bg="#9b59b6",fg="white")
computerScore.grid(row=1,column=3)
playerScore.grid(row=1,column=1)

#indicators
user_indicator = Label(root,font=30,text="USER",bg="#9b59b6",fg="black")
comp_indicator= Label(root,font=30,text="COMPUTER",
                      bg="#9b59b6",fg="black")
user_indicator.grid(row=0,column=1)
comp_indicator.grid(row=0,column=3)

#messages
msg = Label(root, font=50,bg= "#9c59b6", fg="white",text="you loose")
msg.grid(row=3, column=2)

#update message
def updateMessage(x):
    msg['text'] = x

    #update computer score
def updateComputerScore():
        score=int(computerScore["text"])
        score += 1
        computerScore["text"] = str(score)

#update user score

def updateUserScore():
        score=int(playerScore["text"])
        score += 1
        playerScore["text"] = str(score)

#check winner
def checkWin(computer,player):
    if computer == player:
        updateMessage("Its a tie!")
    elif computer == "rock":
        if player == "paper":
            updateMessage("you loose")
            updateComputerScore()
        else:
             updateMessage("you win")
             updateUserScore
    elif computer == "paper":
        if player == "scissor":
            updateMessage("you loose")
            updateComputerScore()
        else:
            updateMessage("you win")
            updateUserScore()
    elif computer == "scissor":
        if player == "rock":
            updateMessage("you loose")
            updateComputerScore()
        else:
            updateMessage("you win")
            updateComputerScore()
    
    else:
        pass
        

#update choices

choices = ["rock","paper","scissor"]


checkWin(computerScore,playerScore)
def updatechoice(x):



   #for user
  compChoice = choices[randint(0,2)]
  if x == "rock":
      user_label.configure(image=rock_image_comp)
  elif x == "paper":
      user_label.configure(image=paper_image_comp)
  else :
      user_label.configure(image=scissor_image_comp)


    #for computer
  if compChoice=="rock":
       comp_label.configure(image=rock_image)
  elif compChoice=="paper":
        comp_label.configure(image=paper_image)
  else:
        comp_label.configure(image=scissor_image)

  checkWin(x,compChoice)
# buttons
paper = Button(root,width=10,height=2, text="PAPER",
              bg="#FFFFFF",fg="black",command=lambda:updatechoice("paper")).grid(row=2,column=1)
rock = Button(root,width=10,height=2, text="ROCK",
              bg="#FAD02E",fg="black",command=lambda:updatechoice("rock")).grid(row=2,column=2)
scissor= Button(root,width=10,height=2, text="SCISSOR",
             bg="#0ABDE3",fg="black",command=lambda:updatechoice("scissor")).grid(row=2,column=3)

root.mainloop()