# Truzz Blogg | Python + Tkinter | How to create a GUI
# How to create a registration form using Python + Tkinter

# Let's import tkinter 
from tkinter import *
#import tkinter as tk
 
# Manipulate data from registration fields 
def send_data():
  name_data = name.get()
  last_name_data = last_name.get()
  telephone_data = telephone.get()
  email_data = email.get()
  username_data = username.get()
  password_data = password.get()
  status_data = str(status.get())
  print(name_data,"\t",last_name_data,"\t",telephone_data,"\t",email_data,"\t",username_data,"\t", password_data,"\t", status_data)

  newfile = open ("registration.txt", "a")
  newfile.write(name_data)
  newfile.write("\t")
  newfile.write(last_name_data)
  newfile.write("\t")
  newfile.write(telephone_data)
  newfile.write("\t")
  newfile.write(email_data)
  newfile.write("\t")
  newfile.write(username_data)
  newfile.write("\t")
  newfile.write(password_data)
  newfile.write("\t")
  newfile.write(status_data)
  newfile.write("\t")
 
 
#  Delete data from previous event
  
  name_entry.delete(0, END)
  last_name_entry.delete(0,END)
  telephone_entry.delete(0, END)
  email_entry.delete(0, END)
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  status_entry.delete(0, END)

# Creación new instancia - Class Tk()  
mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("Registro de Usuarios")
mywindow.resizable(False,False)
mywindow.config(background = "#FFFFFF")
main_title = Label(text = "Registro Usuario | HVDistriTec", font = ("Cambria", 14), bg = "#00BDFF", fg = "black", width = "500", height = "2")
main_title.pack()

# Define Label Fields 
name_label = Label(text = "Nombres", bg = "#FFFFFF")
name_label.place(x = 20, y = 70)
last_name_label = Label(text = "Apellidos", bg = "#FFFFFF")
last_name_label.place(x = 300, y = 70)
telephone_label = Label(text = "Telefono", bg = "#FFFFFF")
telephone_label.place(x = 20, y = 120)
email_label = Label(text = "Email", bg = "#FFFFFF")
email_label.place(x = 300, y = 120)
username_label = Label(text = "Nickname", bg = "#FFFFFF")
username_label.place(x = 20, y = 170)
password_label = Label(text = "Password", bg = "#FFFFFF")
password_label.place(x = 300, y = 170)
status_label = Label(text = "Status", bg = "#FFFFFF")
status_label.place(x = 20, y = 220)
 
# Get and store data from users 
name = StringVar()
last_name = StringVar()
telephone = StringVar()
email = StringVar()
username = StringVar()
password = StringVar()
status = StringVar()
 
name_entry = Entry(textvariable = name, width = "40")
last_name_entry = Entry(textvariable = last_name, width = "40")
telephone_entry = Entry(textvariable = telephone, width = "40")
email_entry = Entry(textvariable = email, width = "40")
username_entry = Entry(textvariable = username, width = "40")
password_entry = Entry(textvariable = password, width = "40",  show = "*")
status_entry = Entry(textvariable = status, width = "40")
 
name_entry.place(x = 20, y = 93)
last_name_entry.place(x = 300, y = 93)
telephone_entry.place(x = 20, y = 143)
email_entry.place(x = 300, y = 143)
username_entry.place(x = 20, y = 197)
password_entry.place(x = 300, y = 197)
status_entry.place(x = 20, y = 247)
 
# Submit Button
submit_btn = Button(mywindow,text = "Registrar", width = "30", height = "2", command = send_data, bg = "#00BDFF")
submit_btn.place(x = 380, y = 320)

mywindow.mainloop()


