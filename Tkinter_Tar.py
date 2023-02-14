from statistics import variance
from tkinter import *
from tkinter import ttk

k=0
def klikker(event):
    global k
    k+=1
    lbl.configure(text=k)

def klikker1(event):
    global k
    if k >0:
        k-=1
    else:
        k=0
    lbl.configure(text=k)

def ent_to_label(event):
    text=ent.get()
    lbl.configure(text=text)
    ent.delete(0,END)
def valik():
    text=var.get() #s4itqvaem infu 
    ent.insert(END,text)
def uus_aken(ind:int):
    def tab_valik(ind:int):
        uusaken.title(texts[ind])
    uusaken=Toplevel() #Tk() 
    tabs=ttk.Notebook(uusaken)
    texts=["Esimene","Teine", "Kolmas", "Neljas"] 
    tab=[]
    for i in range(len(texts)):
        tab.append("tab"+str(i)) #tab0,tab1,tab2,tab3
        tab[i]=Frame(tabs)
        tabs.add(tab[i],text=texts[i])
        tab[i].bind("<Button-1>",tab_valik(i))

    tabs.grid(row=0,column=0) 
    tabs.select(ind)

    uusaken.title(texts[ind])
    uusaken.mainloop()

aken=Tk()
aken.title("Minu esimene aken") 
aken.geometry("600x200") 
m=Menu(aken) 
aken.config(menu=m)
m1=Menu(m) 
m.add_cascade(label="Kaardid", menu=m1)
m1.add_command(label="1.Kaart", accelerator="Command+A", command=lambda:uus_aken(0))
m1.add_command(label="2.Kaart", accelerator="Command+B", command=lambda:uus_aken(1))
m1.add_command(label="3.Kaart", accelerator="Command+C", command=lambda:uus_aken(2))
m1.add_command(label="4.Kaart", accelerator="Command+D", command=lambda:uus_aken(3))

lbl=Label(aken, text="....",font="Arial 14")
btn=Button(aken,text="Vajuta siia",font="Tahoma 20",fg="#1c4226",bg="#aee8be",width=15, heigh=2,relief=RAISED) #SUNKEN, RAISED, SOLID
ent=Entry(aken,font="Tahoma 20",fg="#1c4226",bg="#f0e4c7",width=20,justify=CENTER)

var=IntVar() #stringvar()
r1=Radiobutton(aken,text="Esimene",font="Tahoma 14",width=20,variable=var, value=1,command=valik)
r2=Radiobutton(aken,text="Teine",font="Tahoma 14",width=20,variable=var, value=2,command=valik)

btn.bind("<Button-1>",klikker) #zapusk funkcii, 1- click left mouse, 3- right
btn.bind("<Button-3>",klikker1)
ent.bind("<Return>",ent_to_label) #enter click
btn.pack()

ent.pack()
lbl.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
aken.mainloop()

