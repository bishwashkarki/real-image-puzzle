"""
in this file iam creating a program that has 2x2 frames that can be moved around a empty frame

"""

#imoprt modules
import tkinter



#tkinter settings
win=tkinter.Tk()
win.title("IMAGE PUZZLE")
win.resizable(True, True)
win.geometry("750x750")


def frame1_exchange():
    
    X, Y = button9.grid_info().get("row"), button9.grid_info().get("column")
    X1, Y1 = button1.grid_info().get("row"), button1.grid_info().get("column")
    if X==X1 or Y==Y1:
        button1.grid(row=X,column=Y)
        button9.grid(row=X1,column=Y1)

def frame2_exchange():
    #how to check postion
    X, Y = button9.grid_info().get("row"), button9.grid_info().get("column")
    X1, Y1 = button2.grid_info().get("row"), button2.grid_info().get("column")
    if X==X1 or Y==Y1:
        button2.grid(row=X,column=Y)
        button9.grid(row=X1,column=Y1)

def frame3_exchange():
    #how to check postion
    X, Y = button9.grid_info().get("row"), button9.grid_info().get("column")
    X1, Y1 = button3.grid_info().get("row"), button3.grid_info().get("column")
    if X==X1 or Y==Y1:
        button3.grid(row=X,column=Y)
        button9.grid(row=X1,column=Y1)

def frame4_exchange():
    #how to check postion
    X, Y = button9.grid_info().get("row"), button9.grid_info().get("column")
    X1, Y1 = button4.grid_info().get("row"), button4.grid_info().get("column")
    if X==X1 or Y==Y1:
        button4.grid(row=X,column=Y)
        button9.grid(row=X1,column=Y1)

def frame5_exchange():
    #how to check postion
    X, Y = button9.grid_info().get("row"), button9.grid_info().get("column")
    X1, Y1 = button5.grid_info().get("row"), button5.grid_info().get("column")
    if X==X1 or Y==Y1:
        button5.grid(row=X,column=Y)
        button9.grid(row=X1,column=Y1)

def frame6_exchange():
    #how to check postion
    X, Y = button9.grid_info().get("row"), button9.grid_info().get("column")
    X1, Y1 = button6.grid_info().get("row"), button6.grid_info().get("column")
    if X==X1 or Y==Y1:
        button6.grid(row=X,column=Y)
        button9.grid(row=X1,column=Y1)

def frame7_exchange():
    #how to check postion
    X, Y = button9.grid_info().get("row"), button9.grid_info().get("column")
    X1, Y1 = button7.grid_info().get("row"), button7.grid_info().get("column")
    if X==X1 or Y==Y1:
        button7.grid(row=X,column=Y)
        button9.grid(row=X1,column=Y1)

def frame8_exchange():
    #how to check postion
    X, Y = button9.grid_info().get("row"), button9.grid_info().get("column")
    X1, Y1 = button8.grid_info().get("row"), button8.grid_info().get("column")
    if X==X1 or Y==Y1:
        button8.grid(row=X,column=Y)
        button9.grid(row=X1,column=Y1)
#image_size= 500x500
"""
background=tkinter.PhotoImage(file="main_image.jpg")
"""
#setting images
image1=tkinter.PhotoImage(file="images/GIF/main_image_top_left.gif")
image2=tkinter.PhotoImage(file="images/GIF/main_image_top_right.gif")
image3=tkinter.PhotoImage(file="images/GIF/main_image_bottm_left.gif")
image4=tkinter.PhotoImage(file="images/GIF/main_image_bottm_left.gif")
image5=tkinter.PhotoImage(file="images/GIF/main_image_bottm_left.gif")
image6=tkinter.PhotoImage(file="images/GIF/main_image_bottm_left.gif")
image7=tkinter.PhotoImage(file="images/GIF/main_image_bottm_left.gif")
image8=tkinter.PhotoImage(file="images/GIF/main_image_bottm_left.gif")
image9=tkinter.PhotoImage(file="images/GIF/white250.gif")


#running=True
#while running:
button1= tkinter.Button(win,text="button1", image=image1, command=frame1_exchange)
button1.grid(row=0,column=0)
#button2
button2= tkinter.Button(win,text="button2", image=image2, command=frame2_exchange)
button2.grid(row=1,column=0)
#button3
button3= tkinter.Button(win,text="button3", image=image3, command=frame3_exchange)
button3.grid(row=2,column=0)
#button9
button4= tkinter.Button(win,text="button4", image=image4, command=frame4_exchange)
button4.grid(row=0,column=1)
#button5
button5= tkinter.Button(win,text="button5", image=image5, command=frame5_exchange)
button5.grid(row=1,column=1)
#button6
button6= tkinter.Button(win,text="button6", image=image6, command=frame6_exchange)
button6.grid(row=2,column=1)
#button7
button7= tkinter.Button(win,text="button7", image=image7, command=frame7_exchange)
button7.grid(row=0,column=2)
#button8
button8= tkinter.Button(win,text="button8", image=image8, command=frame8_exchange)
button8.grid(row=1,column=2)
#button9
button9= tkinter.Button(win, image=image9)
button9.grid(row=2,column=2)






win.mainloop()
