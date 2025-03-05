import tkinter as tkinterfrom 
import messagebox

def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":

        messagebox.showerror("Login Failed! Please enter username and password. ")

        return

    if username == "user" or password =="password":

        messagebox.showinfo ("Login Successfully!!")

    else:
        messagebox.showerror("Login Failed! Please enter the correct username and password.")


window = tk.Tk()
window.title("Login Form")
window.geometry(300*150)

username_label = tk.Label(window, text = "USERNAME: ")
username_label.grid (row=0, column=0, padx=10, pady=10, sticky"w")

username_entry = tk.Entry(window)
username_entry.grid (row=0, column=1, padx=10, pady=10)

password_label =tk.Label(window, text= "PASSWORD: ")
password_label.grid (row=1, column=0, padx=10, pady=10, sticky"w")

password_entry = tk.Entry (window, show"*")
password_entry.grid (row=1, column=1, padx=10, pady=10)

login_button = tk.Button(window, text= "LOGIN", command=check_login)
login_button.grid (row=2, column=0, columnspan=2, pady=10)

window.mainloop()