import tkinter
import tkinter.messagebox
root = tkinter.Tk()
root.title("Cute_game_login")
root.geometry('600x400')
root.resizable(False, False)
username_var = tkinter.StringVar()
password_var = tkinter.StringVar()

def login_button():
    username= username_var.get()
    password = password_var.get()
    if(username == "admin" and password == "1234"):
        tkinter.messagebox.showinfo("Login", "Successful")
    else:
        tkinter.messagebox.showerror("Login", "Login Failed")

tkinter.Label(root, text="Login", font="arial 30 bold").pack()
tkinter.Label(root, text="username", font="arial 10").place(x= 20, y= 80)
tkinter.Label(root, text="password", font="arial 10").place(x=20, y= 110)
tkinter.Entry(root, textvariable= username_var).place(x=100, y=80)
tkinter.Entry(root, textvariable= password_var, show="*").place(x= 100, y= 110)
tkinter.Button(root, text="Login", command=login_button).place(x= 100, y= 140)

root.mainloop()