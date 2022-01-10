
import tkinter
from PIL import Image
import os
import random

def imgcrop(input, xPieces, yPieces):
    filename, file_extension = os.path.splitext(input)
    im = Image.open(input)
    imgwidth, imgheight = im.size
    height = imgheight // yPieces
    width = imgwidth // xPieces
    for i in range(0, yPieces):
        for j in range(0, xPieces):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            a = im.crop(box)
            try:
                a.save(filename + "-" + str(i) + "-" + str(j) + file_extension)
            except:
                pass

imgcrop('images/main_image.gif', 3, 3)

#tkinter settings
win=tkinter.Tk()
win.title("IMAGE PUZZLE")
win.resizable(False, False)


# Designate Height and Width of our app
app_width = 500
app_height = 550

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height /2 ) - (app_height / 2)

win.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
                                 

def randomize_button():
    grid_list = [(0,0), (0,1), (0,2), (1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    button_list = [button1,button2,button3,button4,button5,button6,button7,button8,button9]

    for i in range(len(button_list)):
        random_grid = random.choice(grid_list)
        x, y = random_grid
        random_button_choice = random.choice(button_list)
        random_button_choice.grid(row=x, column=y)
        button_list.remove(random_button_choice)
        grid_list.remove(random_grid)

def frame_exchange(curr_button):
    global button1
    

    X, Y = button9.grid_info().get("row"), button9.grid_info().get("column")
    X1, Y1 = curr_button.grid_info().get("row"), curr_button.grid_info().get("column")
    if X1 == X:
        if Y1 + 1 == Y or Y1 - 1 == Y or Y1==Y:
            curr_button.grid(row=X,column=Y)
            button9.grid(row=X1,column=Y1)
    else:
        pass
    if Y1 == Y:
        if X1 + 1 == X or X1 - 1 == X or X1==X:
            curr_button.grid(row=X,column=Y)
            button9.grid(row=X1,column=Y1)
    else:
        pass

    if (button1.grid_info().get("row")==0 and  button1.grid_info().get("column")==0)==True:
        if (button2.grid_info().get("row")==1 and  button2.grid_info().get("column")==0)==True:
            if (button3.grid_info().get("row")==2 and  button3.grid_info().get("column")==0)==True:
                if (button4.grid_info().get("row")==0 and  button4.grid_info().get("column")==1)==True:
                    if (button5.grid_info().get("row")==1 and  button5.grid_info().get("column")==1)==True:
                        if (button6.grid_info().get("row")==2 and  button6.grid_info().get("column")==1)==True:
                            if (button7.grid_info().get("row")==0 and  button7.grid_info().get("column")==2)==True:
                                if (button8.grid_info().get("row")==1 and  button8.grid_info().get("column")==2)==True:
                                    print ("YOU WON")

#setting images
image1=tkinter.PhotoImage(file="images/main_image-0-0.gif")
image2=tkinter.PhotoImage(file="images/main_image-1-0.gif")
image3=tkinter.PhotoImage(file="images/main_image-2-0.gif")
image4=tkinter.PhotoImage(file="images/main_image-0-1.gif")
image5=tkinter.PhotoImage(file="images/main_image-1-1.gif")
image6=tkinter.PhotoImage(file="images/main_image-2-1.gif")
image7=tkinter.PhotoImage(file="images/main_image-0-2.gif")
image8=tkinter.PhotoImage(file="images/main_image-1-2.gif")
image9=tkinter.PhotoImage(file="images/white166.gif")


#running=True
#while running:
button1= tkinter.Button(win,text="button1", image=image1,  command= lambda: frame_exchange(button1))
button1.grid(row=0,column=0)
#button2
button2= tkinter.Button(win,text="button2", image=image2,  command= lambda: frame_exchange(button2))
button2.grid(row=1,column=0)
#button3
button3= tkinter.Button(win,text="button3", image=image3,  command= lambda: frame_exchange(button3))
button3.grid(row=2,column=0)
#button9
button4= tkinter.Button(win,text="button4", image=image4, command= lambda: frame_exchange(button4))
button4.grid(row=0,column=1)
#button5
button5= tkinter.Button(win,text="button5", image=image5, command= lambda: frame_exchange(button5))
button5.grid(row=1,column=1)
#button6
button6= tkinter.Button(win,text="button6", image=image6, command= lambda: frame_exchange(button6))
button6.grid(row=2,column=1)
#button7
button7= tkinter.Button(win,text="button7", image=image7, command= lambda: frame_exchange(button7))
button7.grid(row=0,column=2)
#button8
button8= tkinter.Button(win,text="button8", image=image8, command= lambda: frame_exchange(button8))
button8.grid(row=1,column=2)
#button9
button9= tkinter.Button(win, image=image9)
button9.grid(row=2,column=2)

random_button=tkinter.Button(win, text="ramdomize",background="lightblue", command=randomize_button)
random_button.grid(row=3,column=1)





win.mainloop()
