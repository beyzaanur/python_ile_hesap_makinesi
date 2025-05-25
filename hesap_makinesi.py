from tkinter import *

pencere = Tk()
pencere.title("-Hesap Makinesi-")
pencere.geometry("270x250+300+100")
pencere.resizable(FALSE,FALSE)

depo = ""

def hesapla(tus):
    global depo
    if tus in "1234567980":
        ekran.insert(END,tus)
        depo = depo + tus

    if tus in "/*-+":
        ekran.insert(END,tus)
        depo = depo + tus
    if tus == "=":
        ekran.delete(0,END)
        hesap = eval(depo , {"__builtins__":NONE} , {})
        depo = str(hesap)
        ekran.insert(END,depo)

    if tus == "C":
        ekran.delete(0,END)
        depo = ""



ekran = Entry(width=40 , justify=RIGHT)
ekran.grid(row = 0, column = 0 , columnspan = 3 , ipady = 8)

liste = ["1","2","3","4","5","6","7","8","9","0","=","+","-","/","*","C"]

sira = 1
sutun = 0

for i in liste:
    komut = lambda x = i : hesapla(x)
    Button(text = i , font = "verdana 8 bold" , bg = "#CE8CE3" ,fg = "black", width=10 , height= 2 ,relief=RAISED , command = komut).grid(row = sira , column = sutun)
    sutun += 1
    if sutun>2:
        sutun = 0
        sira += 1

mainloop()