from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import messagebox
#All Sqlite database modules
import sqlite3
import IPhoneDatabase
import SamsungDatabase
import VivoDatabase
import OppoDatabase
import LenovoDatabase
import HuaweiDatabase
import NokiaDatabase
import HonorDatabase
import RealmeDatabase
import OnePlusDatabase
import MainDatabase

class Main:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("JC's Phone and Accessories")
        self.parent.geometry('1100x500+110+80')
        self.parent.config(bg = 'lightblue')
        
        #frame for (insuffecient and thank you when done transaction
        self.frame1 = LabelFrame(self.parent, height=486, bd=3, bg="lightblue", width=120)
        self.frame1.place(x=980,y=8)

        #frame of transaction
        self.frame2 = LabelFrame(self.parent,width=380, height=420, bg="lightblue", text='Transaction', bd = 10, font='Times 12 bold')
        self.frame2.place(x=600, y=1)

        #frame of message
        self.frame3 = LabelFrame(self.parent, bg="lightblue", height=70, width=772, bd=10)
        self.frame3.place(x=210, y=425)

        #frame of phonelist
        self.frame4 = LabelFrame(self.parent,width=380, height=420, bg="lightblue", text='SELECT UNIT', bd = 10, font='Times 12 bold')
        self.frame4.place(relx=0.19, y=1)
                
        #frame phone buttons
        self.frame5 = LabelFrame(self.parent, height=500, bd=3, bg="white", width=200)
        self.frame5.place(x=1,y=1)
        #function of exit
        def Exit():
            Exit = tkinter.messagebox.askyesno("JC's Phone and Accessories", "Do you want to exit?")
            if Exit > 0:
                window.destroy()
                return
        #bill exchange function
        def bill():
            try:
                global cash
                global bill
                global change
                
                cash =int(self.txtCash.get())
                bill = int(self.TotalEntry.get())
                change = (int(cash - bill))
                if change >= 0:
                    for widget in self.frame3.winfo_children():
                        widget.destroy()
                    self.txtChange = Entry(self.frame2, width=15, font='Arial 10', bd=3, justify='right')
                    self.txtChange.insert(0, change)
                    self.txtChange.place(x = 240, y = 330)
                    lb_bill = Label(self.frame3, text = "THANK YOU!", font = "times 25 bold", bg='lightblue')
                    lb_bill.place(x=260, y= 1)
                else:
                    for widget in self.frame3.winfo_children():
                        widget.destroy()
                    lb_bill = Label(self.frame3, text = "INSUFFICIENT AMOUNT!", font = "times 25 bold", bg='lightblue') 
                    lb_bill.place(x=170, y= 1)
            except ValueError:
                error = tkinter.messagebox.showerror("JC's Phone and Accessories", "Invalid!\nShow total/Enter cash value.")
        #Phone Functions. Where all the module of brands called
        def IPhoneListView():
            for widget in self.PhoneList.winfo_children():
                widget.destroy()
            self.PhoneList.delete(0, END)
            for rows in IPhoneDatabase.viewData():
                self.PhoneList.insert(END, rows)
                
        def SamsungListView():
            for widget in self.PhoneList.winfo_children():
                widget.destroy()
            self.PhoneList.delete(0, END)
            for rows in SamsungDatabase.viewData():
                self.PhoneList.insert(END, rows)
                
        def VivoListView():
            for widget in self.PhoneList.winfo_children():
                widget.destroy()
            self.PhoneList.delete(0, END)
            for rows in VivoDatabase.viewData():
                self.PhoneList.insert(END, rows)
                
        def OppoListView():
            for widget in self.PhoneList.winfo_children():
                widget.destroy()
            self.PhoneList.delete(0, END)
            for rows in OppoDatabase.viewData():
                self.PhoneList.insert(END, rows)
                
        def LenovoListView():
            for widget in self.PhoneList.winfo_children():
                widget.destroy()
            self.PhoneList.delete(0, END)
            for rows in LenovoDatabase.viewData():
                self.PhoneList.insert(END, rows)
        
        def HuaweiListView():
            for widget in self.PhoneList.winfo_children():
                widget.destroy()
            self.PhoneList.delete(0, END)
            for rows in HuaweiDatabase.viewData():
                self.PhoneList.insert(END, rows)
        
        def NokiaListView():
            for widget in self.PhoneList.winfo_children():
                widget.destroy()
            self.PhoneList.delete(0, END)
            for rows in NokiaDatabase.viewData():
                self.PhoneList.insert(END, rows)
        
        def HonorListView():
            for widget in self.PhoneList.winfo_children():
                widget.destroy()
            self.PhoneList.delete(0, END)
            for rows in HonorDatabase.viewData():
                self.PhoneList.insert(END, rows)
                
        def RealmeListView():
            for widget in self.PhoneList.winfo_children():
                widget.destroy()
            self.PhoneList.delete(0, END)
            for rows in RealmeDatabase.viewData():
                self.PhoneList.insert(END, rows)
        
        def OnePlusListView():
            for widget in self.PhoneList.winfo_children():
                widget.destroy()
            self.PhoneList.delete(0, END)
            for rows in OnePlusDatabase.viewData():
                self.PhoneList.insert(END, rows)
        
        def getPhone(event):
            global gp
            getPhone = self.PhoneList.curselection()[0]
            gp = self.PhoneList.get(getPhone)
            
            self.UnitEntry.delete(0,END)
            self.UnitEntry.insert(END, gp[0])
            self.PriceEntry.delete(0,END)
            self.PriceEntry.insert(END, gp[1])
            
        #to clear all the widgets in the system
        def clear():
            for widget in self.frame3.winfo_children():
                widget.destroy()
            self.PhoneList.delete(0,END)
            self.UnitEntry.delete(0,END)
            self.PriceEntry.delete(0,END)
            self.TotalEntry.delete(0,END)
            self.list1.delete(0, END)
            self.TotalEntry.delete(0, END)
            self.txtCash.delete(0,END)
            self.txtChange.delete(0,END)
        #thesr two are the variables for the entry
        UNIT = StringVar()
        PRICE = IntVar()
        #the main database
        def add(): 
            if(len(UNIT.get())!=0):
                MainDatabase.add(UNIT.get(), PRICE.get())
                self.list1.delete(0, END)
                self.list1.insert(END,(UNIT.get(), PRICE.get()))
            self.UnitEntry.delete(0,END)
            self.PriceEntry.delete(0,END)
            
        def view():
            self.list1.delete(0, END)
            for rows in MainDatabase.view():
                self.list1.insert(END, rows)
                
        def delete():
            self.PhoneList.delete(0,END)
            self.list1.delete(0, END)
            self.TotalEntry.delete(0, END)
            self.txtCash.delete(0,END)
            self.txtChange.delete(0,END)
            MainDatabase.delete()
            
        def total():
            try:
                con = sqlite3.connect('Sold.db')
                cur = con.cursor()
                cur.execute("SELECT SUM(PRICE) FROM Sold")
                self.TotalEntry.delete(0, END)
                self.TotalEntry.insert(END, cur.fetchone()[0])
                con.close()
            except TclError:
                invalid = tkinter.messagebox.showerror("JC's Phone and Accessories", "No prices to total!")

        
        #Entry
        #Unit
        self.UnitLabel = Label(self.frame2, text='UNIT:', font='Arial 12 bold', bg='lightblue')
        self.UnitLabel.place(x=2, y=1)
        self.UnitEntry = Entry(self.frame2, width=30, font='Arial 10', bd=3, textvariable = UNIT)
        self.UnitEntry.place(x=2, y=25)
        #price
        self.PriceLabel = Label(self.frame2, text='PRICE:', font='Arial 12 bold', bg='lightblue')
        self.PriceLabel.place(x=240, y=1)
        self.PriceEntry = Entry(self.frame2, width=15, font='Arial 10', bd=3, textvariable = PRICE)
        self.PriceEntry.place(x=240, y=25)
        #total
        self.TotalLabel = Label(self.frame2, text='Total', font='Arial 12 bold', bg='lightblue')
        self.TotalLabel.place(x=190, y=270)
        self.TotalEntry = Entry(self.frame2, width=15, font='Arial 10', bd=3, justify='right')
        self.TotalEntry.place(x=240, y=270)
        #cash
        self.lblCash = Label(self.frame2, text='Cash', font='Arial 12 bold', bg='lightblue')
        self.lblCash.place(x=190, y=300)
        self.txtCash = Entry(self.frame2, width=15, font='Arial 10', bd=3, justify='right')
        self.txtCash.place(x = 240, y = 300)
        #change
        self.lbChange = Label(self.frame2, text = "Change", font='Arial 12 bold', bg='lightblue')
        self.lbChange.place(x=170, y = 330)
        self.txtChange = Entry(self.frame2, width=15, font='Arial 10', bd=3, justify='right')
        self.txtChange.place(x = 240, y = 330)
        
        #Cellphone Brand buttons
        self.oneplusButton = Button(self.frame5,font = ('helvetica',10, 'bold'), text="ONE PLUS", height=2, width=23, fg="black", command= OnePlusListView)
        self.oneplusButton.place(x=1, y=1)

        self.realmeButton = Button(self.frame5,font ='Arial 10  bold', text="REALME", height=2, width=23, fg="black", command= RealmeListView)
        self.realmeButton.place(x=1, y=50)

        self.honorButton = Button(self.frame5,font ='Arial 10  bold', text="HONOR", height=2, width=23, fg="black", command= HonorListView)
        self.honorButton.place(x=1, y=100)

        self.nokiaButton = Button(self.frame5,font ='Arial 10  bold', text="NOKIA", height=2, width=23, fg="black", command= NokiaListView)
        self.nokiaButton.place(x=1, y=150)

        self.huaweiButton = Button(self.frame5,font ='Arial 10  bold', text="HUAWEI", height=2, width=23, fg="black", command= HuaweiListView)
        self.huaweiButton.place(x=1, y=200)

        self.lenovoButton = Button(self.frame5,font ='Arial 10  bold', text="LENOVO", height=2, width=23, fg="black", command= LenovoListView)
        self.lenovoButton.place(x=1, y=250)

        self.oppoButton = Button(self.frame5,font ='Arial 10  bold', text="OPPO", height=2, width=23, fg="black", command= OppoListView)
        self.oppoButton.place(x=1, y=300)

        self.vivoButton = Button(self.frame5,font ='Arial 10  bold', text="VIVO", height=2, width=23, fg="black", command= VivoListView)
        self.vivoButton.place(x=1, y=350)

        self.samsungButton = Button(self.frame5,font ='Arial 10  bold', text="SAMSUNG", height=2, width=23, fg="black", command = SamsungListView)
        self.samsungButton.place(x=1, y=400)

        self.appleButton = Button(self.frame5,font ='Arial 10  bold', text="APPLE", height=2, width=23, fg="black", command = IPhoneListView)
        self.appleButton.place(x=1, y=450)

        #currency window button
        self.ccButton = Button(self.frame1,font ='Arial 10  bold', text="CURRENCY\nCONVERTER", height=3, width=13, fg="black")
        self.ccButton.place(x=1, y=1)
        #clear button to call the clear function
        self.clearButton = Button(self.frame1,font ='Arial 10  bold', text="CLEAR\nALL", height=3, width=13, fg="black", command = clear)
        self.clearButton.place(x=1, y=65)
        #exit button
        self.ExitButton = Button(self.frame1,font ='Arial 10  bold', text="EXIT", height=3, width=13, fg="black", command = Exit)
        self.ExitButton.place(x=1, y=130)
        
        #para sa transaction
        self.okButton = ttk.Button(self.frame2, text="OK", command = add)
        self.okButton.place(x=2, y=270)
        
        self.deleteButton = ttk.Button(self.frame2, text="NEW TRANS", command = delete)
        self.deleteButton.place(x=2, y=300)
        
        self.viewButton = ttk.Button(self.frame2, text="VIEW", command = view)
        self.viewButton.place(x=2, y=330)
        
        self.totalButton = ttk.Button(self.frame2, text="TOTAL", command = total)
        self.totalButton.place(x=2, y=360)
        
        self.changeButton = ttk.Button(self.frame2, text="DONE", command = bill)
        self.changeButton.place(x=260, y=360)
        
        #two main list box, one for display and one for transaction
        self.PhoneList = Listbox(self.frame4, bg='lightblue', width=29, height=14, font ='times 18 bold')
        self.PhoneList.bind('<<ListboxSelect>>', getPhone)
        self.PhoneList.place(x=2, y=2)
        
        self.list1 = Listbox(self.frame2, width=44, height=10, font ='times 12 bold')
        self.list1.place(x=2, y=60)
        
window  = Tk()
app = Main(window)
window.mainloop()