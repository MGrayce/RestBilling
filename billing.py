try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter  - we are basing this system on Python 2
except ImportError:
    # for Python3
    from tkinter import *
    from tkinter import ttk

window  = Tk()
window.geometry("950x800")
window.title("Restaurant Billing System")

#=========== field listener =========================
def quantityFieldListener(a,b,c):
    global quantityVar
    global costVar
    quantity = quantityVar.get()
    if quantity !="":
        try:
            quantity=float(quantity)
            cost = quantity*itemRate
            quantityVar.set("%.2f"%quantity)
            costVar.set("%.2f"%cost)
        except ValueError:
            quantity=quantity[:-1]
            quantityVar.set(quantity)
    else:
        quantity=0
        quantityVar.set("%.2f"%quantity)
def costFieldListener(a,b,c):
    global quantityVar
    global costVar
    global itemRate
    cost = costVar.get()
    if cost !="":
        try:
            cost = float(cost)
            quantity=cost/itemRate
            quantityVar.set("%.2f"%quantity)
            costVar.set(cost)
        except ValueError:
            cost=cost[:-1]
            costVar.set(cost)
    else:
        cost=0
        costVar.set(cost)

#=========== global variable for entries ============
#=========== login variable============
usernameVar = StringVar()
passwordVar = StringVar()

#=========main window variable=========

options=("shake","Noodles","Burger")
itemVariable=StringVar()
itemVariable.set(options[0])
quantityVar = StringVar()
quantityVar.trace('w',quantityFieldListener)
itemRate=2
rateVar = StringVar()
rateVar.set("%.2f"%itemRate)
costVar=StringVar()
costVar.trace('w',quantityFieldListener)
#==========mainTreeview============
billsTV = ttk.Treeview(height=15, columns=('Item Name', 'Quantity','Cost'))
#========= add item variables======
addItemNameVar=StringVar()
addItemRateVar=StringVar()
addItemTypeVar=StringVar()
addstoredVar=StringVar()

def adminLogin():
    titleLabel = Label(window,text="P&E Billing System",font="Arial 40",fg="green")
    titleLabel.grid(row = 0,column = 0,columnspan = 4,padx = (20,0),pady=(30,0))

    loginLabel = Label(window,text = "Admin Login",font="Arial 40")
    loginLabel.grid(row = 1,column = 2,padx=(50,0),columnspan=2,pady = 10)

    usernameLabel = Label(window,text = "Username")
    usernameLabel.grid(row = 2,column = 2,padx = 20,pady=5)

    passwordLabel = Label(window,text = "Password")
    passwordLabel.grid(row=3,column=2,padx = 20,pady=5)

    usernameEntry = Entry(window,textvariable=usernameVar)
    usernameEntry.grid(row=2,column=3,padx = 20,pady=5)

    passwordEntry = Entry(window,textvariable=passwordVar,show='*')
    passwordEntry.grid(row = 3,column=3,padx = 20,pady=5)

    loginButton = Button(window,text = "Login",width=20,height = 2)
    loginButton.grid(row = 4,column = 2,columnspan = 2)

def mainwindow():
     titleLabel = Label(window,text="P&E Billing System",font="Arial 30",fg="green")
     titleLabel.grid(row = 0,column = 0,columnspan =3,pady=(30,0))

     addNewItem = Button(window, text="Add Item", width=15, height=2)
     addNewItem.grid(row=1, column=0, padx=(10,0),pady=(10,0))

     logoutBtn = Button(window, text="Logout",width=15, height=2)
     logoutBtn.grid(row=1, column=5, padx=(10,0),pady=(10,0))

     itemLabel = Label(window, text="Select Item")
     itemLabel.grid(row=2, column=0, padx=(5,0),pady=(10,0))

     itemDropDown=OptionMenu(window,itemVariable,*options)
     itemDropDown.grid(row=2, column=1,padx=(10,0), pady=(10,0))

     rateLabel = Label(window, text="Rate")
     rateLabel.grid(row=2,column=2, padx=(10,0), pady=(10,0))

     rateValue = Label(window, textvariable=rateVar)
     rateValue.grid(row=2, column=3, padx=(10,0), pady=(10,0))

     quantityLabel = Label(window, text="Quantity")
     quantityLabel.grid(row=3, column=0,padx=(5,0),pady=(10,0))
     quantityEntry=Entry(window, textvariable=quantityVar)
     quantityEntry.grid(row=3, column=1,padx=(5,0),pady=(10,0))

     costLabel =Label(window, text="cost")
     costLabel.grid(row=3, column=2, padx=(10,0), pady=(10,0))

     costEntry=Entry(window, textvariable=costVar)
     costEntry.grid(row=3, column=3, padx=(10,0), pady=(10,0))

     buttonBill = Button(window, text="Generate Bill", width=15)
     buttonBill.grid(row=3, column=4,padx=(5,0),pady=(10,0))

     billLabel=Label(window, text="Bills",font="Arial 25")
     billLabel.grid(row=4,column=2)

     billsTV.grid(row=5, column=0, columnspan=5)

     scrollBar = Scrollbar(window, orient="vertical", command=billsTV.yview)
     scrollBar.grid(row=5, column=4, sticky="NSE")

     billsTV.configure(yscrollcommand=scrollBar.set)

     billsTV.heading('#0',text="Item Name")
     billsTV.heading('#1',text="Rate")
     billsTV.heading('#2',text="Quantity")
     billsTV.heading('#3',text="Cost")

def addItem():
     titleLabel = Label(window,text="P&E Billing System",width=30,font="Arial 40",fg="green")
     titleLabel.grid(row = 0,column = 0,columnspan = 5,pady=(30,0))

     itemNameLabel = Label(window,text="Name")
     itemNameLabel.grid(row=1, column=1, pady=(10,0))

     itemNameEntry=Entry(window, textvariable=addItemNameVar)
     itemNameEntry.grid(row=1,column=2,pady=(10,0))

     itemRateLabel = Label(window,text="Rate")
     itemRateLabel.grid(row=1, column=3, pady=(10,0))

     itemRateEntry=Entry(window, textvariable=addItemNameVar)
     itemRateEntry.grid(row=1,column=4,pady=(10,0))

     itemTypeLabel = Label(window,text="Type")
     itemTypeLabel.grid(row=2, column=1, pady=(10,0))

     itemTypeEntry=Entry(window, textvariable=addItemNameVar)
     itemTypeEntry.grid(row=2,column=2,pady=(10,0))

     storeTypeLabel = Label(window,text="Stored Type")
     storeTypeLabel.grid(row=2, column=3, pady=(10,0))

     storeEntry=Entry(window, textvariable=addItemNameVar)
     storeEntry.grid(row=2,column=4,pady=(10,0))

     AddItemButton = Button(window, text="Add Item", width=20, height=2)
     AddItemButton.grid(row=3, column=3,pady=(10,0))





mainwindow()    
window.mainloop()