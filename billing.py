try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter  - we are basing this system on Python 2
except ImportError:
    # for Python3
    from tkinter import *

window  = Tk()
window.geometry("600x600")
window.title("Restaurant Billing System")

usernameVar = StringVar()
passwordVar = StringVar()
def adminLogin():
    titleLabel = Label(window,text="P&E Billing System")
    titleLabel.grid(row = 0,column = 0,columnspan = 2,padx = (20,0),pady=(30,0))

    loginLabel = Label(window,text = "Admin Login")
    loginLabel.grid(row = 1,column = 2,padx = 20,pady = 10)

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

adminLogin()    
window.mainloop()