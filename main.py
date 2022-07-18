
from tkinter import *
import tkinter.messagebox as tmsg
import tkinter

# Creation of window GUI
root=Tk()
root.minsize(300,300)
root.maxsize(300,300)
root.title("Tic Tac Toe")

# -------------------------- Design of game ----------------------
btnList=[]
btnRow=[]

# --------------------------- FUNCTION ---------------------------

x=0
player1=[]
player2=[]
setsVal=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

def pressedBtn(v1,v2,number):
    global x
    p1_win=False
    p2_win=False
    y=int()
    if x%2==0:
        y=1
    else:
        y=2
    
    
    for i in range(1,10):
        if i==number:
            if y==1:
                player1.append(number)
                btnList[v1][v2].config(bg="blue")
                x=x+1
                break
            else:
                player2.append(number)
                btnList[v1][v2].config(bg="green")
                x=x+1
                break
    
    print(setsVal[0])
    print(player1)
    for k in setsVal:
        # for k in item:
        p1_win=all(elem in player1 for elem in k)
        p2_win=all(elem in player2 for elem in k)

        if(p1_win==True):
            tmsg.showinfo("P1 WIN","Congrats")
            print("player 1 win")
            break
        
        elif(p2_win==True):
            tmsg.showinfo("P2 WIN","Congrats")
            print("player 2 win")
            break

    

    
    
                



for i in range(3):
    for j in range(3):
        value="b"+str(i)+str(j)
        
        value=Button(root,height=6,width=13,bg="#202020")
        value.grid(row=i,column=j)
        btnRow.append(value)
    btnList.append(btnRow)
    # print(btnRow)
    btnRow=[]
    # print(btnList)

btnList[0][0].config(command=lambda: pressedBtn(0,0,1))
btnList[0][1].config(command=lambda: pressedBtn(0,1,2))
btnList[0][2].config(command=lambda: pressedBtn(0,2,3))

btnList[1][0].config(command=lambda: pressedBtn(1,0,4))
btnList[1][1].config(command=lambda: pressedBtn(1,1,5))
btnList[1][2].config(command=lambda: pressedBtn(1,2,6))

btnList[2][0].config(command=lambda: pressedBtn(2,0,7))
btnList[2][1].config(command=lambda: pressedBtn(2,1,8))
btnList[2][2].config(command=lambda: pressedBtn(2,2,9))














root.mainloop()