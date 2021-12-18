from tkinter import *
from tkinter import messagebox
from datetime import date
today=date.today()
import sqlite3
conn=sqlite3.connect('record.db')
conn.execute('''CREATE TABLE IF NOT EXISTS BILL(DATE NOT NULL,BILL_NO INT,AMOUNT INT)''')
conn.commit()
conn.close()



root=Tk()
root.geometry('800x600')
root.title('Royal Cliff Billing System')
root.wm_iconbitmap('hotel_vacations_hotel_buildings_holidays_icon_128587.ico')
name=Label(root,text='ROYAL CLIFF',font=("Castellar",30)).grid(row=1,column=2)
Label(root).grid(row=2,column=1)
menu=Label(root,text='Menu',font=('Castellar',20)).grid(row=3,column=1)
price=Label(root,text='Price',font=('Castellar',20)).grid(row=3,column=2)
quan=Label(root,text='Quantity',font=('Castellar',20)).grid(row=3,column=3)


####### To generate bill no.  
def billno():

    conn=sqlite3.connect('record.db')    
    cursor=conn.execute("SELECT * FROM BILL")
    c=cursor.fetchall()
    if c ==[]:
        return 1
    elif c[len(c)-1][0]!=str(today):
        return 1

    else:
        return (c[len(c)-1][1])+1
    print(c)
    conn.close()


def bill():
    b=billno()
    sum=0

    top=Tk()
    top.geometry('600x450')
    top.title('Bill')
    Label(top,text='ROYAL CLIFF',font=("Castellar",20)).grid(row=0,column=0,columnspan=3)
    Label(top,text='Date',font=('Castellar',14)).grid(row=2,column=1)#date
    Label(top,text=str(today),font=('Castellar',14)).grid(row=3,column=1)#date
    Label(top,text='Bill No.',font=('Castellar',14)).grid(row=2,column=4)#billno
    Label(top,text=str(b),font=('Castellar',14)).grid(row=3,column=4)#billno
    Label(top,text='Items',font=("Castellar",14)).grid(row=4,column=1)#items
    Label(top,text='Price',font=('Castellar',14)).grid(row=4,column=2)#price
    Label(top,text='Quantity',font=('Castellar',14)).grid(row=4,column=3)#Quantity


    
    if dosavar.get()==1:
        sum=sum+(qdosavar.get()*100)
        Label(top,text='Dosa',font=('Castellar',14)).grid(row=5,column=1,sticky = W,pady=2)
        Label(top,text='100',font=('Castellar',14)).grid(row=5,column=2)
        Label(top,text=qdosavar.get(),font=('Castellar',14)).grid(row=5,column=3)
        
    if thalivar.get()==1:
        sum=sum+(qthalivar.get()*160)
        Label(top,text='Thali',font=('Castellar',14)).grid(row=6,column=1,sticky = W,pady=2)
        Label(top,text='160',font=('Castellar',14)).grid(row=6,column=2)
        Label(top,text=qthalivar.get(),font=('Castellar',14)).grid(row=6,column=3)

    if pizzavar.get()==1:
        sum=sum+(qpizzavar.get()*200)
        Label(top,text='Pizza',font=('Castellar',14)).grid(row=7,column=1,sticky = W,pady=2)
        Label(top,text='200',font=('Castellar',14)).grid(row=7,column=2)
        Label(top,text=qpizzavar.get(),font=('Castellar',14)).grid(row=7,column=3)

    if soupvar.get()==1:
        sum=sum+(qsoupvar.get()*120)
        Label(top,text='Soup',font=('Castellar',14)).grid(row=8,column=1,sticky = W,pady=2)
        Label(top,text='120',font=('Castellar',14)).grid(row=8,column=2)
        Label(top,text=qsoupvar.get(),font=('Castellar',14)).grid(row=8,column=3)

    if noodlevar.get()==1:
        sum=sum+(qnoodlevar.get()*130)
        Label(top,text='Noodles',font=('Castellar',14)).grid(row=9,column=1,sticky = W,pady=2)
        Label(top,text='130',font=('Castellar',14)).grid(row=9,column=2)
        Label(top,text=qnoodlevar.get(),font=('Castellar',14)).grid(row=9,column=3)


    def submit():
        
        conn=sqlite3.connect('record.db')
        conn.execute("INSERT INTO BILL(DATE,BILL_NO,AMOUNT) VALUES(?,?,?)",(today,b,sum))
        conn.commit()
        conn.close()
        

    Label(top,text='Total Bill',font=('Castellar',14)).grid(row=10,column=1)
    Label(top,text=sum,font=('Castellar',14)).grid(row=10,column=2)
    Label(top,text=qdosavar.get()+qthalivar.get()+qpizzavar.get()+qsoupvar.get()+qnoodlevar.get(),font=('Castellar',14)).grid(row=10,column=3)
    Button(top,text='Submit',command=submit).grid(row=11,column=2)
##l=[dosavar.get(),thalivar.get(),pizzavar(),soupvar.get(),noodlevar.get()]
##ilist=['Dosa','Thali','Pizza','Soup','Noodles']
##    plist=[100,160,200,120,130]
##   for i in list:
##       if i==1:
##           Label(top,text=ilist[i],font=('Castellar',14)).grid(row=i+5,column=1)
##            Label(top,text=plist[i],font=('Castellar',14)).grid(row=i+6,column=2)
##            Label(top,text=qdosavar.get(),font=('Castellar',14)).grid(row=i+7,column=3)   




#Check Buttons
dosavar=IntVar()
thalivar=IntVar()
pizzavar=IntVar()
soupvar=IntVar()
noodlevar=IntVar()

dosa=Checkbutton(root,text='Dosa',variable=dosavar,font=('Castellar',14)).grid(row=4,column=1,sticky = W,pady=2)
thali=Checkbutton(root,text='Thali',variable=thalivar,font=('Castellar',14)).grid(row=5,column=1,sticky = W,pady=2)
pizza=Checkbutton(root,text='Pizza',variable=pizzavar,font=('Castellar',14)).grid(row=6,column=1,sticky = W,pady=2)
soup=Checkbutton(root,text='Soup',variable=soupvar,font=('Castellar',14)).grid(row=7,column=1,sticky = W,pady=2)
noodel=Checkbutton(root,text='Noodels',variable=noodlevar,font=('Castellar',14)).grid(row=8,column=1,sticky = W,pady=2)


#Prices
pdosa=Label(root,text='Rs.100',font=('Castellar',14)).grid(row=4,column=2,pady=2)
pthali=Label(root,text='Rs.160',font=('Castellar',14)).grid(row=5,column=2,pady=2)
ppizza=Label(root,text='Rs.200',font=('Castellar',14)).grid(row=6,column=2,pady=2)
psoup=Label(root,text='Rs.120',font=('Castellar',14)).grid(row=7,column=2,pady=2)
pnoodle=Label(root,text='Rs.130',font=('Castellar',14)).grid(row=8,column=2,pady=2)



#Quantity
qdosavar=IntVar()
qthalivar=IntVar()
qpizzavar=IntVar()
qsoupvar=IntVar()
qnoodlevar=IntVar()

qdosa=Entry(root,textvariable=qdosavar).grid(row=4,column=3)
qthali=Entry(root,textvariable=qthalivar).grid(row=5,column=3)
qpizza=Entry(root,textvariable=qpizzavar).grid(row=6,column=3)
qsoup=Entry(root,textvariable=qsoupvar).grid(row=7,column=3)
qnoodle=Entry(root,textvariable=qnoodlevar).grid(row=8,column=3)

#buttons
gbill=Button(root,text='Genetare Bill',command=bill).grid(row=3,column=4,padx=20)

root.mainloop()
