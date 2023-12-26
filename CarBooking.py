from tkinter import *
from tkinter import ttk
import random
import time
from tkinter import messagebox as ms
import sqlite3
#import mysql.connector as mysql
item4=0

with sqlite3.connect('Users.db') as db:
    c=db.cursor #abstraction for database

c.execute('CREATE TABLE IF NOT EXISTS user(username TEXT NOT NULL,password TEXT NOT NULL)')
db.commit() #updating db
db.close()

class user:
    def __init__(self,master):
        self.master=master
        self.username=StringVar()
        self.password=StringVar()
        self.n_username=StringVar()
        self.n_password=StringVar()
        self.widgets()

    def login(self):
        with sqlite3.connect('Users.db') as db:
            c=db.cursor()
        find_user=('SELECT * FROM user WHERE username=? and password=?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result=c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text']="Welcome"+self.username.get()
            self.head.configure(fg="White",bg="black",font=("MV Boli",30,"bold"))
            self.head.pack(fill=X)
            application=travel(root)
        else:
            ms.showerror("Error","Invalid Username or Password,Not in Database")

    def new_user(self):
        with sqlite3.connect('Users.db') as db:
            c=db.cursor()
        find_user=('SELECT * FROM user WHERE username=? and password=?')
        c.execute(find_user,[(self.username.get())])
        if c.fetchall():
            ms.showwarning("Warning!","Username already exists.")
        else:
            ms.showinfo("Account created")
            self.log()
        insert='INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

    def log(self):
        self.username.set("")
        self.password.set("")
        self.crf.pack_forget()
        self.head['text']='Login'
        self.logf.pack()
    
    def cr(self):
        self.n_username.set("")
        self.n_password.set("")
        self.logf.pack_forget()
        self.head['text']='Create Account'
        self.crf.pack()

    def widgets(self):
        self.head=Label(self.master,text='Login Panel',font=("Arial 20"),pady=10)
        self.head.pack()
        self.logf=Frame(self.master,padx=10,pady=10)
        Label(self.logf,text='Username',font=("20"),pady=5,padx=5).grid(sticky=W)
        Entry(self.logf,textvariable=self.username,bd=5,font=("15")).grid(row=0,column=1)
        Label(self.logf,text='Password',font=("20"),pady=5,padx=5).grid(sticky=W)
        Entry(self.logf,textvariable=self.password,bd=5,font=("15")).grid(row=1,column=1)
        Button(self.logf,text='Login',bd=1,font=("15"),padx=5,pady=5,command=self.login,bg="green").grid()
        Button(self.logf,text='Create Account',bd=1,font=("15"),padx=5,pady=5,command=self.cr,bg="red").grid(row=2,column=1)
        self.logf.pack()

        self.crf=Frame(self.master,padx=10,pady=10)
        Label(self.crf,text='Username',font=("20"),pady=5,padx=5).grid(sticky=W)
        Entry(self.crf,textvariable=self.n_username,bd=5,font=("15")).grid(row=0,column=1)
        Label(self.crf,text='Password',font=("20"),pady=5,padx=5).grid(sticky=W)
        Entry(self.crf,textvariable=self.n_password,bd=5,font=("15")).grid(row=1,column=1)
        Button(self.crf,text='Create Account',bd=1,font=("15"),padx=5,pady=5,command=self.new_user,bg="green").grid()
        Button(self.crf,text='Go to Login',bd=1,font=("15"),padx=5,pady=5,command=self.log,bg="red").grid(row=2,column=1)
        self.crf.pack()
class travel:
    def __init__(self,root) :
        self.root=root
        self.root.title("Cab Booking system")
        self.root.geometry(geometry)
        self.root.configure(bacground='black')
        self.root.resizable(width=False,height=False)


        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))
        Receipt_Ref=StringVar()
        PaidTax=StringVar()
        SuubTotal=StringVar()
        TotalCost=StringVar()
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        journeyType=IntVar()
        carType=IntVar()

        varl1=StringVar()
        varl2=StringVar()
        varl3=StringVar()
        reset_counter=0

        Firstname=StringVar()
        SurName=StringVar()
        Address=StringVar()
        Postcode=StringVar()
        Mobile=StringVar()
        Telephone=StringVar()
        Email=StringVar()

        CabTax=StringVar()
        Km=StringVar()
        Travel_Ins=StringVar()
        Luggage=StringVar()
        Receipt=StringVar()

        Standard=StringVar()
        FordGalaxy=StringVar()
        FordMondoe=StringVar()


        CabTax.set("0")
        Km.set("0")
        Travel_Ins.set("0")
        Luggage.set("0")
        Standard.set("0")
        FordGalaxy.set("0")
        FordMondoe.set("0")

        def Cab_Tax():
            global item1
            if var1.get()==1:
                self.txtCabTax.configure(state=NORMAL)
                item1=float(50)
                CabTax.set("Rs "+str(item1))

            elif var1.get()==0:
                self.txtCabTax.configure(state=DISABLED)
                CabTax.set("0")
                item1=0


        def Kilo():
            if var2.get()==0:
                self.txtKm.configure(state=DISABLED)
                Km.set("0")
            elif var2.get()==1 and varl1.get()!="" and varl2.get!="":
                self.txtKm.configure(state=NORMAL)
                if varl1.get()=="Arcade Lane":
                    switch={"The Fort":10,"Cinema":8,"Railway Station":6,"Arcade Lane":0}
                    Km.set(switch[varl2.get()])
                elif varl1.get()=="The Fort":
                    switch={"Arcade Lane":10,"Cinema":5,"Railway Stattion":2,"The Fort":0}
                    Km.set(switch[varl2.get()])
                elif varl1.get()=="Cinema":
                    switch={"Arcade Lane":8,"The Fort":5,"Railway Station":3,"Cinema":0}
                    Km.set(switch[varl2.get()])
                elif varl1.get()=="Railway Station":
                    switch={"Arcade Lane":6,"The Fort":2,"Cinema":3,"Railway Station":0}
                    Km.set(switch[varl2.get()])
                     
        def Travelling():
            global item3
            if var3.get()==1:
                self.txtTravel_Ins.configure(state=NORMAL)
                item3=float(10)
                Travel_Ins.set("Rs "+str(item3))
            elif var3.get()==0:
                self.txtTravel_Ins.configure(state=DISABLED)
                Travel_Ins.set("0")
                item3=0

        def Reset():
            iMs=ms.askyesno("Prompt","Do You wanna Book?")
            if iMs>0:
                ms.showinfo("Prompt","Booking Successful,ThankYou")

        
        def Total_Paid():
            if varl3.get()=="1":
                item2=Km.set()
                Cost_of_fare=(item1+(float(item2)*2+item3+item4))

                Tax="Rs "+str('%.2f'%((Cost_of_fare)*0.09))
                ST="Rs "+str('%.2f'%((Cost_of_fare)))
                TT ="Rs "+ str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.9)))

            elif varl3.get()=="2":
                item2=Km.set()
                Cost_of_fare=(item1+(float(item2)*2)*1.5+item3+item4)

                Tax="Rs "+str('%.2f'%((Cost_of_fare)*0.09))
                ST="Rs "+str('%.2f'%((Cost_of_fare)))
                TT ="Rs "+ str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.9)))

            elif varl3.get()=="3":
                item2=Km.set()
                Cost_of_fare=(item1+(float(item2)*3)*2+item3+item4)

                Tax="Rs "+str('%.2f'%((Cost_of_fare)*0.09))
                ST="Rs "+str('%.2f'%((Cost_of_fare)))
                TT ="Rs "+ str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.9)))

            PaidTax.set(Tax)
            SuubTotal.set(ST)
            TotalCost(TT)


        #MAIN FRAME

        MainFrame=Frame(self.root)
        MainFrame.pack(fill=BOTH,expand=True)


        Tops=Frame(MainFrame,bd=10,bg="black",width=800,relief=RIDGE)
        Tops.pack(side=TOP,fill=BOTH)

        self.lblTitle=Label(Tops,font=('MV Boli',30,'bold'),text='\t Cab Booking System',bg="black",fg="white",bd=10,anchor='w')
        self.lblTitle.grid()


        #CUSTOMER FRAME

        CustomerDetailsFrame=LabelFrame(MainFrame,width=400,height=400,bd=20,pady=5,relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM,fill=BOTH,expand=True)

        FrameDetails=Frame(CustomerDetailsFrame,width=480,height=300,bd=10,relief=RIDGE)
        FrameDetails.pack(side=LEFT,fill=BOTH,expand=True)
        CustomerName=LabelFrame(FrameDetails,width=150,height=250,bd=10,font=('arial',12,'bold'),text='Customer Info')
        CustomerName.grid(row=0,column=0)
        TravelFrame=LabelFrame(FrameDetails,bd=10,width=300,height=50,font=('arial0',12,'bold'),text="Booking Details",relief=RIDGE)
        TravelFrame.grid(row=0,column=1)
        CostFrame=LabelFrame(FrameDetails,width=300,height=150,bd=5,relief=FLAT)
        CostFrame.grid(row=1,column=1)

         #IMAGE PART
        
        Receipt_BottomFrame=LabelFrame(CustomerDetailsFrame,bd=10,width=350,height=300,relief=SUNKEN)
        Receipt_BottomFrame.pack(side=RIGHT,fill=BOTH,expand=True)

        Receipt_BottomFrame.picture=PhotoImage(file="./thanku.png")
        Receipt_BottomFrame.label=Label(Receipt_BottomFrame,image=Receipt_BottomFrame.picture)
        Receipt_BottomFrame.label.pack()


        #CUSTOMER INFORMATION

        self.lblFirstName=Label(CustomerName,font=('arial',14,'bold'),text="First Name",bd=7)
        self.lblFirstName.grid(row=0,column=0,sticky=W)
        self.txtFirstName=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Firstname,bd=7,insertborderwidth=2,justify=RIGHT)
        self.txtFirstName.grid(row=0,column=1)

        self.lblSurName=Label(CustomerName,font=('arial',14,'bold'),text="Sur Name",bd=7)
        self.lblSurtName.grid(row=1,column=0,sticky=W)
        self.txtSurtName=Entry(CustomerName,font=('arial',14,'bold'),textvariable=SurName,bd=7,insertborderwidth=2,justify=RIGHT)
        self.txtSurName.grid(row=1,column=1)

        self.lblAddress=Label(CustomerName,font=('arial',14,'bold'),text="Address",bd=7)
        self.lblAddress.grid(row=2,column=0,sticky=W)
        self.txtAddress=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Address,bd=7,insertborderwidth=2,justify=RIGHT)
        self.txtAddress.grid(row=2,column=1)

        self.lblPostCode=Label(CustomerName,font=('arial',14,'bold'),text="Postal Code",bd=7)
        self.lblPostCode.grid(row=3,column=0,sticky=W)
        self.txtPostCode=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Postcode,bd=7,insertborderwidth=2,justify=RIGHT)
        self.txtPostCode.grid(row=3,column=1)

        self.lblMobile=Label(CustomerName,font=('arial',14,'bold'),text="Mobile",bd=7)
        self.lblMobile.grid(row=4,column=0,sticky=W)
        self.txtMobile=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Mobile,bd=7,insertborderwidth=2,justify=RIGHT)
        self.txtMobile.grid(row=4,column=1)

        self.lblEmail=Label(CustomerName,font=('arial',14,'bold'),text="Email",bd=7)
        self.lblEmail.grid(row=5,column=0,sticky=W)
        self.txtEmail=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Email,bd=7,insertborderwidth=2,justify=RIGHT)
        self.txtEmail.grid(row=2,column=1)


        #Cab info
        self.lblPickup=Label(TravelFrame,font=('arial',14,'bold'),text="Pickup",bd=7)
        self.lblPickup.grid(row=0,column=0,sticky=W)

        self.cboPickup=ttk.Combobox(TravelFrame,textvariable=varl1,state='readonly',font=('arial',20,'bold'),width=14)
        self.cboPickup['values']=('','Arcade lane','The Fort','Cinema','Railway Station')
        self.cboPickup.current(0)
        self.cboPickup.grid(row=0,column=1)

        self.lblDrop=Label(TravelFrame,font=('arial',14,'bold'),text="Drop",bd=7)
        self.lblDrop.grid(row=1,column=0,sticky=W)

        self.cboDrop=ttk.Combobox(TravelFrame,textvariable=varl2,state='readonly',font=('arial',20,'bold'),width=14)
        self.cboDrop['values']=('','Arcade lane','The Fort','Cinema','Railway Station')
        self.cboDrop.current(0)
        self.cboDrop.grid(row=1,column=1)

        self.lblPooling=Label(TravelFrame,font=('arial',14,'bold'),text="Pooling",bd=7)
        self.lblPooling.grid(row=2,column=0,sticky=W)

        self.cboPooling=ttk.Combobox(TravelFrame,textvariable=varl3,state='readonly',font=('arial',20,'bold'),width=14)
        self.cboPooling['values']=('','1','2','3','4')
        self.cboPooling.current(1)
        self.cboPooling.grid(row=2,column=1)


        self.chkCabTax=CHECKBUTTON(TravelFrame,text="Base Charge *",variable=var1,onvalue=1,offvalue=0,font=('arial',16,'bold'),command=Cab_Tax).grid(row=3,column=0,sticky=W)
        self.txtCabTax=Label(TravelFrame,font=('arial',14,'bold'),textvariable=CabTax,bd=6,width=18,bg="white",state=DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtCabTax.grid(row=3,column=1)

        self.chkKm=CHECKBUTTON(TravelFrame,text="Distance(KMs)",variable=var2,onvalue=1,offvalue=0,font=('arial',16,'bold'),command=Kilo).grid(row=4,column=0,sticky=W)
        self.txtKm=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Km,bd=6,width=18,bg="white",state=DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtKm.grid(row=4,column=1)

        self.chkTravel_Ins=CHECKBUTTON(TravelFrame,text="Travelling Insurance",variable=var3,onvalue=1,offvalue=0,font=('arial',16,'bold'),command=Travelling).grid(row=5,column=0,sticky=W)
        self.txtTravel_Ins=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Travel_Ins,bd=6,width=18,bg="white",state=DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtTravel_Ins.grid(row=5,column=1)


        #Payment Info

        self.lblPaidTax=Label(CostFrame,font=('arial',14,'bold'),text="Paid Tax\t\t",bd=7)
        self.lblPaidTax.grid(row=0,column=1,sticky=W)
        self.txtPaidTax=Label(CostFrame,font=('arial',14,'bold'),textvariable=PaidTax,bd=7,width=10,justify=RIGHT,bg='white',relief=SUNKEN)
        self.txtPaidTax.grid(row=0,column=2)

        self.lblSubTotal=Label(CostFrame,font=('arial',14,'bold'),text="Sub Total\t\t",bd=7)
        self.lblSubTotal.grid(row=1,column=1,sticky=W)
        self.txtSubTotal=Label(CostFrame,font=('arial',14,'bold'),textvariable=SuubTotal,bd=7,width=10,justify=RIGHT,bg='white',relief=SUNKEN)
        self.txtSubTotal.grid(row=1,column=2)

        self.lblTotalCost=Label(CostFrame,font=('arial',14,'bold'),text="Total Cost\t\t",bd=7)
        self.lblTotalCost.grid(row=2,column=1,sticky=W)
        self.txtTotalCost=Label(CostFrame,font=('arial',14,'bold'),textvariable=TotalCost,bd=7,width=10,justify=RIGHT,bg='white',relief=SUNKEN)
        self.txtTotalCost.grid(row=2,column=2)

        #buttons
        self.btnTotal=Button(CostFrame,padx=18,bd=3,font=('arial',11,'bold'),width=2,text="Total",command=Total_Paid,bg='black',fg='white').grid(row=2,column=3)
        self.btnReset=Button(CostFrame,padx=18,bd=3,font=('arial',11,'bold'),width=2,text="Book",command=Reset,bg='yellow',fg='black').grid(row=2,column=4)

        
    





        






    



if __name__=='__main__':

    root=Tk()
    w=1150
    h=650
    geometry="%dx%d+%d+%d"%(w,h,50,0)
    root.geometry("500x300+320+200")
    root.title('Login Form')
    application = user(root)
    root.mainloop()